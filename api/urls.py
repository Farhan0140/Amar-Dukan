
from django.urls import path, include

from rest_framework_nested import routers

from product.views import Product_View_Set, Category_View_Set, Review_View_Set
from order.views import Cart_View_Set

router = routers.DefaultRouter()
router.register('products', Product_View_Set, basename='products')
router.register('categories', Category_View_Set)
router.register('carts', Cart_View_Set, basename='carts')

product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', Review_View_Set, basename='product-review')

# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls)),
]

