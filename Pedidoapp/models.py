from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals



class Encargado(models.Model):
    rut_encargado = models.CharField(max_length=999, primary_key=True, blank=True)
    nombre      = models.CharField(max_length=100, blank=True)
    usuario   = models.ForeignKey(User)


    def __str__(self):
        return '{}'.format(self.nombre, self.usuario)
    


class Especialidad(models.Model):
    nombre        = models.CharField(max_length=50, blank=True)
    estadistica   = models.IntegerField(blank=True)
    encargado     = models.ForeignKey('Encargado', blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre)



    def __str__(self):
        return '{}'.format(self.nombre)


class Pedido(models.Model):
    especialidad   = models.ForeignKey('Especialidad')
    articulo       = models.ForeignKey('Articulo')
    fecha_entrega  = models.DateTimeField(auto_now_add=False)
    fecha_pedido   = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    cantidad       = models.IntegerField(blank=True)
    pendiente      = models.CharField(max_length=999,  null=True, blank=True)
    estado         =  models.CharField(max_length=20, blank=True, default='pendiente')


    def __str__(self):
        return '{}'.format(self.especialidad, self.articulo, self.cantidad, self.estado)


class Articulo(models.Model):
    cod_experto = models.CharField(max_length=999, primary_key=True, blank=True)
    nombre      = models.CharField(max_length=999, blank=True)
    descripcion = models.CharField(max_length=999, blank=True, null=True)
    info_bodega = models.ForeignKey('Bodega', null=True, blank=True, on_delete=models.CASCADE)
    stock       = models.CharField(max_length=999, blank=True)
    extmin      = models.CharField(max_length=999, blank=True, null=True)
    extmax      = models.CharField(max_length=999, blank=True, null=True)


    def __str__(self):
        return '{}'.format(self.nombre, self.stock) 





class Bodega(models.Model):
    cod_bodega = models.IntegerField(primary_key=True, blank=True)
    nombre     =  models.CharField(max_length=20, blank=True)


    def __str__(self):
        return '{}'.format(self.nombre, self.cod_bodega) 

from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.sessions.models import Session

@receiver(post_save)
def clear_cache(sender, **kwargs):
    if sender != Session:
        cache.clear()



