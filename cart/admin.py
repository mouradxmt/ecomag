from django.contrib import admin
from cart.models import Order, OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)
# Register your models here.
