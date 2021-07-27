from rest_framework.utils import field_mapping, model_meta
from .models import *
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
