from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from Extensions.utils import persian_number_conv
from django.views.generic import ListView, DetailView

def index(request):
    last_products = Product.objects.filter(status=True)[:8]
    context = {
        'last_products': last_products,
    }
    return render(request, 'storefront/index.html', context)



# def product_detail(request, slug):
#     product = get_object_or_404(Product, slug=slug)
#     context = {
#         'product': product,
#     }
#     return render(request, 'storefront/product_detail.html', context)


class ProductDetailView(DetailView):
    context_object_name = 'product' # Default name

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Product.objects.filter(status=True),  slug=slug)           #TODO Should I add status=True ?


# def products(request):
#     products_list = Product.objects.filter(status=True)
#     paginator = Paginator(products_list, 8)
#     page_number = request.GET.get('page')
#     products = paginator.get_page(page_number)
#     context = {
#         'products': products
#     }
#     return render(request, 'storefront/all_products.html', context )

class ProductListView(ListView):
    queryset = Product.objects.filter(status=True)
    template_name = 'storefront/all_products.html'
    paginate_by = 8
    # context_object_name = 'product_list


# def category(request, slug):
#     category = get_object_or_404(Category, slug=slug, status=True)
#     products_list = category.products.all()     #TODO filter it by status=True
#     paginator = Paginator(products_list, 8)
#     page_number = request.GET.get('page')
#     products = paginator.get_page(page_number)
#     context = {
#         'products': products,
#         'category': category,
#     }
#     return render(request, 'storefront/category.html', context)


class CategoryListView(ListView):
    # context_object_name = 'product_list' # Default name
    template_name = 'storefront/category.html'
    paginate_by = 8

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.filter(status=True),  slug=slug)
        return category.products.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context
    