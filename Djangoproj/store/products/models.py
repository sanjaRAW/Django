from django.db import models

# Create your models here.
class Products(models.Model):
    types = (
        ('PC', 'PC'),
        ("laptop", "laptop"),
        ('phone', 'phone'),
    )
    name = models.CharField(max_length=50)
    description = models.TextField
    type = models.CharField(max_length=50, choices=types)
    price = models.IntegerField()
    image = models.ImageField(null=True)
    products_files = models.FileField()

