from django.urls import path
from product import views


urlpatterns = [
    path('', views.products, name="product-list"),
]