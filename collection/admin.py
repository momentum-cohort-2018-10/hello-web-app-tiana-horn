from django.contrib import admin
from collection.models import Product
# set up automated slug creation
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'description', 'price', )
    prepopulated_fields = {'slug': ('name',)}

# and register it
admin.site.register(Product, ProductAdmin)
