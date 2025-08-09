from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from product.models import Product, Category
from product.serializer import Product_Serializer, Category_Serializer

from django.db.models import Count


class Product_View_Set( ModelViewSet ):
    queryset = Product.objects.all()
    serializer_class = Product_Serializer

    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        if product.stock > 0:
            return Response({'message': 'You can\'t delete an available product'})  
        
        self.perform_destroy(product)
        return Response(status=status.HTTP_204_NO_CONTENT)

# class Product_List( ListCreateAPIView ):
#     queryset = Product.objects.select_related('category').all()
#     serializer_class = Product_Serializer
    
#     def get_serializer_context(self):
#         return {'request': self.request}
    

# class Product_Details( RetrieveUpdateDestroyAPIView ):
#     queryset = Product.objects.all()
#     serializer_class = Product_Serializer

#     def delete(self, request, pk):
#         product = get_object_or_404(Product, pk=pk)
#         if product.stock > 0:
#             return Response({'message': 'You can\'t delete an available product'})  
        
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class Category_View_Set( ModelViewSet ):
    queryset = Category.objects.annotate(product_count=Count('products'))
    serializer_class = Category_Serializer


# class Category_List( ListCreateAPIView ):
#     queryset = Category.objects.annotate(product_count=Count('products'))
#     serializer_class = Category_Serializer
    

# class Category_Details( RetrieveUpdateDestroyAPIView ):
#     queryset = Category.objects.annotate(product_count=Count('products'))
#     serializer_class = Category_Serializer
