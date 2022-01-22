
from operator import truediv
import pdb
from django.shortcuts import render
from django.template import context
from django.http import JsonResponse
from products.forms import CustomerForm, ShippingForm
from products.models import *
import json
import datetime


def cart_view(request):
    return render(request, 'cart.html')


def thankyou(request, id=None):
    order = Order.objects.get(id=id)
    items = order.orderitem_set.all()
    context = {'items': items, 'order': order}
    return render(request, 'thankyou.html', context)


def checkout_view(request):
    customer_form = CustomerForm(None)
    shipping_form = ShippingForm(None)
    context = {
        'customer_form': customer_form,
        'shipping_form': shipping_form,
    }
    return render(request, 'checkout.html', context)


def processOrder(request):
    # load the data
    # request.body is a json string, so we need to make it a json object in order to work with it, that is why we use json.loads
    data = json.loads(request.body)
    # create a transaction id using datetime timestamp
    transaction_id = datetime.datetime.now().timestamp()
    # check if a user is authenticated else guest uuser
    if request.user.is_authenticated:
        customer, created = Customer.objects.get_or_create(user=request.user)
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
    else:
        # Anonomus user
        name = data['customer']['name']
        email = data['customer']['email']
        customer, created = Customer.objects.get_or_create(
            name=name, email=email)
        order = Order.objects.create(customer=customer, complete=False)

    for item, info in data['cart'].items():
        product = Product.objects.get(id=item)
        OrderItem.objects.create(
            product=product,
            order=order,
            quantity=info['quantity']
        )

    order.transaction_id = transaction_id
    order.complete = True
    order.save()

    ShippingAddress.objects.create(
        customer=customer,
        order=order,
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        state=data['shipping']['state'],
        zipcode=data['shipping']['zipcode'],
    )

    return JsonResponse({'message': 'Order created', 'order_id': order.id})
