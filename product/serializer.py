from rest_framework import serializers
from decimal import Decimal

class Product_Serializers( serializers.Serializer ):
    id = serializers.IntegerField()
    name = serializers.CharField()
    stock = serializers.IntegerField()
    description = serializers.CharField()
    # price = serializers.DecimalField(max_digits=10, decimal_places=2)
    unit_price = serializers.DecimalField(max_digits=10, decimal_places=2, source='price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self, product):
        return round(product.price * Decimal(1.1), 2)