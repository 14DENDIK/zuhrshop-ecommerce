from brands.models import Brand
from cart.models import Cart


def add_variable_to_context(request):
    cart = Cart.objects.new_or_get(request)
    brands = Brand.objects.all()
    context = {
        'brands': brands,
        'cart': cart
    }
    return context
