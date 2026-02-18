from django.contrib import admin
from .models import UserCart, UserOrder, OrderItems
# Register your models here.

admin.site.register(UserCart)
admin.site.register(UserOrder)
admin.site.register(OrderItems)
