from django.urls import path
from product import views


urlpatterns = [
    path('', views.View_Categories.as_view(), name="category_list"),
    path('<int:pk>/', views.View_Specific_Category.as_view(), name='view_specific_category'),
]