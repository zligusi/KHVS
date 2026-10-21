from django.shortcuts import render ,get_object_or_404
from itertools import zip_longest
from .models import Device, Liquid, Carttridge, ProductImage

def home (request):
    Device.objects.all()
    Liquid.objects.all()
    Carttridge.objects.all()
    products = []


    for device, liquid, carttridge in zip_longest(device, liquid, carttridge):
        if device and device.stock > 0 :
            device.category = 'device'
            products.append(device)
        if liquid and liquid.stock > 0 :
            liquid.category = 'liquid'
            products.append(liquid)
        if carttridge and carttridge.stock > 0 :
            carttridge.category = 'carttridge'
            products.append(carttridge)

    top_devices = Device.objects.filter(top_product=True)[:5],
    top_liquids = Liquid.objects.filter(top_product=True)[:3],
    top_carttridges = Carttridge.objects.filter(top_product=True)[:2],

    for d in top_devices:
        d.category = 'device'
    for l in top_liquids:
        l.category = 'liquid'
    for c in top_carttridges:
        c.carttridge = 'carttridge'

    top_products = list(top_devices) + list(top_liquids) + list(top_carttridges)

    
    return render(request, 'main/home.html', {'products': products,
                                              'top_products': top_products})


def product_detail (request, category, slug):
    if category == 'device':
        product = get_object_or_404(Device, slug=slug)
    elif category == 'liquid' :
        product = get_object_or_404(Liquid, slug=slug)
    elif category == 'carttridge' :
        product = get_object_or_404(Carttridge, slug=slug)

    images = ProductImage.objects.filter(product=product)
    return render(request, 'main/product_detail.html', {'product': product, 'images': images, 'category': category})
# добавить список похожих товарів


def about (request):
    return render(request, 'main/about.html')

