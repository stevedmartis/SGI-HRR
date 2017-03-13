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


                  
def index(request):
    return render(request, 'pedido/index.html')

@login_required
@cache_page(6000)
def home(request):
      #Urologia
      total_art      = Pedido.objects.filter(especialidad=1).count()
      pend           = Pedido.objects.filter(especialidad=1).filter(estado='pendiente').count()
      entre          = Pedido.objects.filter(especialidad=1).filter(estado='entregado').count()
      #Eda
      total_art2      = Pedido.objects.filter(especialidad=2).count()
      pend2          = Pedido.objects.filter(especialidad=2).filter(estado='pendiente').count()
      entre2          = Pedido.objects.filter(especialidad=2).filter(estado='entregado').count()
      #FIBROBRONCOSCOPIA
      total_art3      = Pedido.objects.filter(especialidad=3).count()
      pend3          = Pedido.objects.filter(especialidad=3).filter(estado='pendiente').count()
      entre3          = Pedido.objects.filter(especialidad=3).filter(estado='entregado').count()
      #PAB.MENOR
      total_art4      = Pedido.objects.filter(especialidad=4).count()
      pend4          = Pedido.objects.filter(especialidad=4).filter(estado='pendiente').count()
      entre4          = Pedido.objects.filter(especialidad=4).filter(estado='entregado').count()
      #CURACION AVANZADA
      total_art5      = Pedido.objects.filter(especialidad=5).count()
      pend5          = Pedido.objects.filter(especialidad=5).filter(estado='pendiente').count()
      entre5          = Pedido.objects.filter(especialidad=5).filter(estado='entregado').count()
      #CLINICATTO    
      total_art6      = Pedido.objects.filter(especialidad=6).count()
      pend6          = Pedido.objects.filter(especialidad=6).filter(estado='pendiente').count()
      entre6          = Pedido.objects.filter(especialidad=6).filter(estado='entregado').count()
      #CARDIOLOGIA
      total_art7      = Pedido.objects.filter(especialidad=7).count()
      pend7           = Pedido.objects.filter(especialidad=7).filter(estado='pendiente').count()
      entre7          = Pedido.objects.filter(especialidad=7).filter(estado='entregado').count()
      #OTORRINO
      total_art8      = Pedido.objects.filter(especialidad=8).count()
      pend8           = Pedido.objects.filter(especialidad=8).filter(estado='pendiente').count()
      entre8          = Pedido.objects.filter(especialidad=8).filter(estado='entregado').count()
      #OFTAMOLOGIA
      total_art9      = Pedido.objects.filter(especialidad=9).count()
      pend9           = Pedido.objects.filter(especialidad=9).filter(estado='pendiente').count()
      entre9          = Pedido.objects.filter(especialidad=9).filter(estado='entregado').count()
      #P. LUMBAR
      total_art10      = Pedido.objects.filter(especialidad=10).count()
      pend10          = Pedido.objects.filter(especialidad=10).filter(estado='pendiente').count()
      entre10          = Pedido.objects.filter(especialidad=10).filter(estado='entregado').count()
      #EGG
      total_art11     = Pedido.objects.filter(especialidad=11).count()
      pend11          = Pedido.objects.filter(especialidad=11).filter(estado='pendiente').count()
      entre11          = Pedido.objects.filter(especialidad=11).filter(estado='entregado').count()
      #BRONCOPULMONAR
      total_art12     = Pedido.objects.filter(especialidad=12).count()
      pend12          = Pedido.objects.filter(especialidad=12).filter(estado='pendiente').count()
      entre12          = Pedido.objects.filter(especialidad=12).filter(estado='entregado').count()
      #TMT
      total_art13     = Pedido.objects.filter(especialidad=13).count()
      pend13          = Pedido.objects.filter(especialidad=13).filter(estado='pendiente').count()
      entre13         = Pedido.objects.filter(especialidad=13).filter(estado='entregado').count()
      #SALA INFORMES PROC.
      total_art14     = Pedido.objects.filter(especialidad=14).count()
      pend14          = Pedido.objects.filter(especialidad=14).filter(estado='pendiente').count()
      entre14         = Pedido.objects.filter(especialidad=14).filter(estado='entregado').count()
      #ADMISION.PROC
      total_art15    = Pedido.objects.filter(especialidad=15).count()
      pend15         = Pedido.objects.filter(especialidad=15).filter(estado='pendiente').count()
      entre15         = Pedido.objects.filter(especialidad=15).filter(estado='entregado').count()
      #NEUROLOGIA
      esp             = Pedido.objects.filter(especialidad=16)
      total_art16     = Pedido.objects.filter(especialidad=16).count()
      pend16          = Pedido.objects.filter(especialidad=16).filter(estado='pendiente').count()
      entre16          = Pedido.objects.filter(especialidad=16).filter(estado='entregado').count()
      #RECUPERACION
      total_art19     = Pedido.objects.filter(especialidad=19).count()
      pend19          = Pedido.objects.filter(especialidad=19).filter(estado='pendiente').count()
      entre19          = Pedido.objects.filter(especialidad=19).filter(estado='entregado').count() 
      #SALA DAN
      total_art18     = Pedido.objects.filter(especialidad=18).count()
      pend18          = Pedido.objects.filter(especialidad=18).filter(estado='pendiente').count()
      entre18          = Pedido.objects.filter(especialidad=18).filter(estado='entregado').count()
        
      #AUX.ASEO.PROC 20
      total_art20     = Pedido.objects.filter(especialidad=20).count()
      pend20         = Pedido.objects.filter(especialidad=20).filter(estado='pendiente').count()
      entre20          = Pedido.objects.filter(especialidad=20).filter(estado='entregado').count()
      #POLITACO
      total_art22     = Pedido.objects.filter(especialidad=22).count()
      pend22         = Pedido.objects.filter(especialidad=22).filter(estado='pendiente').count()
      entre22          = Pedido.objects.filter(especialidad=22).filter(estado='entregado').count()
      #ESTACION ENF. PROC
      total_art23     = Pedido.objects.filter(especialidad=23).count()
      pend23         = Pedido.objects.filter(especialidad=23).filter(estado='pendiente').count()
      entre23          = Pedido.objects.filter(especialidad=23).filter(estado='entregado').count()
      #DIABETES - CONSULTAR NOMBRE
      total_art24     = Pedido.objects.filter(especialidad=24).count()
      pend24           = Pedido.objects.filter(especialidad=24).filter(estado='pendiente').count()
      entre24          = Pedido.objects.filter(especialidad=24).filter(estado='entregado').count()
      #PROG. VIH 
      total_art25     = Pedido.objects.filter(especialidad=25).count()
      pend25           = Pedido.objects.filter(especialidad=25).filter(estado='pendiente').count()
      entre25          = Pedido.objects.filter(especialidad=25).filter(estado='entregado').count()
      #PROG. HEPATITIS - CONSULTAR NOMBRE
      total_art26      = Pedido.objects.filter(especialidad=26).count()
      pend26           = Pedido.objects.filter(especialidad=26).filter(estado='pendiente').count()
      entre26          = Pedido.objects.filter(especialidad=26).filter(estado='entregado').count()
      #SALA INFORMES CONS
      total_art27      = Pedido.objects.filter(especialidad=27).count()
      pend27           = Pedido.objects.filter(especialidad=27).filter(estado='pendiente').count()
      entre27          = Pedido.objects.filter(especialidad=27).filter(estado='entregado').count()
      #ADMISION.CONS
      total_art28      = Pedido.objects.filter(especialidad=28).count()
      pend28           = Pedido.objects.filter(especialidad=28).filter(estado='pendiente').count()
      entre28          = Pedido.objects.filter(especialidad=28).filter(estado='entregado').count()
      #PREPARACION A
      total_art30      = Pedido.objects.filter(especialidad=30).count()
      pend30           = Pedido.objects.filter(especialidad=30).filter(estado='pendiente').count()
      entre30          = Pedido.objects.filter(especialidad=30).filter(estado='entregado').count()
      #PREPARACION B
      total_art31      = Pedido.objects.filter(especialidad=31).count()
      pend31           = Pedido.objects.filter(especialidad=31).filter(estado='pendiente').count()
      entre31          = Pedido.objects.filter(especialidad=31).filter(estado='entregado').count()
      #DRA. CASTELLON
      total_art32      = Pedido.objects.filter(especialidad=32).count()
      pend32           = Pedido.objects.filter(especialidad=32).filter(estado='pendiente').count()
      entre32          = Pedido.objects.filter(especialidad=32).filter(estado='entregado').count()
      #AUX. ASEO.CONS 34

      #DERMA/FOTO
      total_art21     = Pedido.objects.filter(especialidad=21).count()
      pend21          = Pedido.objects.filter(especialidad=21).filter(estado='pendiente').count()
      entre21          = Pedido.objects.filter(especialidad=21).filter(estado='entregado').count()
      #

      encargado      = Encargado.objects.all()
      especialidad  = Especialidad.objects.all()
      pedido  = Pedido.objects.all()
      template = "index.html"
      return render_to_response(template,locals())


@cache_page(6000)
def UroloList(request):
    user = request.user
    if user.is_superuser:
        pedido = Pedido.objects.all()
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.all()
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
        pedido = Pedido.objects.all()
        template  = 'admindata.html'
        return render_to_response(template,locals())
    else:
        pedido = Pedido.objects.all()
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
      return redirect('index2.html')
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

