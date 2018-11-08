from django.db import models
from django.contrib.auth.models import User


class Customers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    forename = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    add1 = models.CharField(max_length=100)
    add2 = models.CharField(max_length=100, blank=True, null=True)
    add3 = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(max_length=254)
    registered = models.BooleanField(default=False)

    def __str__(self):
        return '%s %s' % (self.surname, self.forename)

    class Meta:
        verbose_name_plural = 'Customers'


class Login(models.Model):
    customer = models.OneToOneField(Customers, on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Logins'


class DeliveryAdds(models.Model):
    forename = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    add1 = models.CharField(max_length=100)
    add2 = models.CharField(max_length=100, blank=True, null=True)
    add3 = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)

    class Meta:
        verbose_name_plural = 'Delivery Addresses'


class Orders(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    registered = models.BooleanField(default=False)
    delivery_add = models.OneToOneField(DeliveryAdds, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=20)
    date = models.DateTimeField('date order')
    status = models.BooleanField(default=False)
    session = models.CharField(max_length=20, blank=True, null=True)
    total = models.DecimalField(max_digits=12, decimal_places=0)

    class Meta:
        verbose_name_plural = 'Orders'


class Categories(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Products(models.Model):
    cat = models.ForeignKey(Categories, related_name='products', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=255)
    price = models.DecimalField(default=0, max_digits=10000, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Products'


class OrderItems(models.Model):
    order = models.ForeignKey(Orders, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Order Items'

