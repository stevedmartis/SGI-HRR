from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from Pedidoapp.models import Pedido, Especialidad, Encargado, Articulo, Bodega
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
from Pedidoapp.forms import PedidoEditForm, EstadisticaForm
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


@login_required
@cache_page(6000)
def home(request, id_especialidad):

      especialidad  = Especialidad.objects.all()
      pedido  = Pedido.objects.filter(especialidad=id_especialidad).count()
      template = "index3.html"
      return render_to_response(template,locals())


@cache_page(6000)
def UroloList(request):
    user = request.user
    if user.is_superuser:
        pedido = Pedido.objects.filter(especialidad=1)
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.filter(especialidad=1)
    template  = 'index2.html'
    return render_to_response(template,locals())

@cache_page(6000)
def EdaList(request):
    user = request.user
    if user.is_superuser:
        pedido = Pedido.objects.filter(especialidad=2)
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.filter(especialidad=2)
    template  = 'index2.html'
    return render_to_response(template,locals())

def FibroList(request):
    user = request.user
    if user.is_superuser:
        pedido = Pedido.objects.filter(especialidad=3)
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.filter(especialidad=3)
    template  = 'index2.html'
    return render_to_response(template,locals())

def PabMenorList(request):
    user = request.user
    if user.is_superuser:
        pedido = Pedido.objects.filter(especialidad=4)
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.filter(especialidad=4)
    template  = 'index2.html'
    return render_to_response(template,locals())

def CuracionAvList(request):
    user = request.user
    if user.is_superuser:
        pedido = Pedido.objects.filter(especialidad=5)
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.filter(especialidad=5)
    template  = 'index2.html'
    return render_to_response(template,locals())

def ClinicaList(request):
    user = request.user
    if user.is_superuser:
        pedido = Pedido.objects.filter(especialidad=6)
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.filter(especialidad=6)
    template  = 'index2.html'
    return render_to_response(template,locals())

def CardioList(request):
    user = request.user
    if user.is_superuser:
        pedido = Pedido.objects.filter(especialidad=7)
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.filter(especialidad=7)
    template  = 'index2.html'
    return render_to_response(template,locals())

def OtorrinoList(request):
    user = request.user
    if user.is_superuser:
        pedido = Pedido.objects.filter(especialidad=8)
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.filter(especialidad=8)
    template  = 'index2.html'
    return render_to_response(template,locals())

def OftalList(request):
    user = request.user
    if user.is_superuser:
        pedido = Pedido.objects.filter(especialidad=9)
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.filter(especialidad=9)
    template  = 'index2.html'
    return render_to_response(template,locals())

def PlumbarList(request):
    user = request.user
    if user.is_superuser:
        pedido = Pedido.objects.filter(especialidad=10)
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.filter(especialidad=10)
    template  = 'index2.html'
    return render_to_response(template,locals())

def EggList(request):
    user = request.user
    if user.is_superuser:
        pedido = Pedido.objects.filter(especialidad=11)
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.filter(especialidad=11)
    template  = 'index2.html'
    return render_to_response(template,locals())

def BroncoList(request):
    user = request.user
    if user.is_superuser:
        pedido = Pedido.objects.filter(especialidad=12)
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.filter(especialidad=12)
    template  = 'index2.html'
    return render_to_response(template,locals())

def TmtList(request):
    user = request.user
    if user.is_superuser:
        pedido = Pedido.objects.filter(especialidad=13)
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.filter(especialidad=13)
    template  = 'index2.html'
    return render_to_response(template,locals())


def SalainfoProcList(request):
    user = request.user
    if user.is_superuser:
        pedido = Pedido.objects.filter(especialidad=14)
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.filter(especialidad=14)
    template  = 'index2.html'
    return render_to_response(template,locals())

def AdmisionList(request):
    user = request.user
    if user.is_superuser:
        pedido = Pedido.objects.filter(especialidad=15)
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.filter(especialidad=15)
    template  = 'index2.html'
    return render_to_response(template,locals())

