from django.contrib import admin

from order.models import Cart, Cart_Item, Order, OrderItem


@admin.register(Cart)
class CartAdmin( admin.ModelAdmin ):
    list_display = ['id', 'user']

admin.site.register(Cart_Item)
admin.site.register(Order)
admin.site.register(OrderItem)