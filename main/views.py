from django.shortcuts import render ,get_object_or_404
from itertools import zip_longest
from .models import Product, ProductImage

def get_top_products() :
    top_product = Product.objects.filter(top_product=True)[:10]
    for item in top_product :
        if item.category == 'Device':
            product_type = 'Device'
        elif item.category == 'Liquid':
            product_type = 'Liquid'
        elif item.category == 'Cartridge':
            product_type = 'Cartridge'

def home (request):
    product = Product.objects.all()

    top_product = get_top_products()
    
    return render(request, 'main/home.html', {'product': product,
                                              'top_product': top_product})

def product_detail (request, slug):
    product = Product.objects.filter(slug=slug)
    top_products = get_top_products()

    return render(request, 'main/product_detail.html', {'top_product': top_products,
                                                        'product': product})



def about (request):
    return render(request, 'main/about.html')
