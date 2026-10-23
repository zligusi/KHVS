from django.contrib import admin
from .models import Category , Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category', 'price', 'description', 
                    'create_at', 'update_at', 'stock',
                    'color', 'power', 'battery_capacity', 'guarantee', 'top_product' 
                    'volume_liquid', 'taste', 'nicotine_capacity', 'top_product'
                    'volume_cartridge', 'resistance', 'compatibility', 'top_product')
    list_filter = ('category', 'create_at', 'power')
    list_editable = ('price', 'stock', 'top_product')
    search_fields = ('name', 'description', 'color', 'taste')
    prepopulated_fields = {'slug': ('name',)}
