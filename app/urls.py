from musicv2.settings import MEDIA_ROOT, MEDIA_URL
from os import name
from django.db import router
from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', home, name="home"),
	path('store/', store, name="store"),
	path('cart/', cart, name="cart"),
	path('checkout/', checkout, name="checkout"),

	path('register/', register, name="register"),
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    