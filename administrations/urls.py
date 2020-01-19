from django.urls import path

from . import views

app_name = 'administrations'
#
urlpatterns = [
    path('', views.MainAdminView.as_view(), name='admin-main-view'),
]
