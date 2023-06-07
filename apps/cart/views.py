from rest_framework import viewsets
from rest_framework import permissions

from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all().order_by('id')
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def save(self):
        user = self.request.user
        return super().save(user=user)


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all().order_by('id')
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]
