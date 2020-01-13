from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import Cart, CartItem
from product.models import Product


class CartView(View):
    def get(self, request):
        # cart_id = request.session.get('cart_id', None)
        cart = Cart.objects.get(id=request.session.get('cart_id', None))
        # print("Num of Cart Items:")
        # print(cart.total_items_num())
        return render(request, 'cart/cart.html', {})


class AddCartItemView(View):
    def get(self, request):
        product_id = request.GET.get('product_id', None)
        if product_id is not None:
            product_obj = Product.objects.get(id=product_id)
            cur_cart_id = request.session.get('cart_id', None)
            if cur_cart_id is not None:
                cart_obj = Cart.objects.get(id=cur_cart_id)
                try:
                    allready_existing_item = cart_obj.cartitem_set.get(product=product_obj)
                    allready_existing_item.quantity += 1
                    allready_existing_item.save()
                except ObjectDoesNotExist:
                    cart_obj.cartitem_set.create(product=product_obj)
                total_items = cart_obj.total_items_num()
                data = {
                    'is_added': True,
                    'message': 'Product successfully added to your cart.',
                    'total_items': total_items
                }
        else:
            raise ObjectDoesNotExist('Trying add not existing item.')
        return JsonResponse(data)
        # if self.user.is_authenticated:
        #     user = self.request.user
        #     product_id = request.GET.get('product_id', None)
        #     product = Product.objects.get(id=product_id)
        #     cart = Cart.objects.get(user=user)
        #     try:
        #         allready_existing_item = CartItem.objects.get(cart=cart, product=product)
        #         allready_existing_item.quantity += 1
        #         allready_existing_item.save()
        #     except ObjectDoesNotExist:
        #         CartItem.objects.create(cart=cart, product=product)
        #     data = {
        #         "is_added": True,
        #         "success_message": "Product successfully added to the cart."
        #     }
        # return JsonResponse(data)


class DeleteCartItemView(View):
    def get(self, request):
        # Gets cart items id through id
        cart_item_id = request.GET.get('cart_item_id', None)
        if cart_item_id is not None:
            # Gets cart item with that id
            cart_item_obj = CartItem.objects.get(id=cart_item_id)
            # Gets cart object of that item
            cart = cart_item_obj.cart
            # Deletes cart items that needs to be deleted
            cart_item_obj.delete()
            # Gets total price of items of the cart
            total_price = cart.total_items_price()
            # Gets total number of cart items
            total_items = cart.total_items_num()
            # Checks wheter deleted item is the last one
            if cart.cartitem_set.all().count() == 0:
                is_last = True
            else:
                is_last = False
            data = {
                'is_deleted': True,
                'total_price': total_price,
                'is_last': is_last,
                'total_items': total_items
            }
        else:
            data = {
                'is_deleted': False
            }
        return JsonResponse(data)


class UpdateCartItemQuantityView(View):
    def get(self, request):
        cart_item_id = request.GET.get('cart_item_id', None)
        operation = request.GET.get('operation', None)
        if cart_item_id is not None:
            cart_item_obj = CartItem.objects.get(id=cart_item_id)
            cart = cart_item_obj.cart
            if operation is not None:
                if operation == "1":
                    cart_item_obj.quantity += 1
                elif operation == "0":
                    if cart_item_obj.quantity > 1:
                        cart_item_obj.quantity -= 1
                else:
                    raise ValueError("Not Existing Operation")
                cart_item_obj.save()
                # Gets total price of items of the cart
                total_price = cart.total_items_price()
                # Gets total number of cart items
                total_items = cart.total_items_num()
                # Checks wheter deleted item is the last one
                data = {
                    'is_updated': True,
                    'quantity': cart_item_obj.quantity,
                    'total_price': total_price,
                    'total_items': total_items,
                }
            else:
                raise Exception("Empty Operation.")
        else:
            raise Exception("Empty Cart Item Was Send")
        return JsonResponse(data)

# class SongLikeView(LoginRequiredMixin, View):
#
#     def get(self, request):
#         user1 = self.request.user
#         songId = request.GET.get('songId', None)
#         song1 = Song.objects.get(pk=songId)
#
#         try:
#             user_likes_song = song1.like_set.get(user=user1)
#             user_likes_song.delete()
#             data = {
#                 'is_liked': False
#             }
#         except ObjectDoesNotExist:
#             user_likes_song = Like.objects.create(song=song1, user=user1)
#             data = {
#                 'is_liked': True
#             }
#
#         return JsonResponse(data)
