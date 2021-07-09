from typing import ContextManager, ItemsView
from django.db.models.fields import files
from django.forms.widgets import ClearableFileInput
from django.shortcuts import render, redirect, get_object_or_404
import rest_framework
from rest_framework import serializers
from .models import *
from .forms import *
from rest_framework import viewsets
from .serializers import ProductoSerializer
import json
import requests
from django.views.decorators.csrf import csrf_exempt
from .services import get_starWars
from .services import get_initTrxTBK, get_statusTBK


# Create your views here.
def home(request):
    return render(request, 'app/home.html')


from django.shortcuts import render

def store(request):
	context = {}
	return render(request, 'store/store.html', context)

def cart(request):
	context = {}
	return render(request, 'store/cart.html', context)

def checkout(request):
	context = {}
	return render(request, 'store/checkout.html', context)