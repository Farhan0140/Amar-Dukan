from django.urls import path
from product import views


urlpatterns = [
    path('', views.view_products, name="product_list"),
    path('<int:pk>/', views.view_specific_product, name='specific_product')
]