def NeuroList(request):
    user = request.user
    if user.is_superuser:
        pedido = Pedido.objects.filter(especialidad=16)
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.filter(especialidad=16)
    template  = 'index2.html'
    return render_to_response(template,locals())

def RecuperaList(request):
    user = request.user
    if user.is_superuser:
        pedido = Pedido.objects.filter(especialidad=19)
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.filter(especialidad=19)
    template  = 'index2.html'
    return render_to_response(template,locals())

def SaladanList(request):
    user = request.user
    if user.is_superuser:
        pedido = Pedido.objects.filter(especialidad=18)
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.filter(especialidad=18)
    template  = 'index2.html'
    return render_to_response(template,locals())

def AseoProcList(request):
    user = request.user
    if user.is_superuser:
        pedido = Pedido.objects.filter(especialidad=20)
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.filter(especialidad=20)
    template  = 'index2.html'
    return render_to_response(template,locals())

def DermaList(request):
    user = request.user
    if user.is_superuser:
        pedido = Pedido.objects.filter(especialidad=21)
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.filter(especialidad=21)
    template  = 'index2.html'
    return render_to_response(template,locals())

def PoliTacoList(request):
    user = request.user
    if user.is_superuser:
        pedido = Pedido.objects.filter(especialidad=22)
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.filter(especialidad=22)
    template  = 'index2.html'
    return render_to_response(template,locals())


def EstacionEnfList(request):
    user = request.user
    if user.is_superuser:
        pedido = Pedido.objects.filter(especialidad=23)
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.filter(especialidad=23)
    template  = 'index2.html'
    return render_to_response(template,locals())

def DiabetesList(request):
    user = request.user
    if user.is_superuser:
        pedido = Pedido.objects.filter(especialidad=24)
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.filter(especialidad=24)
    template  = 'index2.html'
    return render_to_response(template,locals())

def VihList(request):
    user = request.user
    if user.is_superuser:
        pedido = Pedido.objects.filter(especialidad=25)
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.filter(especialidad=25)
    template  = 'index2.html'
    return render_to_response(template,locals())

def HepatiList(request):
    user = request.user
    if user.is_superuser:
        pedido = Pedido.objects.filter(especialidad=26)
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.filter(especialidad=26)
    template  = 'index2.html'
    return render_to_response(template,locals())

def SalainfoConsList(request):
    user = request.user
    if user.is_superuser:
        pedido = Pedido.objects.filter(especialidad=27)
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.filter(especialidad=27)
    template  = 'index2.html'
    return render_to_response(template,locals())

def AdmisionConsList(request):
    user = request.user
    if user.is_superuser:
        pedido = Pedido.objects.filter(especialidad=28)
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.filter(especialidad=28)
    template  = 'index2.html'
    return render_to_response(template,locals())

def PrepaListA(request):
    user = request.user
    if user.is_superuser:
        pedido = Pedido.objects.filter(especialidad=30)
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.filter(especialidad=30)
    template  = 'index2.html'
    return render_to_response(template,locals())

def PrepaListB(request):
    user = request.user
    if user.is_superuser:
        pedido = Pedido.objects.filter(especialidad=31)
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.filter(especialidad=31)
    template  = 'index2.html'
    return render_to_response(template,locals())

def DraCasList(request):
    user = request.user
    if user.is_superuser:
        pedido = Pedido.objects.filter(especialidad=32)
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.filter(especialidad=32)
    template  = 'index2.html'
    return render_to_response(template,locals())

def ListAll(request, id_especialidad):
  especialidad = Especialidad.objects.get(id=id_especialidad)
  if request.method == 'GET':
    user = request.user
    if user.is_superuser:
        pedido = Pedido.objects.filter(especialidad=especialidad)
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.filter(especialidad=especialidad)
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
      return redirect('usuario:lita_todo')
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

