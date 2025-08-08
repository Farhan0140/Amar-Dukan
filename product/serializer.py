from rest_framework import serializers
from decimal import Decimal
from product.models import Category


class Category_Serializer( serializers.Serializer ):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()

class Product_Serializers( serializers.Serializer ):
    id = serializers.IntegerField()
    name = serializers.CharField()
    stock = serializers.IntegerField()
    description = serializers.CharField()
    # price = serializers.DecimalField(max_digits=10, decimal_places=2)
    unit_price = serializers.DecimalField(max_digits=10, decimal_places=2, source='price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    # category = serializers.PrimaryKeyRelatedField(
    #     queryset = Category.objects.all()           # It return only id
    # )

    # category = serializers.StringRelatedField()     # It return Dunder method of Category model

    # category = Category_Serializer()      # It return another dictionary of category details we add in Category_Serializer class

    category = serializers.HyperlinkedRelatedField(
        queryset = Category.objects.all(),              # It return link of category details
        view_name = 'view_specific_category'    # url name in urls.py
    )
    

    def calculate_tax(self, product):
        return round(product.price * Decimal(1.1), 2)