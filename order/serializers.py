
from rest_framework import serializers

from order.models import Cart, Cart_Item
from product.models import Product



class Simplified_Product_Serializer( serializers.ModelSerializer ):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']


class CartItems_Serializer( serializers.ModelSerializer ):
    product = Simplified_Product_Serializer()
    total_price = serializers.SerializerMethodField(method_name='get_total_price')
    class Meta:
        model = Cart_Item
        fields = ['id', 'quantity', 'total_price', 'product']

        
    def get_total_price(self, cart_item: Cart_Item):
        return cart_item.quantity * cart_item.product.price


class Cart_Serializer( serializers.ModelSerializer ):
    items = CartItems_Serializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(method_name='get_total_price')
    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total_price']


    def get_total_price(self, cart:Cart):
        return sum([ item.quantity * item.product.price for item in cart.items.all()])