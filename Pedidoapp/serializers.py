from rest_framework import serializers

from apps.Pedidoapp.models import Pedido, Especialidad



class PedidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pedido
        fields = ('especialidad','fecha_entrega','articulo','cantidad', ) 
   
class EspecialidadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Especialidad
        fields = ('nombre', 'encargado')