// inititlaize your cart from javascript jocalStorage
if(localStorage.getItem('cart') == null)
{
	var cart={};
}
else{
	cart= JSON.parse(localStorage.getItem('cart'));
}
function calculateTotal(){
    var sum = 0;
    for (item in cart){
        sum += cart[item].quantity * cart[item].price
    }
    return sum;
}

// function to get cart length
function cartLength() { 
    var count = 0;
    for ( var key in cart){
        count += cart[key].quantity 
    }
    return count;
}
// all the magic happens for cart
$( document ).ready(function() {
    
    
    // jquery implementation for updating an html tag/element( div, span...etc) with exiting cart items
    $('#cart-items').html(cartLength());
    // jquery click event to add items into the javascript cart object 
    $('.add-to-cart').click(function(){
		console.log(this.dataset.price);
        var idstr= this.dataset.product.toString();
		// the cart attributes(quantity) is being updated
        if(cart[idstr]!= undefined) {

			quantity = cart[idstr].quantity
            cart[idstr].quantity =  quantity + 1;
        }
        else {
			// cart being inititlzied
            cart[idstr] = {quantity: 1,name: this.dataset.name,price: this.dataset.price,category: this.dataset.category,image:this.dataset.image };
        }
        localStorage.setItem('cart', JSON.stringify(cart));
        $('#cart-items').html(cartLength(cart));
    });
});



