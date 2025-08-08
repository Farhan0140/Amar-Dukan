from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from product.models import Product
from product.serializer import Product_Serializers


@api_view()
def products( request ):
    return Response({"messages": "Rest Api"})

@api_view()
def categories( request ):
    return Response({"Messages": "Categories API"})


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
def view_specific_product( request, id ):
    product = get_object_or_404( Product, pk = id )
    # product_dict = {
    #     'id': product.id,
    #     'name': product.name,
    #     'price': product.price,
    #     'stock': product.stock,
    #     'description': product.description,
    # }

    serializer = Product_Serializers(product)

    return Response( serializer.data )