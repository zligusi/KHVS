from . import views
from django.urls import path 



urlpatterns = [
   path('', views.home, name="home"),
   path('product/<slug:slug>/', views.product_detail, name='product_detail' ),
   path('create/category/select', views.category_select, name='category_select'),
   path('create/product/<slug:category_slug>/', views.create_product, name='create_product'),
   path('top_products/', views.favorite_products, name='favorite_products'),
   path('about/', views.about, name='about'),
]
