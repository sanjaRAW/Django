from django.shortcuts import render
from .models import *
# Create your views here.

def products_page(request):
    products = Products.objects.all()
    return render(request, 'templates/products/products.html', {"products":products})
