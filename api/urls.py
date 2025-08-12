
from django.urls import path, include

from rest_framework_nested import routers

from product.views import Product_View_Set, Category_View_Set, Review_View_Set
from order.views import Cart_View_Set, Cart_Items_View_Set

router = routers.DefaultRouter()
router.register('products', Product_View_Set, basename='products')
router.register('categories', Category_View_Set)
router.register('carts', Cart_View_Set, basename='carts')
router.register('cart-items', Cart_Items_View_Set, basename='cart_items')

product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', Review_View_Set, basename='product-review')

cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items', Cart_Items_View_Set, basename='cart-item')

# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls)),
    path('', include(cart_router.urls)),
]

