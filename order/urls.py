from django.urls import path
from .views import (
    UserCartListCreateAPIView,
    UserCartUpdateAPIView,
    UserOrderCreateApiView,
    UserItemsListCreateAPIView,
    UserOrderDetailAPIView,
)

urlpatterns = [
    path("user-cart/", UserCartListCreateAPIView.as_view()),
    path("user-cart/<int:pk>/", UserCartUpdateAPIView.as_view()),
    path("user-order/", UserOrderCreateApiView.as_view()),
    path("user-order/<int:pk>/", UserOrderDetailAPIView.as_view()),
    path("user-items/", UserItemsListCreateAPIView.as_view()),
]
