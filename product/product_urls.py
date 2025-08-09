from django.urls import path
from product import views


urlpatterns = [
    path('', views.View_Products.as_view(), name="product_list"),
    path('<int:pk>/', views.View_Specific_Product.as_view(), name='specific_product'),
]