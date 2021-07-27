#tranforma datos  a JSON
from rest_framework.utils import field_mapping, model_meta
from django.db.models import fields
from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
