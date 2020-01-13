from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.CartView.as_view(), name='cart'),
    path('ajax/add-cart-item/', views.AddCartItemView.as_view(), name='add-cart-item'),
    path('ajax/delete-cart-item/', views.DeleteCartItemView.as_view(), name='delete-cart-item'),
    path('ajax/update-cart-item-quantity/', views.UpdateCartItemQuantityView.as_view(), name='update-cart-item-quantity'),
]
