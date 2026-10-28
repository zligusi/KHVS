from django.shortcuts import render ,get_object_or_404
from itertools import zip_longest
from .models import Product, ProductImage

def get_top_products(limit_d, limit_l, limit_c):
    devices = Product.objects.filter(top_product=True,
                                     category__name='Device'
                                     )[:limit_d]
    liquids = Product.objects.filter(top_product=True,
                                     category__name='Liquid'
                                     )[:limit_l]
    cartridges = Product.objects.filter(top_product=True,
                                        category__name='Cartridge'
                                        )[:limit_c]

    return list(devices) + list(liquids) + list(cartridges)


def get_similar_product(product, limit):
    return(Product.objects.filter(category=product.category,
                                  ).exclude(pk=product.pk).order_by('?')[:limit])


def home (request):
    product = Product.objects.all()

    top_product = get_top_products(limit_d=5, limit_l=3, limit_c=2)
    
    return render(request, 'main/home.html', {'products': product,
                                              'top_products': top_product})


def product_detail (request, slug):
    product = get_object_or_404(Product, slug=slug)
    top_products = get_top_products(limit_d=3, limit_l=1, limit_c=1)
    releted = get_similar_product(product, limit=5)

    return render(request, 'main/product_detail.html', {'top_products': top_products,
                                                        'product': product,
                                                        'releted': releted})



def about (request):
    return render(request, 'main/about.html')
