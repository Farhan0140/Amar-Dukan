from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from product.models import Product, Category
from product.serializer import Product_Serializers, Category_Serializer


@api_view()
def view_products( request ):
    products = Product.objects.select_related('category').all()
    serializer = Product_Serializers( products, many=True, context={'request': request} )
    return Response(serializer.data)


# @api_view()
# def view_specific_product( request, id ):
#     try:
#         product = Product.objects.get(pk = id)
#         product_dict = {
#             'id': product.id,
#             'name': product.name,
#             'price': product.price,
#             'stock': product.stock,
#             'description': product.description,
#         }
#     except Product.DoesNotExist:
#         return Response(
#             {'message': 'Product Does Not Exist'},
#             # status = 404,     # not recommended
#             status = status.HTTP_404_NOT_FOUND,
#         )

#     return Response( product_dict )

# ---------> Simple Version

@api_view()
def view_specific_product( request, pk ):
    product = get_object_or_404( Product, pk = pk )
    # product_dict = {
    #     'id': product.id,
    #     'name': product.name,
    #     'price': product.price,
    #     'stock': product.stock,
    #     'description': product.description,
    # }

    serializer = Product_Serializers( product, context={'request': request} )

    return Response( serializer.data )


@api_view()
def view_categories( request ):
    categories = Category.objects.all()
    serializer = Category_Serializer( categories, many=True )

    return Response( serializer.data )


@api_view()
def view_specific_category( request, pk ):
    category = get_object_or_404( Category, pk = pk )
    serializer = Category_Serializer( category )

    return Response( serializer.data )