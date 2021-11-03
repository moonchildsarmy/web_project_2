from datetime import datetime, timedelta

from django.shortcuts import render, redirect
from django.http import HttpResponse
import json

from shop.models import Product


def cart(request):
    session_product = []
    products = []
    product_ids = []
    if "product" in request.session:
        session_product = request.session["product"]
    for item in session_product:
        product_ids.append(item['product_id'],)
    if session_product:
        products = Product.objects.filter(id__in=product_ids)
    return render(request, 'checkout1/cart.html', {'products': products})


def add_order(request, id):
    product_json = []
    if "product" in request.session:
        product_json = request.session["product"]
    product_json.append({'product_id': id, 'qty': 1})
    request.sessions['product'] = product_json
    request.sessions.modified = True
    return redirect('cart')
