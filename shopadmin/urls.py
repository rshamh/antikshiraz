from django.urls import path
from .views import index, ProductListView, ProductCreateView, CustomerListView
app_name = 'shopadmin'
urlpatterns = [
    path('', index, name='index'),
    path('products/', ProductListView.as_view(), name='products'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('customers/', CustomerListView.as_view(), name='customers'),
]