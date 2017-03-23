from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')


class Encargado(models.Model):
    rut_encargado = models.CharField(max_length=999, primary_key=True, blank=True)
    nombre      = models.CharField(max_length=100, blank=True)
    usuario   = models.ForeignKey(User)


    def __unicode__(self):
        return '{}'.format(self.nombre)


class Especialidad(models.Model):
    nombre        = models.CharField(max_length=50, blank=True)
    estadistica   = models.IntegerField(blank=True)
    encargado     = models.ForeignKey('Encargado', blank=True, on_delete=models.CASCADE)
    estado        = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return '{}'.format(self.nombre, self.estadistica, self.encargado)


class Pedido(models.Model):
    especialidad   = models.ForeignKey('Especialidad')
    articulo       = models.ForeignKey('Articulo')
    fecha_entrega  = models.DateTimeField(auto_now_add=False)
    fecha_pedido   = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    cantidad       = models.IntegerField(blank=True)
    estado         =  models.CharField(max_length=20, blank=True, default='pendiente')


    def __str__(self):
        return '{}'.format(self.especialidad, self.articulo, self.cantidad, self.estado)


def update_total(sender, instance, **kwargs):
    instance.articulo.total_pedido +=-1 instance.cantidad 
    instance.articulo.save()

# register the signal
signals.post_save.connect(update_total, sender=Pedido, dispatch_uid="update_stock_count")


class Articulo(models.Model):
    cod_experto = models.CharField(max_length=999, primary_key=True, blank=True)
    nombre      = models.CharField(max_length=999, blank=True)
    descripcion = models.CharField(max_length=999, blank=True, null=True)
    info_bodega = models.ForeignKey('Bodega', null=True, blank=True, on_delete=models.CASCADE)
    stock       = models.IntegerField(blank=True, default=0)
    extmin      = models.CharField(max_length=999, blank=True, null=True)
    extmax      = models.CharField(max_length=999, blank=True, null=True)
    total_pedido =models.IntegerField(blank=True, default=0)


    def __str__(self):
        return '{}'.format(self.nombre, self.stock, self.cod_experto)

    def get_absolute_url(self):
        return reverse('entregado_ex', kwargs={'id_pedido_ex': pedido.id, 'cod_experto':self.cod_experto})



class Bodega(models.Model):
    cod_bodega = models.IntegerField(primary_key=True, blank=True)
    nombre     = models.CharField(max_length=20, blank=True)


    def __str__(self):
        return '{}'.format(self.nombre, self.cod_bodega)

class Pedido_Extra(models.Model):
    articulo_ex       = models.ForeignKey('Articulo')
    especialidad_ex   = models.ForeignKey('Especialidad')
    fecha_pedido_ex   = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    fecha_entrega_ex  = models.DateTimeField(auto_now_add=False)
    cantidad_ex       = models.IntegerField(blank=True, default=0)
    estado_ex         =  models.CharField(max_length=20, blank=True, default='pendiente')

    def __str__(self):
        return '{}'.format(self.articulo_ex, self.especialidad_ex, self.estado_ex, self.cantidad_ex) 



from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.sessions.models import Session

@receiver(post_save)
def clear_cache(sender, **kwargs):
    if sender != Session:
        cache.clear()



