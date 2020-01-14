from django.db import models
from django.core.exceptions import ObjectDoesNotExist

from users.models import CustomUser
from product.models import Product


class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get('cart_id', None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                if not hasattr(request.user, 'cart'):
                    cart_obj.user = request.user
                    cart_obj.save()
                else:
                    users_cart_obj = Cart.objects.get(user=request.user)
                    for item in cart_obj.cartitem_set.all():
                        try:
                            obj = users_cart_obj.cartitem_set.get(product=item.product)
                            obj.quantity += item.quantity
                            obj.save()
                        except ObjectDoesNotExist:
                            users_cart_obj.cartitem_set.create(product=item.product, quantity=item.quantity)
                    cart_obj.delete()
                    cart_obj = users_cart_obj
                    request.session['cart_id'] = users_cart_obj.id
        else:
            if not request.user.is_anonymous:
                if request.user.cart is not None:
                    cart_obj = Cart.objects.get(user=request.user)
            else:
                cart_obj = Cart.objects.new(user=request.user)
            request.session['cart_id'] = cart_obj.id
        return cart_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)


class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name='cart')
    # cart_item = models.ManyToManyField(CartItem, blank=True)
    objects = CartManager()

    def total_items_num(self):
        total = 0
        for item in self.cartitem_set.all():
            total += item.get_quantity()
        return total

    def total_items_price(self):
        total_price = 0
        for item in self.cartitem_set.all():
            total_price += item.items_price()
        return total_price

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, default=1)

    def items_price(self):
        return self.product.price * self.quantity

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return self.product.name + ' - ' + str(self.quantity)
