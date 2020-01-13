from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from product.models import Product
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomUserLoginForm


class CustomUserLoginView(View):

    def get(self, request):
        form = CustomUserLoginForm()
        context = {
            'form': form
        }
        return render(request, 'users/login.html', context)

    def post(self, request):
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('pages:home-page')
                else:
                    messages.error(request, 'Your account is disabled.')
                    return redirect('pages:home-page')
            else:
                messages.warning(request, 'Not existing user.')
                return redirect('users:user-login')
        else:
            messages.error(request, 'Not correct input field(s).')
            return redirect('users:user-login')


class CustomUserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('users:user-login')
