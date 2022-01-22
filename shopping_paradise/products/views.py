from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework import viewsets
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import Product, Category
from products.serializers import ProductSerializer, CategorySerializer


class ProductListView(ListView):
    model = Product
    Product.objects.filter().order_by('name')
    template_name = 'product_list.html'
    context_object_name = 'products'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_create.html'
    fields = '__all__'
    success_url = reverse_lazy('product_list')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

class ProductUpdateView(PermissionRequiredMixin,UpdateView):
    permission_required = 'products.change_product'
    model = Product
    template_name = 'product_update.html'
    context_object_name = 'product'
    fields = '__all__'
    success_url = reverse_lazy('product_list')


class ProductDeleteView(PermissionRequiredMixin,DeleteView):

    model = Product
    permission_required = 'products.delete_product'
    template_name = 'product_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('product_list')


def counter(request):
    # Number of visits to this view, stored in the session variable.
    visits_count = request.session.get('visits_count', 0)
    request.session['visits_count'] = visits_count + 1

    context = {
        'visits_count': visits_count
    }

    # Render the HTML template passing data in the context.
    return render(request, 'counter.html', context=context)


class ProductViewSet(LoginRequiredMixin,viewsets.ModelViewSet):
    permission_required = 'products.list_products'
    queryset = Product.objects.all().order_by('-name')
    serializer_class = ProductSerializer


class CategoryViewSet(PermissionRequiredMixin,viewsets.ModelViewSet):
    permission_required = 'categories.list_categories'
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import MyForm


def my_form(request):
    # If this is a POST request we need to process the form data.
    if request.method == 'POST':
        # Create a form instance and populate it
        # with data from the request.
        form = MyForm(request.POST)
        # Check whether it is valid.
        if form.is_valid():
            # Does any data require extra processing?
            # If so, do it in form.cleaned_data as required.
            # ...
            # Redirect to a new URL.
            return HttpResponseRedirect('/thank-you')
        else:
            # Redirect back to the same page if the data
            # was invalid.
            return render(request, 'my_form.html', {'form': form})

    # If a GET (or any other method) we will create a blank form.
    else:
        form = MyForm()

    return render(request, 'my_form.html', {'form': form})
