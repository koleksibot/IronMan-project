from django.contrib import admin
from .models import Product, Order, OrderedItem


admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderedItem)


