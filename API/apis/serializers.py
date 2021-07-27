from rest_framework.utils import field_mapping, model_meta
from .models import *
from rest_framework import serializers


class CateogiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoria
        fields = '__all__'
