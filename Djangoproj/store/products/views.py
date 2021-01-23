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
    return render(request, 'products/order.html')
