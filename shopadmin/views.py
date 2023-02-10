from django.shortcuts import render
from accounts.models import User
from django.http import Http404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.mixins import SuperUserRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView
from storefront.models import Product
from django.db.models import Q

@login_required
@user_passes_test(lambda user: user.is_superuser)
def index(request):
    context ={
    }
    return render(request, 'shopadmin/index.html')


# def products(request):
#     return render(request, 'shopadmin/products.html')

class ProductListView(LoginRequiredMixin, SuperUserRequiredMixin, ListView):
        queryset = Product.objects.all()
        template_name = 'shopadmin/products.html'
        # paginate_by = 8
        # context_object_name = 'product_list
        def get_context_data(self, **kwargs):
            context =  super().get_context_data(**kwargs)
            context['all_products_count'] = self.queryset.count()
            context['available_products_count'] = Product.objects.filter(stock__gt = 0 ).count()

            return context


class ProductCreateView(LoginRequiredMixin, SuperUserRequiredMixin, CreateView):
    model = Product
    fields = ["title", "slug", "category", "description", "thumbnail", "price", "publish", "stock", "status"]
    template_name = 'shopadmin/product-create-update.html'


class ProductUpdateView(LoginRequiredMixin, SuperUserRequiredMixin, UpdateView):
    model = Product
    fields = ["title", "slug", "category", "description", "thumbnail", "price", "publish", "stock", "status"]
    template_name = 'shopadmin/product-create-update.html'


class CustomerListView(LoginRequiredMixin, SuperUserRequiredMixin, ListView):
    queryset = User.objects.all()
    template_name = 'shopadmin/customers.html'
    # paginate_by = 8
    context_object_name = 'customer_list'

def search(request):
    context={}
    if 'table_search' in request.GET:
        keyword = request.GET['table_search']
        if keyword:
            products = Product.objects.filter(Q(title__icontains=keyword) | Q(description__icontains=keyword))

            context={
                'product_list': products
            }
    return render(request, 'shopadmin/products.html', context)