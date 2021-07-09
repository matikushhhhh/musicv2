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
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'app/home.html')




def store(request):
	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'app/store.html', context)

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
	return render(request, 'app/cart.html', context)

def checkout(request):
	context = {}
	return render(request, 'app/checkout.html', context)