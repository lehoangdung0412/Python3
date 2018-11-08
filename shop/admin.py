from django.contrib import admin
from . import models


@admin.register(models.Login)
class Login(admin.ModelAdmin):
    list_display = ['id', 'username', 'customer']


@admin.register(models.Customers)
class Customers(admin.ModelAdmin):
    list_display = ['id', 'forename', 'surname', 'add1', 'add2', 'add3', 'postcode', 'email', 'registered']


@admin.register(models.Orders)
class Orders(admin.ModelAdmin):
    list_display = ['id', 'customer', 'registered', 'delivery_add', 'payment_type', 'date', 'status', 'session',
                    'total']


@admin.register(models.DeliveryAdds)
class DeliveryAdds(admin.ModelAdmin):
    list_display = ['id', 'forename', 'surname', 'add1', 'add2', 'add3', 'postcode', 'phone', 'email']


@admin.register(models.OrderItems)
class OrderItems(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'quantity']


@admin.register(models.Products)
class Products(admin.ModelAdmin):
    list_display = ['id', 'cat', 'name', 'description', 'image', 'price']


@admin.register(models.Categories)
class Categories(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'image']

