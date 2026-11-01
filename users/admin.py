from django.contrib import admin
from .models import CustomUser, CustomUserManager

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'date_of_birth', 'city',
                    'postal_code', 'address_1', 'address_2', 'is_staff', 'is_superuser']
    list_editable = ['is_staff', 'is_superuser']
    list_filter = ['is_staff', 'is_superuser']
    search_fields = ['email', 'first_name', 'last_name']
    
