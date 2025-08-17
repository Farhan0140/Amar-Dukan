
from rest_framework import serializers

from order.models import Cart, Cart_Item, Order, OrderItem
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
    
class Update_CartItem_Serializer( serializers.ModelSerializer ):
    class Meta:
        model = Cart_Item
        fields = ['quantity']
    

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
        read_only_fields = ['user']


    def get_total_price(self, cart:Cart):
        return sum([ item.quantity * item.product.price for item in cart.items.all()])
    

# Order  ----

class Create_Order_Serializer( serializers.Serializer ):
    cart_id = serializers.UUIDField()

    def validate_cart_id(self, cart_id):
        if not Cart.objects.filter(pk=cart_id).exists():
            raise serializers.ValidationError('Cart Not Found')
        
        if not Cart_Item.objects.filter(cart_id=cart_id).exists():
            raise serializers.ValidationError('Cart Is Empty')

class OrderItems_Serializer( serializers.ModelSerializer ):
    product = Simplified_Product_Serializer()

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'price', 'total_price']



class Order_Serializer( serializers.ModelSerializer ):
    items = OrderItems_Serializer(many=True)
    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'total_price', 'created_at', 'items']