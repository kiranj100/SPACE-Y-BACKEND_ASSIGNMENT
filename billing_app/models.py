from django.contrib.auth.models import AbstractUser
from django.db import models


class Employee(models.Model):
   username = models.CharField(max_length=50)
   password = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class Bill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, default='Cash')
