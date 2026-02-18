from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserFavouriteListCreateAPIView, UserAddressListCreateAPIView

urlpatterns = [
    path('v1/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user-address/', UserAddressListCreateAPIView.as_view(), name='user_address'),
    path('user-address/<int:pk>/', UserAddressListCreateAPIView.as_view(), name='user_address'),
    path('user-favourite/', UserFavouriteListCreateAPIView.as_view(), name='user_favourite'),
    path('user-favourite/<int:pk>/', UserFavouriteListCreateAPIView.as_view(), name='user_favourite'),
]
