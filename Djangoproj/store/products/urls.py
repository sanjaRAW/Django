from django.urls import path
from .views import products_page, order_page

urlpatterns = [
    path('', products_page, name='products'),
    path('order/', order_page)
]
