from django.db import models 
from django.utils.html import strip_tags
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    pass


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=120, unique=True)
    phone = models.CharField(max_length=13, unique=True)
    first_name = models.CharField(max_length=25, db_index=True)
    last_name = models.CharField(max_length=25, db_index=True)
    city = models.CharField(max_length=100, blank=True)
    postal_code = models.IntegerField(max_length=5, blank=True, null=True)
    address_1 = models.CharField(max_length=200, blank=True)
    address_2 = models.CharField(max_length=200, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def clean(self):
        for field in ['email', 'phone', 'first_name', 'last_name', 'city',
                     'postall_code', 'address_1', 'address_2']:
            value = getattr(self, field)
            if value :
                setattr(self, field, strip_tags(value))

