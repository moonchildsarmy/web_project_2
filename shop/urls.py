from django.urls import path
from . import views


urlpatterns = [
    path("product/", views.product, name='product'),
    path("category/<int:id>", views.category, name='category'),
    path("color/<int:id>", views.color_filter, name='color_filter'),
    path("size/<int:id>", views.size_filter, name='size_filter'),
    path("product_detail/<int:id>", views.product_detail, name='product_detail'),
    path("search_price/", views.price_filter, name='price_filter'),
]