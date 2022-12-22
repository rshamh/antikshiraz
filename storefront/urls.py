from django.urls import path
from .views import  index, ProductDetailView, ProductListView, CategoryListView
app_name = 'storefront'
urlpatterns = [
    path('', index, name='index'),
    path('product/<slug:slug>', ProductDetailView.as_view(), name='product-detail'),
    path('products', ProductListView.as_view(), name='all-products'),
    path('category/<slug:slug>', CategoryListView.as_view(), name='category')
]