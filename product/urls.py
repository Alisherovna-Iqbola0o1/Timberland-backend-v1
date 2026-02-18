from django.urls import path
from .views import CategoryListCreateAPIView, ProductListCreateAPIView

urlpatterns = [
    path("category/", CategoryListCreateAPIView.as_view()),
    path("product/", ProductListCreateAPIView.as_view()),
]
