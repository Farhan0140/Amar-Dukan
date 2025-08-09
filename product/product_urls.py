from django.urls import path
from product import views


urlpatterns = [
    path('', views.Product_List.as_view(), name="product_list"),
    path('<int:pk>/', views.Product_Details.as_view(), name='specific_product'),
]