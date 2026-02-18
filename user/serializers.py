from rest_framework import serializers
from .models import UserAddress, UserFavourite

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = "__all__"


class UserFavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFavourite
        fields = "__all__"