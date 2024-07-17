from django.db import models # type: ignore

# Create your models here.

class Product(models.Model):
    class ProductType(models.TextChoices):
        KBIS = 'KBIS'
        OTHER = 'Other'
        
    stripe_product_id = models.CharField(max_length=100, unique=True)
    stripe_price_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    product_type = models.CharField(max_length=10,choices=ProductType.choices,editable=False,default=ProductType.KBIS)

    def __str__(self):
        return self.name
    