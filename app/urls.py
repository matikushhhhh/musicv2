from musicv2.settings import MEDIA_ROOT, MEDIA_URL
from os import name
from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products',ProductViewSet)

urlpatterns = [
    path('', home, name="home"),
	path('store/', store, name="store"),
	path('cart/', cart, name="cart"),
	path('checkout/', checkout, name="checkout"),
    path('update_item/', updateItem, name="updateItem"),
    path('accounts/login/', login, name="login"),
	path('register/', register, name="register"),
	path('tbk/', tbk, name="tbk"),
    path('tbkRes/', tbk, name="tbkRes"),
    path('statusTrx/', statusTrx, name="statusTrx"),
	path('api/',include(router.urls)),
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    