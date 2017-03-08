from django import forms
from django.forms import ModelForm
from .models import Pedido, Especialidad


class PedidoEditForm(forms.ModelForm):
    cantidad       = forms.IntegerField(label='Cantidad:', widget=forms.TextInput(attrs={'placeholder':'Ingrese cantidad requerida'}))

    class Meta:
        model = Pedido


        fields = [

        'cantidad',

        ]    
