from typing import ContextManager, ItemsView
from django.db.models.fields import files
from django.forms.widgets import ClearableFileInput
from django.shortcuts import render, redirect, get_object_or_404
import rest_framework
from rest_framework import serializers
from django.contrib import messages
from .models import *
from .forms import *

import json
import requests
from django.views.decorators.csrf import csrf_exempt
from .services import get_initTrxTBK, get_statusTBK
from django.http import JsonResponse
import json
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

from rest_framework import viewsets
from .serializers import  ProductSerializer

def home(request):
	return render(request,'app/home.html')
# Create your views here.
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

def store(request):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0}
		cartItems = order['get_cart_items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'app/store.html', context)

def cart(request):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0}
		cartItems = order['get_cart_items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'app/cart.html', context)

def checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0}
		cartItems = order['get_cart_items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'app/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def login(request):
    data = {
        'form':LoginForm()
    }
    if request.method == 'POST':
        formulario = LoginForm(data=request.POST)
        if formulario.is_valid():
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password"])
            auth_login(request,user)
            messages.success(request, "Logueo exitoso")
            return redirect(to="home")
        data['from'] = formulario
    return render(request, 'registration/login.html', data)

def register(request):
    data = {
        'form':RegistroForms()
    }
    if request.method == 'POST':
        formulario = RegistroForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            auth_login(request, user)
            messages.success(request, "Registro exitoso")
            return redirect(to="home")
        data['from'] = formulario
    return render(request, 'registration/register.html', data)

#API WEBBAY

def tbk(request):
    data = {
        'resultado': get_initTrxTBK()
    }
    return render(request, 'app/initTrxTbk.html',data)

@csrf_exempt
def statusTrx(request):
    data = {
        'resultado': get_statusTBK(request)
    }
    return render(request, 'app/statusTrx.html',data)


#api 

class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

	