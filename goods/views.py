from django.shortcuts import get_list_or_404, render
from goods.models import Products


def catatlog(request, category_slug):

    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    
    context = {
        # Временно разместил не в БД
        "title": "Home - Каталог",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug=False):

    product = Products.objects.get(slug=product_slug)
    
    context = {
        'product': product
    }

    return render(request, "goods/product.html", context=context)
