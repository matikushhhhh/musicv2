from typing import ContextManager, ItemsView
from django.db.models.fields import files
from django.forms.widgets import ClearableFileInput
from django.shortcuts import render, redirect, get_object_or_404
import rest_framework
from rest_framework import serializers
from .models import *
from .forms import *
from rest_framework import viewsets
import json
import requests
from django.views.decorators.csrf import csrf_exempt
<<<<<<< HEAD
from .services import get_starWars
from .services import get_initTrxTBK, get_statusTBK
from django.contrib.auth import authenticate,login
=======
from django.shortcuts import render
>>>>>>> c65d61211e6a2c3e0eb30aba477b322a3494d3b0


# Create your views here.
def home(request):
    return render(request, 'app/home.html')




def store(request):
<<<<<<< HEAD
	context = {}
	return render(request, 'app/store.html', context)

def cart(request):
	context = {}
	return render(request, 'app/cart.html', context)
=======
	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'store/store.html', context)

def cart(request):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0}

	context = {'items':items, 'order':order}
	return render(request, 'store/cart.html', context)
>>>>>>> c65d61211e6a2c3e0eb30aba477b322a3494d3b0

def checkout(request):
	context = {}
	return render(request, 'app/checkout.html', context)


def register(request):
    data = {
        'form':RegistroForms()
    }
    if request.method == 'POST':
        formulario = RegistroForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registro exitoso")
            return redirect(to="home")
        data['from'] = formulario
    return render(request, 'registration/register.html', data)


