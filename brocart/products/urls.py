from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('products', views.products, name = 'products'),
    path('products/<id>', views.single_product, name = 'single_product')
]