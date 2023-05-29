from rest_framework import serializers
from .models import Category, Product, ProductImage, Specification


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'url',
            'name',
            'parent',
            'description',
        )


class ProductImageSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = ProductImage
        fields = (
            'id',
            'url',
            'product',
            'image',
        )


class SpecificationSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Specification
        fields = (
            'id',
            'url',
            'name',
            'value',
            'product',
        )


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer()
    images = ProductImageSerializer(many=True)
    specifications = SpecificationSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'url',
            'name',
            'category',
            'description',
            'price',
            'quantity',
            'images',
            'specifications',
        )
