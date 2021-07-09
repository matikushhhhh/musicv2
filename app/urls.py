from musicv2.settings import MEDIA_ROOT, MEDIA_URL
from os import name
from django.db import router
from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from .views import tbk, statusTrx

router = routers.DefaultRouter()
router.register('productos', ProductoViewSet)

urlpatterns = [
    path('', home, name="home"),
    path('tienda/',tienda, name="tienda"),
	path('carrito/', carrito, name="carrito"),
	path('main/', main, name="main"),
    path('pagos/', pagos, name="pagos"),
    path('api/' , include(router.urls)),
    path('tbk/', tbk, name="tbk"),
    path('tbkRes', tbk, name="tbkRes"),
    path('statusTrx/', statusTrx, name="statusTrx")
    ]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    