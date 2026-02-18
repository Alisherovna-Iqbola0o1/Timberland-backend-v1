from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Product, Category
from .serializers import  ProductSerializer, CategorySerializer
from config.paginator import MyPaginator
# Create your views here.

class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = MyPaginator

class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = MyPaginator