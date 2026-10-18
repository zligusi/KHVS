from django.contrib import admin
from .models import Category , Liquid, Carttridge, Device, ProductImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category', 'price', 'description', 
                    'main_image', 'create_at', 'update_at', 'stock',
                     'color', 'power', 'batery_capacity', 'gurantee' )
    list_filter = ('category', 'create_at')
    list_editable = ('price', 'stock', 'power')
    search_fields = ('name', 'description', 'color')
    prepopulated_fields = {'slug': ('name')}


@admin.register(Liquid)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category', 'price', 'description', 
                    'main_image', 'create_at', 'update_at', 'stock',
                    'volume', 'taste', 'nicotine_capacity')
    list_filter = ('category', 'create_at')
    list_editable = ('price', 'stock')
    search_fields = ('name', 'description', 'taste')
    prepopulated_fields = {'slug': ('name')}


@admin.register(Carttridge)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category', 'price', 'description', 
                    'main_image', 'create_at', 'update_at', 'stock',
                    'volume', 'resistance', 'compatibility')
    list_filter = ('category', 'create_at')
    list_editable = ('price', 'stock')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name')}
