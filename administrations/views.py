from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.backends import BaseBackend
from django.http import Http404, JsonResponse
from django.core.exceptions import PermissionDenied

from users.models import CustomUser
from product.models import Product, ProductImage
from cart.models import Cart
from brands.models import Brand

from product.forms import PhoneCreationForm, ProductImageFormset, AccessoryCreationForm
from brands.forms import BrandCreationForm


class UserCheckingView(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        if self.request.user.is_staff:
            return True
        else:
            return False


class MainAdminView(UserCheckingView, View):

    def get(self, request):

        context = {
            'url_name': 'dashboard',
        }
        return render(request, 'administrations/admin-main.html', context)


class ProductListAdminView(UserCheckingView, View):

    def get(self, request):
        # print(request.path)
        # a = request.path.split('/')[2]
        # print(a)
        # print(request.user.is_active)
        products = Product.objects.all()
        context = {
            'products': products,
            'url_name': 'products',
        }
        return render(request, 'administrations/admin-product.html', context)


class ProductAddAdminView(UserCheckingView, View):
    def get(self, request, born):
        if born == "phone":
            form = PhoneCreationForm()
        elif born == "accessory":
            form = AccessoryCreationForm()
        else:
            raise Http404("No such element")
        formset = ProductImageFormset(queryset=ProductImage.objects.none())
        context = {
            'form': form,
            'formset': formset,
            'born': born,
            'url_name': 'products',
        }
        return render(request, 'administrations/admin-add-product.html', context)

    def post(self, request, born):
        if born == 'phone':
            form = PhoneCreationForm(request.POST or None, request.FILES or None)
        elif born == 'accessory':
            form = AccessoryCreationForm(request.POST or None, request.FILES or None)
        else:
            raise PermissionDenied()
        formset = ProductImageFormset(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            product = form.save(commit=False)
            product.main_image = request.FILES['main_image']
            product.category = born
            product.save()
            print(formset.total_form_count())
            print(formset.initial_form_count())
            for f in formset:
                try:
                    image = ProductImage(product=product, image=f.cleaned_data['image'])
                    image.save()
                except KeyError as e:
                    break
                except Exception as e:
                    raise e

        return redirect('administrations:admin-products')


class ProductDeleteAdminView(UserCheckingView, View):
    def get(self, request):
        product_id = request.GET.get('product_id', None)
        if product_id is not None:
            Product.objects.get(id=product_id).delete()
            data = {
                'is_deleted': True
            }
        else:
            data = {
                'is_deleted': False
            }
        return JsonResponse(data)


class AccountsAdminView(UserCheckingView, View):

    def get(self, request, who):
        if who == 'staff':
            accounts = CustomUser.objects.filter(is_staff=True)
        elif who == 'clients':
            accounts = CustomUser.objects.filter(is_staff=False)
        else:
            raise Http404("Page Does Not Exist.")
        context = {
            'url_name': who,
            'accounts': accounts
        }
        return render(request, 'administrations/admin-accounts.html', context)


class AccountDeleteAdminView(UserCheckingView, View):
    def get(self, request):
        account_id = request.GET.get('account_id', None)
        if account_id is not None:
            user = CustomUser.objects.get(id=account_id)
            if not user.is_active:
                user.is_active = True
            else:
                user.is_active = False
            user.save()
            data = {
                'is_changed': True,
                'is_active': user.is_active
            }
        else:
            data = {
                'is_changed': False
            }
        return JsonResponse(data)


class BrandsAdminView(UserCheckingView, View):
    def get(self,  request):
        form = BrandCreationForm()
        context = {
            'url_name': 'brands',
            'form': form
        }
        return render(request, 'administrations/admin-brands.html', context)

    def post(self, request):
        form = BrandCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('administrations:admin-brands')
        else:
            raise Http404()


class  BrandDeleteAdminView(UserCheckingView, View):
    def get(self, request):
        brand_id = request.GET.get('brand_id', None)
        if brand_id is not None:
            brand_obj = Brand.objects.get(id=brand_id)
            if brand_obj.phone_set.all():
                data = {
                    'is_deleted': False,
                    'message': 'There are products of this brand. Delete them first!'
                }
            else:
                Brand.objects.get(id=brand_id).delete()
                data = {
                    'is_deleted': True
                }
        else:
            data = {
                'is_deleted': False
            }
        return JsonResponse(data)


class CartsAdminView(UserCheckingView, View):
    def get(self, request):
        carts = Cart.objects.all()
        context = {
            'url_name': 'carts',
            'carts': carts,
        }
        return render(request, 'administrations/admin-carts.html', context)


class CartDeleteAdminView(UserCheckingView, View):
    def get(self, request):
        cart_id = request.GET.get('cart_id', None)
        if cart_id is not None:
            Cart.objects.get(id=cart_id).delete()
            data = {
                'is_deleted': True
            }
        else:
            data = {
                'is_deleted': False
            }
        return JsonResponse(data)
