from rest_framework import serializers
from decimal import Decimal
from product.models import Product, Category


class Category_Serializer( serializers.ModelSerializer ):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'product_count']

    product_count = serializers.IntegerField()


    # 
    # product_count = serializers.SerializerMethodField(method_name='get_product_count')

    # def get_product_count(self, category):
    #     count = Product.objects.filter(category=category).count()     # This method is too time-consuming 
    #     return count                                                  # We need to solve this from views.py 


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


# class Category_Serializer( serializers.Serializer ):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     description = serializers.CharField()


# class Product_Serializer( serializers.Serializer ):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     stock = serializers.IntegerField()
#     description = serializers.CharField()
#     # price = serializers.DecimalField(max_digits=10, decimal_places=2)
#     unit_price = serializers.DecimalField(max_digits=10, decimal_places=2, source='price')
#     price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

#     # category = serializers.PrimaryKeyRelatedField(
#     #     queryset = Category.objects.all()           # It return only id
#     # )

#     # category = serializers.StringRelatedField()     # It return Dunder method of Category model

#     # category = Category_Serializer()      # It return another dictionary of category details we add in Category_Serializer class

#     category = serializers.HyperlinkedRelatedField(
#         queryset = Category.objects.all(),              # It return link of category details
#         view_name = 'view_specific_category'    # url name in urls.py
#     )
    

#     def calculate_tax(self, product):
#         return round(product.price * Decimal(1.1), 2)