from django.shortcuts import render ,get_object_or_404, redirect
from itertools import zip_longest
from .models import Product, ProductImage
from .models import Category
from .forms import DeviceForm, LiquidForm, CartridgeForm
from django.http import Http404
from django.db.models import Q
from .servis import get_similar_product, get_top_products
 

def home (request):
    products = Product.objects.all()
    
    top_product = get_top_products(limit_d=5, limit_l=3, limit_c=2)

    filter_cetegory = request.GET.getlist('filter_cetegory')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    search = request.GET.get('search', '').strip()


    if filter_cetegory :
        products = products.filter(category__name__in=filter_cetegory)
    if price_min :
        products = products.filter(price__gte=price_min)
    if price_max :
        products = products.filter(price__lte=price_max)
    if search :
        for word in search.strip():
            products = products.filter(Q(description__icontains=word) | Q(name__icontains=word))
        products = products.distinct()
    
        
    return render(request, 'main/home.html', {'products': products,
                                              'top_products': top_product})


def product_detail (request, slug):
    product = get_object_or_404(Product, slug=slug)
    top_products = get_top_products(limit_d=3, limit_l=1, limit_c=1)
    releted = get_similar_product(product, limit=5)

    if product.group :
        group_products = Product.objects.filter(group=product.group, stock__gt=0)
    else:
        group_products = []

    return render(request, 'main/product_detail.html', {'top_products': top_products,
                                                        'product': product,
                                                        'releted': releted,
                                                        'group_products': group_products})


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
    

def favorite_products (request):
    top_products = Product.objects.filter(top_product=True)
    return render(request, 'main/favorite_products.html', {'top_products':top_products})


def about (request):
    return render(request, 'main/about.html')
