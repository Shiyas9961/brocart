from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_page, name = 'cart'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('remove_item/<id>', views.remove_from_cart, name='remove_item'),
    path('checkout', views.checkout_order, name="checkout"),
    path('orders', views.view_orders, name='orders')
]
