from django.urls import path
from . import views


urlpatterns = [
    path("add/order/<int:id>", views.add_order, name='add_order'),
    path("cart", views.cart, name='cart'),
]