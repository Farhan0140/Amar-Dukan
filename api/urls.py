
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from product.views import Product_View_Set, Category_View_Set


router = DefaultRouter()
router.register('products', Product_View_Set)
router.register('categories', Category_View_Set)

# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    # path('something/' , )
]

