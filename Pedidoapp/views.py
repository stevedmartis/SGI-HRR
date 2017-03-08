from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from Pedidoapp.models import Pedido, Especialidad, Encargado, Articulo, Bodega
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
from Pedidoapp.forms import PedidoEditForm
from django.template.context import RequestContext
from django.template import RequestContext
from django.views.decorators.cache import cache_page
from django.shortcuts import get_list_or_404, get_object_or_404
from django.db import models
from django.db.models import Count

import psycopg2
import sys
import json


#reload(sys)
#sys.setdefaultencoding('utf8')



@login_required
@cache_page(1000)
def add(request):
    if request.method == 'POST':
        form = PedidoEditForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('add')
    else:
        form = PedidoEditForm()
    return render(request, 'form.html', {'form':form})


                  
def index(request):
    return render(request, 'pedido/index.html')

@login_required
#@cache_page(6000)
def home(request):
    user = request.user
    if user.is_superuser:
      pedido         = Pedido.objects.all()
      pend           = Pedido.objects.filter(especialidad=1).filter(estado='pendiente').count()
      entre          = Pedido.objects.filter(especialidad=1).filter(estado='entregado').count()
      especialidades = Especialidad.objects.all()
      encargado      = Encargado.objects.all()
      template       = "index.html"
      return render_to_response(template,locals())
    else :
      return render(request, 'index.html')



def ArticuloListView(request):
    user = request.user
    if user.is_superuser:
        pedido = Pedido.objects.all()
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.filter(especialidad__encargado__usuario=user.id)
    template  = 'index2.html'
    return render_to_response(template,locals())


def Pedido_Edit(request, id_pedido):
    pedido = Pedido.objects.get(id=id_pedido)
    if request.method == 'GET':
      form = PedidoEditForm(instance=pedido)
    else:
      form = PedidoEditForm(request.POST, instance=pedido)
      if form.is_valid():
          form.save()
          pedido.estado = 'pendiente'
          pedido.fecha_pedido = datetime.now()
          pedido.save()
      return redirect('usuario:listar_esp')
    return render(request, 'form.html', {'form':form})




from django.views.generic import ListView, DetailView
   

class PedidoDetailView(DetailView):
    model = Pedido
    def get_template_names(self):
        return render('index.html')


def Aprobado(request, id_pedido):
    pedido = Pedido.objects.get(id=id_pedido)
    if request.method == 'GET':
        pedido.estado = 'entregado'
        pedido.fecha_entrega = datetime.now()
        pedido.save()
     # articulo.stock = cantidad
    return HttpResponseRedirect("/solicitar/lista/")

