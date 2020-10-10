from django.db import models
from django.urls import reverse


class Product(models.Model):
    CATEGORY_CHOICES = (
        ('smartphone', 'Smart Phone'),
        ('laptop', 'Laptop'),
        ('desktop', 'Desktop'),
    )

    title = models.CharField(max_length=250)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=15)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse('shop:product-detail', kwargs={"id": self.id})

    def __str__(self):
        return self.title
