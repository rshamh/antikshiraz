from django.urls import path
from .views import index, ProductListView, ProductCreateView, ProductUpdateView, CustomerListView, search
app_name = 'shopadmin'
urlpatterns = [
    path('', index, name='index'),
    path('products/', ProductListView.as_view(), name='products'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/update/<str:slug>', ProductUpdateView.as_view(), name='product-update'),
    path('accounts/', CustomerListView.as_view(), name='accounts'),
    path('search/', search, name='search'),
]