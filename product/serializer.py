from rest_framework import serializers
from decimal import Decimal
from product.models import Product, Category, Review


class Category_Serializer( serializers.ModelSerializer ):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'product_count']

    product_count = serializers.IntegerField(
        read_only=True, 
        help_text="Return the number product in this category"
    )


class Product_Serializer( serializers.ModelSerializer ):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'stock', 'price', 'product_with_tax', 'category']

    product_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self, product):
        return round(product.price * Decimal(1.1), 2)
    
    # Field Level Validation
    def validate_price(self, price):
        if price < 0:
            return serializers.ValidationError('Price can\'t be negative')
        
        return price


class Review_Serializer( serializers.ModelSerializer ):
    class Meta:
        model = Review
        fields = ['id', 'user_name', 'description']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id = product_id, **validated_data)