from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

from drf_yasg.utils import swagger_auto_schema

from product.models import Product, Category, Review, Product_Images
from product.filters import Product_Filter
from product.serializer import Product_Serializer, Category_Serializer, Review_Serializer, Product_Image_Serializer
from product.paginations import Default_Pagination

from api.permissions import IsAdmin_Or_ReadOnly, Custom_Django_Model_Permission
from .permissions import Is_ReviewAuthor_Or_ReadOnly

from django_filters.rest_framework import DjangoFilterBackend

from django.db.models import Count


class Product_Images_ViewSet( ModelViewSet ):
    serializer_class = Product_Image_Serializer
    permission_classes = [IsAdmin_Or_ReadOnly]


    def get_queryset(self):
        return Product_Images.objects.filter(product_id=self.kwargs.get('product_pk'))
    
    def perform_create(self, serializer):
        serializer.save(product_id=self.kwargs.get('product_pk'))


class Product_View_Set( ModelViewSet ):
    """
    API endpoint for managing products in the e-commerce store
     - Allows authenticated admin to create, update, and delete products
     - Allows user to browse and filter product
     - Support searching by name, description, and category 
     - Support ordering by price and updated_at
    """

    queryset = Product.objects.all()
    serializer_class = Product_Serializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = Product_Filter
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'stock', 'updated_at']
    pagination_class = Default_Pagination
    permission_classes = [IsAdmin_Or_ReadOnly]

    def list(self, request, *args, **kwargs):
        """
        Retrieve all Products
        """
        return super().list(request, *args, **kwargs)
    

    @swagger_auto_schema(
        operation_summary="Creating a Product",     # With End-Point
        operation_description="Only Authenticated Admin can create a product",      # Inside End-Point
        request_body=Product_Serializer,
        responses={
            201:Product_Serializer,
            400: 'Bad Request'
        }
    )
    def create(self, request, *args, **kwargs):
        """
        Crating a Product                           #   -> operation_description
         - Only admin can create product            #      override this thing 
        """
        return super().create(request, *args, **kwargs)


    # def destroy(self, request, *args, **kwargs):
    #     product = self.get_object()
    #     if product.stock > 0:
    #         return Response({'message': 'You can\'t delete an available product'})  
        
    #     self.perform_destroy(product)
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class Category_View_Set( ModelViewSet ):
    queryset = Category.objects.annotate(product_count=Count('products'))
    serializer_class = Category_Serializer
    permission_classes = [IsAdmin_Or_ReadOnly]


class Review_View_Set( ModelViewSet ):
    serializer_class = Review_Serializer
    permission_classes = [Is_ReviewAuthor_Or_ReadOnly]

    def get_queryset(self):
        return Review.objects.filter(product_id = self.kwargs.get('product_pk'))
    

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        

    def get_serializer_context(self):
        return {'product_id': self.kwargs.get('product_pk')}