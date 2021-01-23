from django.contrib import admin
from .models import *
# Register your models here.
class product_top(admin.ModelAdmin):
    list_display = ['image', 'name', 'description', 'type', 'price', 'products_files']

admin.site.register(Products)
admin.site.register(Order)