from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app.views import *


class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)

    def test_store_url_resolves(self):
        url = reverse('store')
        print(resolve(url))
        self.assertEquals(resolve(url).func, store)
     
    def test_cart_url_resolves(self):
        url = reverse('cart')
        print(resolve(url))
        self.assertEquals(resolve(url).func, cart)
    
    def test_checkout_url_resolves(self):
        url = reverse('checkout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, checkout)
    
    def test_login_url_resolves(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login)
    
    def test_register_resolves(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func, register)

    def test_tbk_url_resolves(self):
        url = reverse('tbk')
        print(resolve(url))
        self.assertEquals(resolve(url).func, tbk)

  