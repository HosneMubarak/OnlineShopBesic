from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    location = models.CharField(max_length=50)

    def __str__(self):
        return f"Customer Name: {self.user.username}"


class Employee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=50)

    def __str__(self):
        return f"Employee Name: {self.user.username}"
