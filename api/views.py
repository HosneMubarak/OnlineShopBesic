from django.shortcuts import render
from rest_framework import generics
from rest_framework import serializers
from rest_framework import permissions
from shop.models import Product

from .serializers import ProductSerializer
from .permissions import IsEmployeeOrReadOnly, IsAdmin


class ProductApiListView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailApiView(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsEmployeeOrReadOnly)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDeleteUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdmin,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateApiView(generics.CreateAPIView):
    permission_classes = (IsAdmin,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
