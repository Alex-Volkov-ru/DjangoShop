from django.shortcuts import render

def catatlog(request):
    return render(request, 'goods/catalog.html')

def product(request):
    return render(request, 'goods/product.html')

