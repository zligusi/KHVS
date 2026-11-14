from .models import Product

def get_top_products(limit_d, limit_l, limit_c):
    devices = Product.objects.filter(top_product=True,
                                     category__name='Device'
                                     )[:limit_d]
    liquids = Product.objects.filter(top_product=True,
                                     category__name='Liquid'
                                     )[:limit_l]
    carttridges = Product.objects.filter(top_product=True,
                                        category__name='Carttridge'
                                        )[:limit_c]

    return list(devices) + list(liquids) + list(carttridges)

def get_similar_product(product, limit):
    return(Product.objects.filter(category=product.category,
                                  ).exclude(pk=product.pk).order_by('?')[:limit])