
from rest_framework import serializers

from order.models import Cart, Cart_Item


class Cart_Serializer( serializers.ModelSerializer ):
    class Meta:
        model = Cart
        fields = ['id', 'user']