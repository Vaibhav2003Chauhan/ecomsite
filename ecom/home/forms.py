from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.forms import forms
from django.contrib.auth.models import User
from home.models import *

class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields='__all__'


class createuserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class customerForm(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        exclude=['user','phone']


# class createCustomer(ModelForm):
#     class Meta