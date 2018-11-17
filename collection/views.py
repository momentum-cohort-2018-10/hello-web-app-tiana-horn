from django.shortcuts import render, redirect
from collection.forms import ProductForm
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

def edit_product(request, slug):
    product = Product.objects.get(slug=slug)
    form_class = ProductForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', slug=product.slug)
    else:
        form = form_class(instance=product)
    return render(request, 'products/edit_product.html', {
        'product': product,
        'form': form,
    })
