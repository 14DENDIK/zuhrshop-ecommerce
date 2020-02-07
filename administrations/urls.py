from django.urls import path

from . import views

app_name = 'administrations'
#
urlpatterns = [
    path('', views.MainAdminView.as_view(), name='admin-main'),
    path('products/', views.ProductListAdminView.as_view(), name='admin-products'),
    path('brands/', views.BrandsAdminView.as_view(), name='admin-brands'),
    path('carts/', views.CartsAdminView.as_view(), name='admin-carts'),
    path('<str:who>/', views.AccountsAdminView.as_view(), name='admin-accounts'),
    path('products/<str:born>/', views.ProductAddAdminView.as_view(), name='admin-add-product'),
    path('ajax/product/delete/', views.ProductDeleteAdminView.as_view(), name='admin-delete-product'),
    path('ajax/account/delete/', views.AccountDeleteAdminView.as_view(), name='admin-delete-account'),
    path('ajax/cart/delete/', views.CartDeleteAdminView.as_view(), name='admin-delete-cart'),
    path('ajax/brand/delete/', views.BrandDeleteAdminView.as_view(), name='admin-delete-brand'),
]
