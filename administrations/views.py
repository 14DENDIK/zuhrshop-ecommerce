from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.backends import BaseBackend

from users.models import CustomUser
from product.models import Product, ProductImage
from product.forms import PhoneCreationForm, ProductImageFormset


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


class ProductAdminView(UserCheckingView, View):

    def get(self, request):
        form = PhoneCreationForm()
        formset = ProductImageFormset(queryset=ProductImage.objects.none())
        products = Product.objects.all()
        context = {
            'products': products,
            'url_name': 'products',
            'form': form,
            'formset': formset
        }
        return render(request, 'administrations/admin-product.html', context)


    def post(self, request):
        form = PhoneCreationForm(request.POST or None, request.FILES or None)
        formset = ProductImageFormset(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            product = form.save()
            for f in formset:
                try:
                    image = ProductImage(product=product, image=f.cleaned_data['image'])
                    image.save()
                except Exception:
                    raise Exception('Something but wrong')

            return redirect('administrations:admin-products')


class AccountsAdminView(UserCheckingView, View):

    def get(self, request):
        clients = CustomUser.objects.filter(is_staff=False)
        employees = CustomUser.objects.filter(is_staff=True)
        context = {
            'url_name': 'accounts',
            'clients': clients,
            'employees': employees
        }
        return render(request, 'administrations/admin-accounts.html', context)
