from rest_framework import serializers
from decimal import Decimal
from product.models import Product, Category, Review, Product_Images

from django.contrib.auth import get_user_model


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
    

class Product_Image_Serializer( serializers.ModelSerializer ):
    class Meta:
        model = Product_Images
        fields = ['id', 'image']


class Simple_User_Serializer( serializers.ModelSerializer ):
    full_name = serializers.SerializerMethodField(method_name='get_full_name')

    class Meta:
        model = get_user_model()
        fields = ['id', 'full_name']

    def get_full_name(self, obj):
        return obj.get_full_name()
    

class Review_Serializer( serializers.ModelSerializer ):
    user = serializers.SerializerMethodField(method_name='get_user')

    class Meta:
        model = Review
        fields = ['id', 'user', 'product', 'comment', 'ratings', 'created_at']
        read_only_fields = ['user', 'product']

    def get_user(self, obj):
        return Simple_User_Serializer(obj.user).data

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id = product_id, **validated_data)