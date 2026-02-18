from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework.exceptions import ValidationError
from .models import UserCart, UserOrder, OrderItems


class UserCartListCreateSerialzier(ModelSerializer):

    class Meta:
        model = UserCart
        fields = '__all__'
        read_only_fields = ("created_at", "updated_at")


class UserCartUpdateSerialzier(ModelSerializer):

    class Meta:
        model = UserCart
        fields = '__all__'
        read_only_fields = ("user", "product", "created_at", "updated_at")

    def validate_quantity(self, value):
        if value > 50:
            raise ValidationError("Siz 50 tadan ko'p birdaniga qo'sha olmaysiz!")
        return value

    def validate_user(self, value):
        if self.instance and value != self.instance.user:
            raise ValidationError("Siz birovni savatchasini o'zgartira olmaysiz!")
        return value


class UserOrderListSerialzier(ModelSerializer):

    class Meta:
        model = UserOrder
        fields = '__all__'


class UserOrderCreateSerialzier(ModelSerializer):

    class Meta:
        model = UserOrder
        fields = '__all__'
        extra_kwargs = {
            'address': {'required': True}
        }
        
    def validate_address(self, value):
        if value.user != self.user:
            raise ValidationError("Siz o'zingizning manzilingizga buyurtma berolasiz holos!")
        return value


class OrderItemsSerialzier(ModelSerializer):

    class Meta:
        model = OrderItems
        fields = '__all__'
