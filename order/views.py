from django.shortcuts import render

from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin

from order.models import Cart, Cart_Item
from order.serializers import Cart_Serializer, CartItems_Serializer, Add_Cart_Item_Serializer, Update_CartItem_Serializer


class Cart_View_Set( CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet ):
    queryset = Cart.objects.all()
    serializer_class = Cart_Serializer


class Cart_Items_View_Set( ModelViewSet ):
    http_method_names = ['get', 'post', 'patch', 'delete']
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return Add_Cart_Item_Serializer
        if self.request.method == 'PATCH':
            return Update_CartItem_Serializer
        
        return CartItems_Serializer

    def get_queryset(self):
        return Cart_Item.objects.filter(cart_id=self.kwargs['cart_pk'])
    
    def get_serializer_context(self):
        return {'cart_pk': self.kwargs['cart_pk']}