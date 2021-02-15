from django.urls import path
from .views import *
from django.contrib.auth import views as a_views

urlpatterns = [
    path('', products_page, name='products'),
    path('order/<int:product_id>/', order_page, name='order'),
    path('register/', reg_page, name='register'),
    path('userlist/<int:user_id>', product_list, name='userlist'),
    path('about_us/', about_us, name='about_us'),
    path('contacts/', contacts_page, name='contacts'),
    path('order_update/<int:order_id>/', update_order, name='order_update'),
    path('order_delete/<int:order_id>/', delete_order, name='order_delete'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('reset_password/', a_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset_done/', a_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>',a_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete/', a_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('profile/', account_settings, name='profile'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',activate, name='activate')
]
