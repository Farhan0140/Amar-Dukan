
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
    
    
class Add_Cart_Item_Serializer( serializers.ModelSerializer ):
    product_id = serializers.IntegerField()

    class Meta:
        model = Cart_Item
        fields = ['id', 'product_id', 'quantity']

    
    def save(self, **kwargs):
        cart_id = self.context['cart_pk']
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']

        try:
            cart_item = Cart_Item.objects.get(cart_id = cart_id, product_id = product_id)
            cart_item.quantity += quantity
            self.instance = cart_item.save()
        except Cart_Item.DoesNotExist:
            self.instance = Cart_Item.objects.create(cart_id=cart_id, **self.validated_data)
            
        return self.instance
    

    def validate_product_id(self, value):
        if not Product.objects.filter(pk=value).exists():
            raise serializers.ValidationError(f'Product with id -> {value} does not exists')
        
        return value


class Cart_Serializer( serializers.ModelSerializer ):
    items = CartItems_Serializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(method_name='get_total_price')
    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total_price']


    def get_total_price(self, cart:Cart):
        return sum([ item.quantity * item.product.price for item in cart.items.all()])