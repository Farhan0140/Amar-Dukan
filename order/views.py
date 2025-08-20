from django.shortcuts import render

from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from order.models import Cart, Cart_Item, Order, OrderItem
from order.serializers import Cart_Serializer, CartItems_Serializer, Add_Cart_Item_Serializer, Update_CartItem_Serializer, Order_Serializer, Create_Order_Serializer, Update_Order_Serializer


class Cart_View_Set( CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet ):
    serializer_class = Cart_Serializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


class Cart_Items_View_Set( ModelViewSet ):
    http_method_names = ['get', 'post', 'patch', 'delete']
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return Add_Cart_Item_Serializer
        if self.request.method == 'PATCH':
            return Update_CartItem_Serializer
        
        return CartItems_Serializer

    def get_queryset(self):
        return Cart_Item.objects.select_related('product').filter(cart_id=self.kwargs['cart_pk'])
    
    def get_serializer_context(self):
        return {'cart_pk': self.kwargs['cart_pk']}
    

# Order  ---

class Order_View_Set( ModelViewSet ):
    # permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'POST':
            return Create_Order_Serializer
        if self.request.method == 'PATCH':
            return Update_Order_Serializer

        return Order_Serializer
    
    def get_serializer_context(self):
        return {
            'user_id': self.request.user.id,
            'user': self.request.user,
        }
    

    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.prefetch_related('items__product').all()
        
        return Order.objects.prefetch_related('items__product').filter(user=self.request.user)
