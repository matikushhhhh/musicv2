from functools import total_ordering
from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import Usuario

# Create your models here.


class Cliente(models.Model):
     usuario = models.OneToOneField(
         User, null=True, blank=True, on_delete=models.CASCADE)
     nombre = models.CharField(max_length=200, null=True)
     email = models.CharField(max_length=200)

     def __str__(self):
         return str(self.nombre)


class Producto(models.Model):
     nombre = models.CharField(max_length=200, null= True)
     precio = models.IntegerField()
     digital = models.BooleanField(default=False, null=True, blank=True)
     imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)

     def __str__(self):
         return str(self.nombre)

     @property
     def imagenURL(self):
         try:
             url = self.imagen.urls
         except:
                url = ''
         return url

class Pedido(models.Model):
     cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL,null=True,blank=True)
     fecha_pedido= models.DateTimeField(auto_now_add=True)
     complete = models.BooleanField(default=False)
     transaction_id = models.CharField(max_length=100, null=True)

     def __str__(self):
         return str(self.id)

     @property
     def get_cart_total(self):
        PedidoProducto = self.pedidoproducto_set.all()
        total = sum ([item.get_total for item in PedidoProducto])
        return total

     @property
     def get_cart_items(self):
        PedidoProducto = self.pedidoproducto_set.all()
        total = sum([item.cantidad for item in PedidoProducto])
        return total


class PedidoProducto(models.Model):
     producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, blank=True, null=True)
     pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, blank=True, null=True)
     cantidad = models.IntegerField(default=0, null=True, blank=True)
     fecha_agregar =models.DateTimeField(auto_now_add=True)

     @property
     def get_total(self):
         total = self.producto.precio * self.cantidad
         return total



class DireccionEnvio(models.Model):
     cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
     pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)
     direccion = models.CharField(max_length=200, null=False)
     ciudad =models.CharField(max_length=200, null=False)
     region =models.CharField(max_length=200, null=False)
     codigo =models.CharField(max_length=200, null=False)
     fecha_agregar =models.DateTimeField(auto_now_add=True)

     def __str__(self):
         return str(self.direccion)