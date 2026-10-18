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
        

    
    return render(request, 'main/home.html', {'products': products})
    



