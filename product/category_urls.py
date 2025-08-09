from django.urls import path
from product import views


urlpatterns = [
    path('', views.Category_List.as_view(), name="category_list"),
    path('<int:pk>/', views.Category_Details.as_view(), name='view_specific_category'),
]