from django import forms
from django.db.models import fields
from .models import Product
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class RegistroForms(UserCreationForm):

    class Meta:
        model = User
        fields = ["username","email", "first_name","password1","password2"]

class LoginForm(AuthenticationForm):
    pass