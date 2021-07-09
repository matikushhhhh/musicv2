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



def tienda(request):
    productos = Producto.objects.all()
    context ={'productos':productos}
    return render (request, 'app/tienda.html', context)


def carrito(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, created = Pedido.objects.get_or_create(cliente = cliente, complete = False)
        items = pedido.pedidoproducto_set.all()
    else:
        items = [] 
        pedido = {'get_cart_total' : 0, 'get_cart_items': 0}  

    context ={'items': items, 'pedido':pedido}
    return render (request, 'app/carrito.html', context)
    

def main(request):
    context ={}
    return render (request, 'app/main.html', context)



def pagos(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, created = Pedido.objects.get_or_create(cliente = cliente, complete = False)
        items = pedido.pedidoproducto_set.all()
    else:
        items = [] 
        pedido = {'get_cart_total' : 0, 'get_cart_items': 0}  

    context ={'items': items, 'pedido':pedido}
    return render (request, 'app/pagos.html', context)
    
def login(request):
    return render(request, 'registration/login.html')


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    def get_queryset(self):
        productos = Producto.objects.all()
        nombre = self.request.GET.get('nombre')

        if nombre:
            productos = productos.filter(nombre=nombre)
        return productos

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