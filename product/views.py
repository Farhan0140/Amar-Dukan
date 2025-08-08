from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from product.models import Product, Category
from product.serializer import Product_Serializer, Category_Serializer

from django.db.models import Count


@api_view(['GET', 'POST'])
def view_products( request ):
    if request.method == 'GET':
        products = Product.objects.select_related('category').all()
        serializer = Product_Serializer( products, many=True, context={'request': request} )
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = Product_Serializer(data=request.data, context={'request': request})  # Deserializer

        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


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

    serializer = Product_Serializer( product, context={'request': request} )

    return Response( serializer.data )


@api_view(['GET', 'POST'])
def view_categories( request ):
    if request.method == 'GET':
        categories = Category.objects.annotate(product_count=Count('products'))
        serializer = Category_Serializer( categories, many=True )

        return Response( serializer.data )
    
    if request.method == 'POST':
        serializer = Category_Serializer(data=request.data)     # Deserializer
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view()
def view_specific_category( request, pk ):
    category = get_object_or_404( Category, pk = pk )
    serializer = Category_Serializer( category )

    return Response( serializer.data )