from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from .models import Category, Color, Size, Product
from django.db.models import Q
from django.core.paginator import Paginator
from cart.forms import CartAddProductForm
from django.core.exceptions import ObjectDoesNotExist


def product(request):
    category = Category.objects.all()
    color = Color.objects.all()
    size = Size.objects.all()
    cart_product_form = CartAddProductForm
    item = Product.objects.all()
    paginator = Paginator(item, per_page=9)

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'shop/shop.html', {
        'item': page_obj.object_list,
        'paginator': paginator,
        'page_obj': page_obj,
        'page_number': int(page_number),
        'category': category,
        'color': color,
        'size': size,
        'cart_product_form': cart_product_form,
    })


def category(request, id):
    color = Color.objects.all()
    size = Size.objects.all()
    category = Category.objects.all()
    ctg = Category.objects.get(id=id)
    queryset = Product.objects.filter(category=ctg)

    if queryset:
        c = {
            'item': queryset,
            'category': category,
            'color': color,
            'size': size
        }

        return render(request, 'shop/shop.html', c)
    else:
        return render(request, 'shop/shop.html')


def color_filter(request, id):
    category = Category.objects.all()
    size = Size.objects.all()
    color = Color.objects.all()
    clr = Color.objects.get(id=id)
    queryset = Product.objects.filter(color=clr)

    if queryset:
        b = {
            'item': queryset,
            'color': color,
            'category': category,
            'size': size,
        }
        return render(request, 'shop/shop.html', b)
    else:
        return HttpResponseNotFound("<h2>Not found</h2>")


def size_filter(request, id):
    category = Category.objects.all()
    color = Color.objects.all()
    size = Size.objects.all()
    proportions = Size.objects.get(id=id)
    queryset = Product.objects.filter(size=proportions)

    if queryset:
        s = {
            'item': queryset,
            'size': size,
            'color': color,
            'category': category,
        }
        return render(request, 'shop/shop.html', s)
    else:
        return HttpResponseNotFound("<h2>Not found</h2>")


def product_detail(request, id):
    detail = Product.objects.get(id=id)
    cart_product_form = CartAddProductForm

    return render(request, 'shop/product-details.html', {
        'detail': detail,
        'cart_product_form': cart_product_form,
    })




# def product_filter(request):
#     category = Category.objects.all()
#     color = Color.objects.all()
#     size = Size.objects.all()
#     item = Product.objects.filter(price__range=(10,100))
#     paginator = Paginator(item, per_page=9)
#
#     page_number = request.GET.get('page', 1)
#     page_obj = paginator.get_page(page_number)
#
#     return render(request, 'shop/shop.html', {
#         'item': page_obj.object_list,
#         'paginator': paginator,
#         'page_obj': page_obj,
#         'page_number': int(page_number),
#         'category': category,
#         'color': color,
#         'size': size,
#     })


def price_filter(request):
    category = Category.objects.all()
    color = Color.objects.all()
    size = Size.objects.all()
    search_query = request.GET.get('search', '')

    if search_query:
        p = Product.objects.filter(Q(price__icontains=search_query))
    else:
        p = Product.abjects.all()

    return render(request, "shop/shop.html", {
        'item': p,
        'size': size,
        'color': color,
        'category': category,
    })


# def add_product(request, id):
#     try:
#         product = Product.objects.get(id=id)
#         product.save()
#         response = redirect('product')
#         response.set_cookie(id, "order")
#         return response
#     except ObjectDoesNotExist:
#         raise HttpResponseNotFound("<h2>Not found</h2>")
#     return redirect('product')
# # Create your views here.
