from django.db import models

# Create your models here.

class Product(models.Model):
    stripe_product_id = models.CharField(max_length=100, unique=True)
    stripe_price_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    