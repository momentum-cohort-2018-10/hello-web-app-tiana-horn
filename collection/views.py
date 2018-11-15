from django.shortcuts import render
from collection.models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {
        'products': products,
    })

def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'products/product_detail.html', {
        'product' : product,
    })

