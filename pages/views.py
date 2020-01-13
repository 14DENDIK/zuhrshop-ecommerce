from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.translation import gettext as _

from product.models import Product
from cart.models import Cart


class HomeView(View):
    def get(self, request):
        # from django.utils import translation
        # user_language = 'ru'
        # translation.activate(user_language)
        # request.session[translation.LANGUAGE_SESSION_KEY] = user_language
        # if request.user.is_authenticated():
        #     cart = Cart.objects.get(user=request.user)
        # print(request.session.get('first_name', 'Unknown'))
        products = Product.objects.all()
        context = {
            'products': products
        }
        return render(request, 'pages/home.html', context)
