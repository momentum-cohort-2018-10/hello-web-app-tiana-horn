from django.forms import ModelForm
from collection.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price',)
        
