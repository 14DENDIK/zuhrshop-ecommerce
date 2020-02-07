from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from .models import Product, Phone


class ProductDetailView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if product.is_on_sale:
            off_percent = 100 * (1 - product.on_sale_price / product.price)
            off_percent = round(off_percent, 1)
            saved_money = product.price - product.on_sale_price
            context = {
                'product': product,
                'off_percent': off_percent,
                'saved_money': saved_money
            }
        else:
            context = {
                'product': product
            }
        return render(request, 'product/product-detail.html', context)


class PhonesListView(View):
    def get(self, request, brand, cond):
        products = Phone.objects.all()
        context = {
            'products': products,
            'current_brand': brand,
            'cond': cond,
        }
        return render(request, 'product/phones-list.html', context)
