
from django.urls import path, include

from rest_framework.routers import SimpleRouter

from product.views import Product_View_Set, Category_View_Set


router = SimpleRouter()
router.register('products', Product_View_Set)
router.register('categories', Category_View_Set)

urlpatterns = router.urls
