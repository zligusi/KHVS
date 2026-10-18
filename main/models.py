from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().self(*args, **kwargs)
        
        
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,
                                related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    main_image = models.ImageField(upload_to='products/main/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stock = models.PositiveIntegerField(default=0)
    top_product = models.BooleanField(default=False)
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().self(*args, **kwargs)
            
            
    def __str__(self):
        return self.name
    
    
class Device(Product):
    color = models.CharField(max_length=100)
    power = models.IntegerField()
    battery_capacity = models.IntegerField()
    guarantee = models.DecimalField(max_digits=3, decimal_places=1)
        
        
class Liquid(Product):
    volume = models.IntegerField()
    taste = models.CharField(max_length=100)
    nicotine_capacity = models.IntegerField()


class Carttridge(Product):
    volume = models.DecimalField(max_digits=3, decimal_places=1)
    resistance = models.DecimalField(max_digits=2, decimal_places=1)
    compatibility = models.CharField(max_length=120)
    
    
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='images')
    image = models.ImageField(upload_to='products/extra/')
    