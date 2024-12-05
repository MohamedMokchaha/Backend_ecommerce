from django.core.validators import MinValueValidator
from django.db import models
from django.core.exceptions import ValidationError

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(validators=[MinValueValidator(0.01)])
    stock = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name
