from django.urls import path

from . import views

app_name = 'administrations'
#
urlpatterns = [
    path('', views.MainAdminView.as_view(), name='admin-main'),
    path('products/', views.ProductAdminView.as_view(), name='admin-products'),
    path('accounts/', views.AccountsAdminView.as_view(), name='admin-accounts')
]
