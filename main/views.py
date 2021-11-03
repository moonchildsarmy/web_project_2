from django.shortcuts import render
from .models import Slaider, Review
from cart.forms import CartAddProductForm
from shop.models import Product


def home(request):
    slaider = Slaider.objects.all()
    review = Review.objects.all()
    cart_product_form = CartAddProductForm
    last = Product.objects.all().order_by('-id')[:6]
    return render(request, 'main/index.html', {
        'slaider': slaider,
        'review': review,
        'last': last,
        'cart_product_form': cart_product_form,
    })


# Create your views here.
