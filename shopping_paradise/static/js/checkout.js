function confirmOrder(cart, customer,shipping){
	console.log('User is authenticated, sending data...')

		var url = '/process_order/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'cart':cart, 'customer':customer,'shipping':shipping})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
			// clears all cart information from javascript sessions
			localStorage.clear()
			// redirects to another url
		    location.replace('/thankyou/'+data['order_id'])
		});
}

$( document ).ready(function() {
    // if (user != "AnonymousUser"){
    //     $('#user-info').hide()
    // }

    $('#total_items').html(cartLength());
    $('#total').html("€ "+calculateTotal());

	$('#checkout').submit(function(e){
		e.preventDefault() 
		customer = {
			"name":$('#id_name').val(),
			"email":$('#id_email').val()
		}
		shipping = {
				"address":$('#id_address').val(),
				"city":$('#id_city').val(),
				"state":$('#id_state').val(),
				"zipcode":$('#id_zipcode').val()
		}
		confirmOrder(cart,customer,shipping);

	})

});