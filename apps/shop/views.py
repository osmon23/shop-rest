from rest_framework import viewsets
from rest_framework import permissions

from .models import Category, Product, ProductImage, Specification
from .serializers import CategorySerializer, ProductSerializer, ProductImageSerializer, SpecificationSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.order_by('id')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [permissions.IsAuthenticated]


class SpecificationViewSet(viewsets.ModelViewSet):
    queryset = Specification.objects.all()
    serializer_class = SpecificationSerializer
    permission_classes = [permissions.IsAuthenticated]
