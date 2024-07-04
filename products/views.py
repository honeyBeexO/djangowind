from django.shortcuts import render

# Create your views here.
from django.views import generic 
from products.models import Product

class ProductsListView(generic.ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        return Product.objects.filter(is_active=True)
    