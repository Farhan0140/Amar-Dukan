from django.contrib import admin
from product.models import Product, Category, Product_Images

# Register your models here.
admin.site.register(Product)
admin.site.register(Product_Images)
admin.site.register(Category)