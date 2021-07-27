from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models.base import ModelState
from django.db.models.expressions import Case
from django.db.models.fields import BooleanField, CharField, NullBooleanField
from django.contrib.auth.models import User
from datetime import date,datetime
from django.utils.text import slugify
# Create your models here.


class categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(categoria, self).save(*args, **kwargs)   
    
