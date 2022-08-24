from django.contrib import admin
from .models import OrderItem, Item, Order

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Item)