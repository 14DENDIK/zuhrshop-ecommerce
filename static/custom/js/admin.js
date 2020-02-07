function deleteCart(cart_id) {
  var url = $('#Url').attr('data-url');
  $.ajax({
    url: url,
    data: {
      'cart_id': cart_id
    },
    dataType: 'json',
    success: function(data) {
      if (data.is_deleted) {
        cart = document.getElementById("cart-"+cart_id);
        cart.remove();
      }
    }
  });
}

function deleteBrand(brand_id) {
  var url = $('#Url').attr('data-url');
  $.ajax({
    url: url,
    data: {
      'brand_id': brand_id
    },
    dataType: 'json',
    success: function(data) {
      if (data.is_deleted) {
        brand = document.getElementById("brand-"+brand_id);
        brand.remove();
      } else  {
        html_code = '<div class="alert alert-danger" id="added_message" role="alert">';
        html_code += data.message;
        html_code += '</div>';
        $('#forMessages').after(html_code);
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

function deleteProduct(product_id) {
  var url = $('#Url').attr('data-url');
  $.ajax({
    url: url,
    data: {
      'product_id': product_id
    },
    dataType: 'json',
    success: function(data) {
      if (data.is_deleted) {
        product = document.getElementById("product-"+product_id);
        product.remove();
      }
    }
  });
}

function deleteAccount(account_id) {
  var url = $('#Url').attr('data-url');
  $.ajax({
    url: url,
    data:  {
      'account_id': account_id
    },
    dataType: 'json',
    success: function(data) {
      if (data.is_changed) {
        account = document.getElementById('activeStatus-' + account_id);
        badge =  document.getElementById('badgeColor-' + account_id);
        if (data.is_active) {
          account.className = "fas fa-check";
          badge.classList.remove('badge-danger');
          badge.classList.add('badge-success');
        } else {
          account.className = "fas fa-times";
          badge.classList.remove('badge-success');
          badge.classList.add('badge-danger');
        }
      }
    }
  });
}

// $('#createPhone').on('click', function() {
//   var form = document.getElementById('phoneCreationForm');
//   var form2 = document.getElementById('accessoryCreationForm');
//   form2.style.display = "none";
//   form.style.display = "block";
// })
//
// $('#createAccesory').on('click', function() {
//   var form = document.getElementById('phoneCreationForm');
//   var form2 = document.getElementById('accessoryCreationForm');
//   form.style.display = "none";
//   form2.style.display = "block";
// })

$('#id_is_on_sale').on('click', function() {
  var field = document.getElementById('id_on_sale_price');
  if (this.checked) {
    field.disabled = false;
    field.focus();
  } else {
    field.value = null;
    field.disabled = true;
  }
});

function filterCat(n) {
  var input, filter, table, tr, td, i, txtValue, j;
  if (n == 0) {
    input = 'all';
  } else if (n == 1) {
    input = 'phone';
  } else if (n == 2) {
    input = 'accessory';
  }
  filter = input.toUpperCase();
  table = document.getElementById("productTable");
  tr = table.getElementsByTagName("tr");
  if (input == 'all') {
    for (j = 0; j < tr.length; j++) {
      tr[j].style.display = "";
    }
  } else {
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[3];
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  }
}


function sortTableStr(n) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById("productTable");
  switching = true;
  //Set the sorting direction to ascending:
  dir = "asc";
  /*Make a loop that will continue until
  no switching has been done:*/
  while (switching) {
    //start by saying: no switching is done:
    switching = false;
    rows = table.rows;
    /*Loop through all table rows (except the
    first, which contains table headers):*/
    for (i = 1; i < (rows.length - 1); i++) {
      //start by saying there should be no switching:
      shouldSwitch = false;
      /*Get the two elements you want to compare,
      one from current row and one from the next:*/
      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];
      /*check if the two rows should switch place,
      based on the direction, asc or desc:*/
      if (dir == "asc") {
        if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
          //if so, mark as a switch and break the loop:
          shouldSwitch= true;
          break;
        }
      } else if (dir == "desc") {
        if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
          //if so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      }
    }
    if (shouldSwitch) {
      /*If a switch has been marked, make the switch
      and mark that a switch has been done:*/
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      //Each time a switch is done, increase this count by 1:
      switchcount ++;
    } else {
      /*If no switching has been done AND the direction is "asc",
      set the direction to "desc" and run the while loop again.*/
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}

function sortTableInt(n) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById("productTable");
  switching = true;
  //Set the sorting direction to ascending:
  dir = "asc";
  while (switching) {
    //start by saying: no switching is done:
    switching = false;
    rows = table.rows;
    /*Loop through all table rows (except the
    first, which contains table headers):*/
    for (i = 1; i < (rows.length - 1); i++) {
      //start by saying there should be no switching:
      shouldSwitch = false;
      /*Get the two elements you want to compare,
      one from current row and one from the next:*/
      if (n == -1) {
        x = rows[i].getElementsByTagName("TH")[0];
        y = rows[i + 1].getElementsByTagName("TH")[0];
      } else {
        x = rows[i].getElementsByTagName("TD")[n];
        y = rows[i + 1].getElementsByTagName("TD")[n];
      }

      //check if the two rows should switch place:
      if (dir == "asc") {
        if (Number(x.innerHTML) > Number(y.innerHTML)) {
          //if so, mark as a switch and break the loop:
          shouldSwitch= true;
          break;
        }
      } else if (dir == "desc") {
        if (Number(x.innerHTML) < Number(y.innerHTML)) {
          //if so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      }
    }
    if (shouldSwitch) {
      /*If a switch has been marked, make the switch
      and mark that a switch has been done:*/
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      //Each time a switch is done, increase this count by 1:
      switchcount ++;
    } else {
      /*If no switching has been done AND the direction is "asc",
      set the direction to "desc" and run the while loop again.*/
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}

$(document).ready(function () {

    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
        $(this).toggleClass('active');
    });

});
