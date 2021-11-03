from django.conf.urls import url
from django.urls import path
from . import views


app_name = 'order'

urlpatterns = [
    path('order_create', views.order_create, name='order_create'),
    path('checkout', views.checkout, name='checkout'),
]

