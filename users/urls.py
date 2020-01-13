from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.CustomUserLoginView.as_view(), name='user-login'),
    path('logout/', views.CustomUserLogoutView.as_view(), name='user-logout'),
]
