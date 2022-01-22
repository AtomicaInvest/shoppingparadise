$( document ).ready(function() {

	var html = "<tr><th>Image</th><th>Name</th><th>Price</th><th>Quantity</th><th>Category</th></tr>"
	for (product_id in cart ) {
        html += "<tr>";
		html += "<td><img src="+ cart[product_id].image+" width=50 height=50 class='product'  alt='My image'></td>"
        html += "<td>"+ cart[product_id].name+"</td>"
        html += "<td>"+ cart[product_id].price+"</td>"
        html += "<td>"+ cart[product_id].quantity+"</td>"
        html += "<td>"+ cart[product_id].category+"</td>"
        html += "<td><button class='btn remove-from-cart' data-id='"+product_id+"'><i class='fa fa-trash'></i></button></td>"
        html += "</tr>";

	}
    html += "<tr><td colspan='5'></td><td> <b>Total:</b> <span id='total-amount'> "+calculateTotal()+"</span></td></tr>"
	$('#display-cart').html(html)
    $('.remove-from-cart').click(function(){
        if(cart[this.dataset.id].quantity === 1){
            delete cart[this.dataset.id]
        }else{
            cart[this.dataset.id].quantity = cart[this.dataset.id].quantity - 1
        }
        localStorage.setItem('cart', JSON.stringify(cart));
        // reloads the page from cache, faster but not up to date
        location.reload();
        // reloads the page from server, slower but always uptp date
        // location.reload(true);
    });

    



});