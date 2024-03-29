from django.urls import path
from .views import  index, ProductDetailView, ProductListView, CategoryListView, search
app_name = 'storefront'
urlpatterns = [
    path('', index, name='index'),
    path('product/<str:slug>', ProductDetailView.as_view(), name='product-detail'),
    path('products', ProductListView.as_view(), name='all-products'),
    path('category/<str:slug>', CategoryListView.as_view(), name='category'),
    path('search', search, name='search'),

]