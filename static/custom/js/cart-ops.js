function addToCart(id) {
  var url = $('#Url').attr('data-url');
  $.ajax({
    url: url,
    data: {
      'product_id': id,
    },
    dataType: 'json',
    success: function(data) {
      if (data.is_added) {
        html_code = '<div class="alert alert-warning" id="added_message" role="alert">';
        html_code += data.message;
        html_code += '</div>';
        $('#cart-badge-total').text(data.total_items);
        $('.navbar').after(html_code);
        var fade_out = function() {
          $('#added_message').fadeOut(2000, function() {
            $(this).remove();
          });
        }
        setTimeout(fade_out, 1000);
      }
    }
  });
}


function updateQuantity(id, op) {
  // Fast But Insecure Way:
  //   1. If some clicks too fast, ajax can not be able to reach after him
  //      and consequently the quantity in input and in cart badge, also
  //      total price will show wrong values(
  // foo = document.getElementById("quantity-"+id);
  // intVal = parseInt(foo.value, 10);
  // if (op == "0") {
  //   if (intVal > 1) {
  //     intVal -= 1;
  //   }
  // } else {
  //   intVal += 1;
  // }
  // foo.value = intVal;
  $.ajax({
    url: 'ajax/update-cart-item-quantity/',
    data: {
      'cart_item_id': id,
      'operation': op,
    },
    dataType: 'json',
    success: function(data) {
      if (data.is_updated) {
        document.getElementById("quantity-"+id).value = data.quantity;
        total = document.getElementById("total").textContent = data.total_price;
        document.getElementById("cart-badge-total").textContent = data.total_items;
      }
    }
  });
}




function deleteCartItem(id) {
  var action = confirm('Are you sure you want to delete this cart item?');
  if (action != false) {
    $.ajax({
      url: 'ajax/delete-cart-item/',
      data: {
        'cart_item_id': id,
      },
      dataType: 'json',
      success: function(data) {
        if (data.is_deleted) {
          raw = document.getElementById("cart_item_row"+id);
          raw.remove();
          total = document.getElementById("total").textContent = data.total_price;
          document.getElementById("cart-badge-total").textContent = data.total_items;
          if (data.is_last) {
            document.getElementById("total-price-row").remove();
            table = document.getElementById("table");
            el = document.createElement("h3");
            el.textContent = "Your cart is empty.";
            el.className = "display-4 text-center";
            table.parentNode.insertBefore(el, table.nextSibling);
          }
        }
      }
    });
  }
}
