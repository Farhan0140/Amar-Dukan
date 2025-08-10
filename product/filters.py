
from django_filters.rest_framework import FilterSet
from product.models import Product


class Product_Filter( FilterSet ):
    class Meta:
        model = Product
        fields = {
            'category_id': ['exact'],
            'price': ['gt', 'lt'],
        }

