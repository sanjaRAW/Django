from django.contrib.auth.models import User
from django.db import models
from datetime import date

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
    sale = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True, default="no_image_avialable.png")

    def __str__(self):
        return f"{self.name} {self.type} {self.price}"


class Order(models.Model):
    statuses = (
        ('In process', 'In process'),
        ('Delivered', 'Delivered'),
        ('Not Delivered', 'not delivered'),
    )
    p_methods = (
        ('money','money'),
        ('wallet', 'wallet')

    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=20, choices=statuses, default='In Process')
    date_created = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=248, choices= p_methods)


class About_us(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()


class Contacts(models.Model):
    contacttypes = (
        ('phone number', 'phone number'),
        ('email', 'email'),
        ('address', 'address'),
        ('name+surname', 'real_name')
    )
    phonenumb = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=256, null=True, blank=True)
    real_name = models.CharField(max_length=32, null=True, blank=True)
    lastname = models.CharField(max_length=256, null=True, blank=True)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)
    contacttype = models.CharField(choices=contacttypes, max_length=32)

class Profile(models.Model):
    genders = (
        ('F','F'),
        ('M','M')
    )
    user = models.OneToOneField(User,on_delete= models.CASCADE)
    image = models.ImageField(default='default_user_pfp.jpg', blank= True)
    full_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20, choices=genders)
    description = models.TextField()
    birthday = models.DateField(default=date.today())
    twitterlink = models.CharField(max_length=100)
    order_count = models.PositiveIntegerField(default=0)
    wallet = models.PositiveIntegerField(default=0)
    sale_amount = models.FloatField(default=1)

