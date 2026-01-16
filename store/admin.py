from django.contrib import admin
from .models import Product, Customer, Cart, CartItem, Order, OrderItem

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('title', 'price')
#     search_fields = ('title',)


admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
