from django.shortcuts import render

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin

from order.models import Cart, Cart_Item
from order.serializers import Cart_Serializer


class Cart_View_Set( CreateModelMixin, RetrieveModelMixin, GenericViewSet ):
    queryset = Cart.objects.all()
    serializer_class = Cart_Serializer