from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['product', 'quantity']

class ProfileForm(forms.ModelForm):


    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user', ]


class SignUpform(UserCreationForm):
    email = forms.EmailField(max_length=200,help_text='required')


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


