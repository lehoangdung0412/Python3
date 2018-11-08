from .serializers import *
from . import models
from rest_framework import serializers, viewsets, permissions
from rest_framework_jwt import authentication


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customers.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JSONWebTokenAuthentication]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Products.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if (self.action == 'list') | (self.action == 'retrieve'):
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


class DeliveryAddViewSet(viewsets.ModelViewSet):
    queryset = models.DeliveryAdds.objects.all()
    serializer_class = DeliveryAddSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Orders.objects.all()
    serializer_class = OrderSerializer

    def get_permissions(self):
        if self.action == 'retrieve':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Categories.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if (self.action == 'list') | (self.action == 'retrieve'):
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = models.OrderItems.objects.all()
    serializer_class = OrderItemSerializer


class LoginViewSet(viewsets.ModelViewSet):
    queryset = models.Login.objects.all()
    serializer_class = LoginSerializer
