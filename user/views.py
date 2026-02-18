from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from .models import UserAddress, UserFavourite
from .serializers import UserAddressSerializer, UserFavouriteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.

class UserAddressListCreateAPIView(ListCreateAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        if instance.user == self.request.user:
            return super().perform_destroy(instance)
        return False


class UserFavouriteListCreateAPIView(ListCreateAPIView):
    queryset = UserFavourite.objects.all()
    serializer_class = UserFavouriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    def create(self, request):
        self.request.data['user'] = self.request.user.id
        return super().create(self.request)
    
class UserFavouriteDestroyAPIView(DestroyAPIView):
    queryset = UserFavourite.objects.all()
    serializer_class = UserFavouriteSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        if instance.user == self.request.user:
            return super().perform_destroy(instance)
        return Response(
            {
                "error": "Siz boshqa Userlarning <<User-Favourite>> larini ochira olmaysiz"
            }
        )
    