from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app.views import *


class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)

    def test_catalogo_url_resolves(self):
        url = reverse('catalogo')
        print(resolve(url))
        self.assertEquals(resolve(url).func, catalogo)
     
    def test_agregar_producto_url_resolves(self):
        url = reverse('agregar_producto')
        print(resolve(url))
        self.assertEquals(resolve(url).func, agregar_producto)
    
    def test_listar_productos_url_resolves(self):
        url = reverse('listar_productos')
        print(resolve(url))
        self.assertEquals(resolve(url).func, listar_productos)
    
    def test_modificar_producto_url_resolves(self):
        url = reverse('modificar_producto')
        print(resolve(url))
        self.assertEquals(resolve(url).func, modificar_producto)
    
    def test_tineda_url_resolves(self):
        url = reverse('tienda')
        print(resolve(url))
        self.assertEquals(resolve(url).func, tienda)

    def test_carrito_url_resolves(self):
        url = reverse('carrito')
        print(resolve(url))
        self.assertEquals(resolve(url).func, carrito)

    def test_main_url_resolves(self):
        url = reverse('main')
        print(resolve(url))
        self.assertEquals(resolve(url).func, main)

    def test_pagos_url_resolves(self):
        url = reverse('pagos')
        print(resolve(url))
        self.assertEquals(resolve(url).func, pagos)
    
    def test_agregar_producto_url_resolves(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login)
