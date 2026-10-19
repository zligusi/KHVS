from django.shortcuts import render
from itertools import zip_longest
from .models import Device, Liquid, Carttridge

def home (request):
    Device.objects.all()
    Liquid.objects.all()
    Carttridge.objects.all()
    products = []


    for device, liquid, carttridge in zip_longest(device, liquid, carttridge):
        if device and device.stock > 0 :
            products.append(device)
        if liquid and liquid.stock > 0 :
            products.append(liquid)
        if carttridge and carttridge.stock > 0 :
            products.append(carttridge)

    top_devices = Device.objects.filter(top_product=True)[:5],
    top_liquids = Liquid.objects.filter(top_product=True)[:3],
    top_carttridges = Carttridge.objects.filter(top_product=True)[:2],

    top_products = list(top_devices) + list(top_liquids) + list(top_carttridges)

    
    return render(request, 'main/home.html', {'products': products,
                                              'top_products': top_products})
    

def about (request):
    return render(request, 'main/about.html')

