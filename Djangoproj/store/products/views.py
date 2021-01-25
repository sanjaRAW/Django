from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import *
# Create your views here.
from .forms import OrderForm

def products_page(request):
    products = Products.objects.all()
    return render(request, 'products/products.html', {"products":products})

def order_page(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    return render(request, 'products/order.html', {'form':form})

def reg_page(request):
    register = UserCreationForm()
    if request.method == 'POST':
        register = UserCreationForm(request.POST)
        if register.is_valid():
            register.save()
            return redirect('products')
    return render(request, 'products/registr.html', {'user':register})
