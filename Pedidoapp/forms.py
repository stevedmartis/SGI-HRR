from django import forms
from django.forms import ModelForm
from .models import Pedido, Especialidad


class PedidoEditForm(forms.ModelForm):
    cantidad       = forms.IntegerField(label='Cantidad:', widget=forms.TextInput(attrs=attrs={'size':'10'}))

    class Meta:
        model = Pedido


        fields = [

        'cantidad',

        ]  

class EstadisticaForm(forms.ModelForm):
    estadistica    = forms.IntegerField(label='Estadistica Menusal:', widget=forms.TextInput(attrs={'placeholder':'Ingrese numero pacientes'}))  
    
    class Meta:
    	model = Especialidad

    	fields = [

        'estadistica',

    	]