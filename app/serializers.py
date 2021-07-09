from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import Producto 


class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        models = Producto
        fields = 'all'
  