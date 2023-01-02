from django.shortcuts import render
from customers.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from storefront.models import Product

@login_required
def index(request):
    context ={
    }
    return render(request, 'shopadmin/index.html')


# def products(request):
#     return render(request, 'shopadmin/products.html')

class ProductListView(LoginRequiredMixin, ListView):
    queryset = Product.objects.all()
    template_name = 'shopadmin/products.html'
    # paginate_by = 8
    # context_object_name = 'product_list
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['all_products_count'] = self.queryset.count()
        context['available_products_count'] = Product.objects.filter(stock__gt = 0 ).count()

        return context



class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ["title", "slug", "category", "description", "thumbnail", "price", "publish", "amount", "status"]
    template_name = 'shopadmin/product-create-update.html'


class CustomerListView(LoginRequiredMixin, ListView):
    queryset = User.objects.all()
    template_name = 'shopadmin/customers.html'
    # paginate_by = 8
    context_object_name = 'customer_list'