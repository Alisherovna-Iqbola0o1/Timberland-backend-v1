from django.contrib import admin
from .models import User, UserFavourite, UserAddress
# Register your models here.

admin.site.register(User)
admin.site.register(UserFavourite)
admin.site.register(UserAddress)
