from . import views
from django.urls import path 



urlpatterns = [
   path('', views.home, name="home"),
   path('product/<slug:slug>/', views.product_detail, name='product_detail' ),
   path('about/', views.about, name='about'),
]
