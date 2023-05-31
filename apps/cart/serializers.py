from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Cart, CartItem
from ..shop.models import Product

User = get_user_model()


class CartSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(required=True)

    class Meta:
        model = Cart
        fields = (
            'id',
            'owner',
        )
        read_only_fields = (
            'id',
        )


class CartItemSerializer(serializers.ModelSerializer):
    product = serializers.CharField(required=True)
    cart = serializers.CharField(required=True)

    class Meta:
        model = CartItem
        fields = (
            'id',
            'product',
            'quantity',
            'cart',
        )
        read_only_fields = (
            'id',
            'cart',
        )
