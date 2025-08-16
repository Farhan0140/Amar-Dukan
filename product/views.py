from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

from product.models import Product, Category, Review
from product.filters import Product_Filter
from product.serializer import Product_Serializer, Category_Serializer, Review_Serializer
from product.paginations import Default_Pagination

from api.permissions import IsAdmin_Or_ReadOnly, Custom_Django_Model_Permission
from .permissions import Is_ReviewAuthor_Or_ReadOnly

from django_filters.rest_framework import DjangoFilterBackend

from django.db.models import Count


class Product_View_Set( ModelViewSet ):
    queryset = Product.objects.all()
    serializer_class = Product_Serializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = Product_Filter
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'stock', 'updated_at']
    pagination_class = Default_Pagination
    permission_classes = [IsAdmin_Or_ReadOnly]


    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        if product.stock > 0:
            return Response({'message': 'You can\'t delete an available product'})  
        
        self.perform_destroy(product)
        return Response(status=status.HTTP_204_NO_CONTENT)


class Category_View_Set( ModelViewSet ):
    queryset = Category.objects.annotate(product_count=Count('products'))
    serializer_class = Category_Serializer
    permission_classes = [IsAdmin_Or_ReadOnly]


class Review_View_Set( ModelViewSet ):
    serializer_class = Review_Serializer
    permission_classes = [Is_ReviewAuthor_Or_ReadOnly]

    def get_queryset(self):
        return Review.objects.filter(product_id = self.kwargs['product_pk'])
    

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}