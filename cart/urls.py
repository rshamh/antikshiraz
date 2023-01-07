from django.urls import path
from .views import  index, add_to_cart, add_cart, subtract_cart, remove_cart, clear_cart

app_name = 'cart'
urlpatterns = [
    path('', index, name='index'),
    path('add_to_cart/<int:product_pk>/', add_to_cart, name='add-to-cart'),
    path('add_cart/<int:product_pk>/', add_cart, name='add-cart'),
    path('subtract_cart/<int:product_pk>/', subtract_cart, name='subtract-cart'),
    path('remove_cart/<int:product_pk>/', remove_cart, name='remove-cart'),
    path('clear_cart/', clear_cart, name='clear-cart'),
]