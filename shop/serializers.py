from rest_framework import serializers
from . import models


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customers
        fields = '__all__'


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Login
        fields = '__all__'


class DeliveryAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DeliveryAdds
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItems
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = models.Orders
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Products
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = models.Categories
        fields = '__all__'
