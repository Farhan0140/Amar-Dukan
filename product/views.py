from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def products( request ):
    return Response({"messages": "Rest Api"})

