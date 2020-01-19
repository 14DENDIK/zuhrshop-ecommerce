from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin, PermissionRequiredMixin

class MainAdminView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'users.is_staff'

    def get(self, request):
        return render(request, 'cart/cart.html', {})
