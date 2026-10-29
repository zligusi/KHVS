from django.shortcuts import render ,get_object_or_404, redirect
from itertools import zip_longest
from .models import Product, ProductImage
from .models import Category
from .forms import DeviceForm, LiquidForm, CartridgeForm
from django.http import Http404

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


def category_select(request):
    return render(request, 'main/create/category_select.html')


def create_product (request, category_slug):
    FORMS_MAP = {
        'device': DeviceForm,
        'liquid': LiquidForm,
        'cartridge': CartridgeForm,
    }

    form_class = FORMS_MAP.get(category_slug)
    if form_class is None :
        raise Http404 
    if request.method == "POST":
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.category = get_object_or_404(Category, name__iexact=category_slug)
            product.save()
            if request.POST.get('action') == 'save_add':
                return redirect('category_select')
            return redirect('home')
    else:
        form = form_class()

    return render(request, 'main/create/create_product.html', {'form': form})
    


def about (request):
    return render(request, 'main/about.html')
