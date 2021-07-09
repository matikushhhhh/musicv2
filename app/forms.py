from django import forms
from django.db.models import fields
<<<<<<< HEAD
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
=======
from .models import Product
>>>>>>> c65d61211e6a2c3e0eb30aba477b322a3494d3b0



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class RegistroForms(UserCreationForm):

    pass