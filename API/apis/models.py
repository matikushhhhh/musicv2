from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models.base import ModelState
from django.db.models.expressions import Case
from django.db.models.fields import BooleanField, CharField, NullBooleanField
from django.contrib.auth.models import User
from datetime import date,datetime
from django.utils.text import slugify
# Create your models here.

class Product(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	marca = models.CharField(max_length=50,blank=True)
	price = models.FloatField()
	imagen = models.ImageField(upload_to="productos", blank = True)
	digital = models.BooleanField(default=False, null=True, blank= True)

	def __str__(self):
		return self.name
