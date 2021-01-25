from django.db import models

# Create your models here.
class Products(models.Model):
    types = (
        ('PC', 'PC'),
        ("laptop", "laptop"),
        ('phone', 'phone'),
    )
    name = models.CharField(max_length=50)
    description = models.TextField(default='none')
    type = models.CharField(max_length=50, choices=types)
    price = models.IntegerField()
    image = models.ImageField(null=True, blank=True,default="no_image_avialable.png")

    def __str__(self):
        return f"{self.name} {self.type} {self.price}"

class Order(models.Model):
    statuses = (
        ('In process', 'In process'),
        ('Delivered', 'Delivered'),
        ('Not Delivered', 'not delivered'),
    )
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=20, choices=statuses, default='In Process')
    date_created = models.DateTimeField(auto_now_add=True)