from rest_framework import serializers
from decimal import Decimal
from product.models import Product, Category


class Category_Serializer( serializers.ModelSerializer ):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'product_count']

    product_count = serializers.SerializerMethodField(method_name='get_product_count')

    def get_product_count(self, obj):
        return obj.products.count()                                                # We need to solve this from views.py 


class Product_Serializer( serializers.ModelSerializer ):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'stock', 'price', 'product_with_tax', 'category']

    product_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    category = serializers.HyperlinkedRelatedField(
        queryset = Category.objects.all(),              # It return link of category details
        view_name = 'view_specific_category'    # url name in urls.py
    )

    def calculate_tax(self, product):
        return round(product.price * Decimal(1.1), 2)
    
    # Field Level Validation
    def validate_price(self, price):
        if price < 0:
            return serializers.ValidationError('Price can\'t be negative')
        
        return price
