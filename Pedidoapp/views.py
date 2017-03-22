#!/usr/bin/env python
#-*- coding: utf-8 -*- 

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from Pedidoapp.models import Pedido, Especialidad, Encargado, Articulo, Bodega, Pedido_Extra
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
from Pedidoapp.forms import PedidoEditForm, EstadisticaForm, ExtraForm
from django.template.context import RequestContext
from django.template import RequestContext
from django.views.decorators.cache import cache_page
from django.shortcuts import get_list_or_404, get_object_or_404
from django.db import models
from django.db.models import Count
from django.core.urlresolvers import reverse

import datetime
mylist = []
today = datetime.date.today()
mylist.append(today)
import psycopg2
import sys
import json




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
def home(request):
    user = request.user
    if user.is_superuser:
      #Urologia
      total_art      = Pedido.objects.filter(especialidad=1).count()
      pend           = Pedido.objects.filter(especialidad=1).filter(estado='pendiente').count()
      entre          = Pedido.objects.filter(especialidad=1).filter(estado='entregado').count()
      id_urolo  = Pedido.objects.get(id=15)
      #Eda
      total_art2      = Pedido.objects.filter(especialidad=2).count()
      pend2          = Pedido.objects.filter(especialidad=2).filter(estado='pendiente').count()
      entre2          = Pedido.objects.filter(especialidad=2).filter(estado='entregado').count()
      id_eda  = Pedido.objects.get(id=2)
      #FIBROBRONCOSCOPIA
      total_art3      = Pedido.objects.filter(especialidad=3).count()
      pend3          = Pedido.objects.filter(especialidad=3).filter(estado='pendiente').count()
      entre3          = Pedido.objects.filter(especialidad=3).filter(estado='entregado').count()
      id_fibro  = Pedido.objects.get(id=3)
      #PAB.MENOR
      total_art4      = Pedido.objects.filter(especialidad=4).count()
      pend4          = Pedido.objects.filter(especialidad=4).filter(estado='pendiente').count()
      entre4          = Pedido.objects.filter(especialidad=4).filter(estado='entregado').count()
      id_pabm  = Pedido.objects.get(id=4)
      #CURACION AVANZADA
      total_art5      = Pedido.objects.filter(especialidad=5).count()
      pend5          = Pedido.objects.filter(especialidad=5).filter(estado='pendiente').count()
      entre5          = Pedido.objects.filter(especialidad=5).filter(estado='entregado').count()
      id_curav  = Pedido.objects.get(id=5)
      #CLINICATTO    
      total_art6      = Pedido.objects.filter(especialidad=6).count()
      pend6          = Pedido.objects.filter(especialidad=6).filter(estado='pendiente').count()
      entre6          = Pedido.objects.filter(especialidad=6).filter(estado='entregado').count()
      id_clinitt  = Pedido.objects.get(id=6)
      #CARDIOLOGIA
      total_art7      = Pedido.objects.filter(especialidad=7).count()
      pend7           = Pedido.objects.filter(especialidad=7).filter(estado='pendiente').count()
      entre7          = Pedido.objects.filter(especialidad=7).filter(estado='entregado').count()
      id_cardio  = Pedido.objects.get(id=7)
      #OTORRINO
      total_art8      = Pedido.objects.filter(especialidad=8).count()
      pend8           = Pedido.objects.filter(especialidad=8).filter(estado='pendiente').count()
      entre8          = Pedido.objects.filter(especialidad=8).filter(estado='entregado').count()
      id_otto  = Pedido.objects.get(id=8)
      #OFTAMOLOGIA
      total_art9      = Pedido.objects.filter(especialidad=9).count()
      pend9           = Pedido.objects.filter(especialidad=9).filter(estado='pendiente').count()
      entre9          = Pedido.objects.filter(especialidad=9).filter(estado='entregado').count()
      id_oftal  = Pedido.objects.get(id=9)
      #P. LUMBAR
      total_art10      = Pedido.objects.filter(especialidad=10).count()
      pend10          = Pedido.objects.filter(especialidad=10).filter(estado='pendiente').count()
      entre10          = Pedido.objects.filter(especialidad=10).filter(estado='entregado').count()
      id_lumbar  = Pedido.objects.get(id=10)
      #EGG
      total_art11     = Pedido.objects.filter(especialidad=11).count()
      pend11          = Pedido.objects.filter(especialidad=11).filter(estado='pendiente').count()
      entre11          = Pedido.objects.filter(especialidad=11).filter(estado='entregado').count()
      id_egg  = Pedido.objects.get(id=11)
      #BRONCOPULMONAR
      total_art12     = Pedido.objects.filter(especialidad=12).count()
      pend12          = Pedido.objects.filter(especialidad=12).filter(estado='pendiente').count()
      entre12          = Pedido.objects.filter(especialidad=12).filter(estado='entregado').count()
      id_bronco  = Pedido.objects.get(id=12)
      #TMT
      total_art13     = Pedido.objects.filter(especialidad=13).count()
      pend13          = Pedido.objects.filter(especialidad=13).filter(estado='pendiente').count()
      entre13         = Pedido.objects.filter(especialidad=13).filter(estado='entregado').count()
      id_tmt  = Pedido.objects.get(id=13)
      #SALA INFORMES PROC.
      total_art14     = Pedido.objects.filter(especialidad=14).count()
      pend14          = Pedido.objects.filter(especialidad=14).filter(estado='pendiente').count()
      entre14         = Pedido.objects.filter(especialidad=14).filter(estado='entregado').count()
      id_salaproc  = Pedido.objects.get(id=14)
      #ADMISION.PROC
      total_art15    = Pedido.objects.filter(especialidad=15).count()
      pend15         = Pedido.objects.filter(especialidad=15).filter(estado='pendiente').count()
      entre15         = Pedido.objects.filter(especialidad=15).filter(estado='entregado').count()
      id_admiproc  = Pedido.objects.get(id=15)
      #NEUROLOGIA
      esp             = Pedido.objects.filter(especialidad=16)
      total_art16     = Pedido.objects.filter(especialidad=16).count()
      pend16          = Pedido.objects.filter(especialidad=16).filter(estado='pendiente').count()
      entre16          = Pedido.objects.filter(especialidad=16).filter(estado='entregado').count()
      id_neuro  = Pedido.objects.get(id=16)
      #RECUPERACION
      total_art19     = Pedido.objects.filter(especialidad=19).count()
      pend19          = Pedido.objects.filter(especialidad=19).filter(estado='pendiente').count()
      entre19          = Pedido.objects.filter(especialidad=19).filter(estado='entregado').count() 
      id_recu  = Pedido.objects.get(id=19)
      #SALA DAN
      total_art18     = Pedido.objects.filter(especialidad=18).count()
      pend18          = Pedido.objects.filter(especialidad=18).filter(estado='pendiente').count()
      entre18          = Pedido.objects.filter(especialidad=18).filter(estado='entregado').count()
      id_sdan  = Pedido.objects.get(id=18)
      #AUX.ASEO.PROC 20
      total_art20     = Pedido.objects.filter(especialidad=20).count()
      pend20         = Pedido.objects.filter(especialidad=20).filter(estado='pendiente').count()
      entre20          = Pedido.objects.filter(especialidad=20).filter(estado='entregado').count()
      id_aseop  = Pedido.objects.get(id=20)
      #DERMA/FOTO
      total_art21     = Pedido.objects.filter(especialidad=21).count()
      pend21          = Pedido.objects.filter(especialidad=21).filter(estado='pendiente').count()
      entre21          = Pedido.objects.filter(especialidad=21).filter(estado='entregado').count()
      id_derma         = Pedido.objects.get(id=21)
      #POLITACO
      total_art22     = Pedido.objects.filter(especialidad=22).count()
      pend22         = Pedido.objects.filter(especialidad=22).filter(estado='pendiente').count()
      entre22          = Pedido.objects.filter(especialidad=22).filter(estado='entregado').count()
      id_taco  = Pedido.objects.get(id=22)
      #ESTACION ENF. PROC
      total_art23     = Pedido.objects.filter(especialidad=23).count()
      pend23         = Pedido.objects.filter(especialidad=23).filter(estado='pendiente').count()
      entre23          = Pedido.objects.filter(especialidad=23).filter(estado='entregado').count()
      id_enfp          = Pedido.objects.get(id=23)
      #DIABETES 
      total_art24     = Pedido.objects.filter(especialidad=24).count()
      pend24           = Pedido.objects.filter(especialidad=24).filter(estado='pendiente').count()
      entre24          = Pedido.objects.filter(especialidad=24).filter(estado='entregado').count()
      id_diab          = Pedido.objects.get(id=24)
      #PROG. VIH 
      total_art25     = Pedido.objects.filter(especialidad=25).count()
      pend25           = Pedido.objects.filter(especialidad=25).filter(estado='pendiente').count()
      entre25          = Pedido.objects.filter(especialidad=25).filter(estado='entregado').count()
      id_vih           = Pedido.objects.get(id=25)
      #PROG. HEPATITIS 
      total_art26      = Pedido.objects.filter(especialidad=26).count()
      pend26           = Pedido.objects.filter(especialidad=26).filter(estado='pendiente').count()
      entre26          = Pedido.objects.filter(especialidad=26).filter(estado='entregado').count()
      id_hepa          = Pedido.objects.get(id=26)

      #SALA INFORMES CONS
      total_art27      = Pedido.objects.filter(especialidad=27).count()
      pend27           = Pedido.objects.filter(especialidad=27).filter(estado='pendiente').count()
      entre27          = Pedido.objects.filter(especialidad=27).filter(estado='entregado').count()
      id_salac          = Pedido.objects.get(id=27)
      #ADMISION.CONS
      total_art28      = Pedido.objects.filter(especialidad=28).count()
      pend28           = Pedido.objects.filter(especialidad=28).filter(estado='pendiente').count()
      entre28          = Pedido.objects.filter(especialidad=28).filter(estado='entregado').count()
      id_admicons      = Pedido.objects.get(id=28)
      #PAT.MAMARIA
      total_art29      = Pedido.objects.filter(especialidad=29).count()
      pend29           = Pedido.objects.filter(especialidad=29).filter(estado='pendiente').count()
      entre29          = Pedido.objects.filter(especialidad=29).filter(estado='entregado').count()
      id_mama      = Pedido.objects.get(id=29)
      #PREPARACION A
      total_art30      = Pedido.objects.filter(especialidad=30).count()
      pend30           = Pedido.objects.filter(especialidad=30).filter(estado='pendiente').count()
      entre30          = Pedido.objects.filter(especialidad=30).filter(estado='entregado').count()
      id_prea          = Pedido.objects.get(id=30)
      #PREPARACION B
      total_art31      = Pedido.objects.filter(especialidad=31).count()
      pend31           = Pedido.objects.filter(especialidad=31).filter(estado='pendiente').count()
      entre31          = Pedido.objects.filter(especialidad=31).filter(estado='entregado').count()
      id_preb          = Pedido.objects.get(id=31)
      #DRA. CASTELLON
      total_art32      = Pedido.objects.filter(especialidad=32).count()
      pend32           = Pedido.objects.filter(especialidad=32).filter(estado='pendiente').count()
      entre32          = Pedido.objects.filter(especialidad=32).filter(estado='entregado').count()
      id_caste         = Pedido.objects.get(id=32)
      #SECRETARIAS.CAE
      total_art33      = Pedido.objects.filter(especialidad=33).count()
      pend33           = Pedido.objects.filter(especialidad=33).filter(estado='pendiente').count()
      entre33          = Pedido.objects.filter(especialidad=33).filter(estado='entregado').count()
      id_secre         = Pedido.objects.get(id=33)
      #AUX. ASEO.CONS 34
      total_art34      = Pedido.objects.filter(especialidad=34).count()
      pend34           = Pedido.objects.filter(especialidad=34).filter(estado='pendiente').count()
      entre34          = Pedido.objects.filter(especialidad=34).filter(estado='entregado').count()
      id_aseocon         = Pedido.objects.get(id=34)      
      template = "index.html"
      return render_to_response(template,locals())
    else:
      especialidad  = Especialidad.objects.filter(encargado__usuario=user.id)
      template2 = "index3.html"
      return render_to_response(template2,locals())

@cache_page(6000)
@login_required
def ListAll(request, id_especialidad):
  especialidad = Especialidad.objects.get(id=id_especialidad)
  if request.method == 'GET':
        pedido = Pedido.objects.filter(especialidad=especialidad).order_by('-cantidad')
        template  = 'admindata.html'
        return render(request, template, {'pedido':pedido, 'especialidad':especialidad})

@cache_page(6000)
@login_required
def ListEspeci(request, id_especialidad):
  especialidad = Especialidad.objects.get(id=id_especialidad)
  pedido = Pedido.objects.filter(especialidad=especialidad).order_by('-cantidad')
  if request.method == 'GET':
    form = EstadisticaForm(instance=especialidad)
  else:
    form = EstadisticaForm(request.POST, instance=especialidad)
    if form.is_valid():
        form.save()
        especialidad.estado = "pendiente"
        especialidad.save()
    return HttpResponseRedirect('/solicitar/lista_active/%s/' % id_especialidad)
  return render(request, 'index2.html', {'form':form, 'pedido':pedido, 'especialidad':especialidad})


@login_required
def Cant_ingresar(request, id_pedido, id_especialidad):
    especialidad = Especialidad.objects.get(id=id_especialidad)
    pedido = Pedido.objects.get(id=id_pedido)
    if request.method == 'GET':
      form = PedidoEditForm(instance=pedido)
    else:
      form = PedidoEditForm(request.POST, instance=pedido)
      if form.is_valid():
          form.save()
          pedido.estado = 'pendiente'
          pedido.fecha_pedido = datetime.date.today()
          pedido.save()
          especialidad.estado='pendiente'
          especialidad.save()
      return HttpResponseRedirect('/solicitar/lista_active/%s/' % id_especialidad)
    return render(request, 'form.html', {'form':form, 'pedido':pedido, 'especialidad':especialidad}) 

@login_required
def Cant_update(request, id_pedido, id_especialidad):
    especialidad = Especialidad.objects.get(id=id_especialidad)
    pedido = Pedido.objects.get(id=id_pedido)
    if request.method == 'GET':
      form = PedidoEditForm(instance=pedido)
    else:
      form = PedidoEditForm(request.POST, instance=pedido)
      if form.is_valid():
          form.save()
          pedido.estado = 'modificado'
          pedido.save()
      return HttpResponseRedirect('/solicitar/lista_super/%s/' % id_especialidad)
    return render(request, 'form.html', {'form':form, 'pedido':pedido, 'especialidad':especialidad})



from django.views.generic import ListView, DetailView
   

class PedidoDetailView(DetailView):
    model = Pedido
    def get_template_names(self):
        return render('index.html')

@login_required
def Update_stock(request, id_pedido, cod_experto, id_especialidad):
  if request.method == 'GET':
    especialidad = Especialidad.objects.get(id=id_especialidad)
    pedido = Pedido.objects.get(id=id_pedido)
    articulo = Articulo.objects.get(pk=cod_experto)
    articulo.stock -= pedido.cantidad
    articulo.total_pedido += pedido.cantidad
    articulo.save()
    pedido.estado = 'entregado'
    pedido.fecha_entrega = datetime.date.today()
    pedido.save()
    especialidad.estado = 'entregado'
    especialidad.save()
    return HttpResponseRedirect('/solicitar/lista_super/%s/' % id_especialidad)

@login_required
def PedidoExtra(request, id_especialidad):
    especialidad = Especialidad.objects.get(id=id_especialidad)
    if request.method == 'GET':
      form = ExtraForm()
    else:
      form = ExtraForm(request.POST)
      if form.is_valid():
        esp = form.save(commit=False)
        esp.especialidad_ex = especialidad
        esp.save()
        form.save()
      return HttpResponseRedirect('/solicitar/home/')
    return render(request, 'form2.html', {'form':form, 'especialidad':especialidad})

@login_required
def ExtraView(request):
      user = request.user
      if user.is_superuser:
        extra = Pedido_Extra.objects.all()
        return render(request, 'extra.html', {'extra':extra, 'user':user})
      else:
        extra = Pedido_Extra.objects.filter(especialidad_ex__encargado__usuario=user.id)
        return render(request, 'extra.html', {'extra':extra, 'user':user})
  
@login_required
def Cant_upex(request, id_pedido_ex):
    extra = Pedido_Extra.objects.get(id=id_pedido_ex)
    if request.method == 'GET':
      form = ExtraForm(instance=extra)
    else:
      form = ExtraForm(request.POST, instance=extra)
      if form.is_valid():
          form.save()
          extra.estado_ex = 'modificado'
          extra.save()
      return HttpResponseRedirect('/solicitar/pedidos-extra/')
    return render(request, 'form2.html', {'form':form, 'extra':extra})


@login_required
def Update_stockex(request, id_pedido_ex, cod_experto):
  if request.method == 'GET':
    pedido = Pedido_Extra.objects.get(id=id_pedido_ex)
    articulo = Articulo.objects.get(pk=cod_experto)
    articulo.stock -= pedido.cantidad_ex
    articulo.total_pedido += pedido.cantidad_ex
    articulo.save()
    pedido.estado_ex = 'entregado'
    pedido.fecha_entrega_ex = datetime.date.today()
    pedido.save()
    return HttpResponseRedirect('/solicitar/pedidos-extra/')

@login_required
def Completar(request, id_especialidad):
   if request.method == 'GET':
    especialidad = Especialidad.objects.get(id=id_especialidad)
    pedido = Pedido.objects.filter(especialidad=especialidad).update(cantidad=0, estado="", fecha_pedido=None, fecha_entrega=None)
    articulo = Articulo.objects.all().update(total_pedido=0)
    especialidad.estadistica = 0
    especialidad.estado = "completado"
    especialidad.save()
    return HttpResponseRedirect('/solicitar/home/')

from reportlab.pdfgen import canvas
from io import BytesIO
from django.views.generic import View
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter,A4,A5, A3, A2
from reportlab.platypus import (BaseDocTemplate, Frame, Paragraph, NextPageTemplate, PageBreak, PageTemplate)
from reportlab.platypus.tables import Table, TableStyle
import datetime
mylist = []
today = datetime.date.today()
mylist.append(today)


class ReportePedidosPDF(View): 

    def cabecera(self,pdf, id_especialidad):
        especialidad = Especialidad.objects.get(id=id_especialidad)
        #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica", 16)
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(370, 1125, u"REPORTE CAE")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(330, 1100, u"PEDIDO POR ESPECIALIDAD")
        pdf.setFont("Helvetica", 10)
        pdf.drawString(625, 1000, u"FECHA: " + str(datetime.date.today()))
        pdf.setFont("Helvetica", 10)
        pdf.drawString(100, 1000, u"Solicitado por: " + str(especialidad.encargado.nombre))


    def tabla(self,pdf,y, id_especialidad):
        especialidad = Especialidad.objects.get(id=id_especialidad)
        #Creamos una tupla de encabezados para neustra tabla
        encabezados = ('Especialidad', 'Codigo Experto', 'Nombre Articulo', 'Cantidad', 'Total')
        #Creamos una lista de tuplas que van a contener a las personas
        detalles = [(pedido.especialidad.nombre, pedido.articulo.cod_experto, pedido.articulo.nombre, pedido.cantidad, pedido.articulo.total_pedido) for pedido in Pedido.objects.filter(especialidad=especialidad)]
        #Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezados] + detalles, colWidths=[5 * cm, 5 * cm, 8 * cm, 2 * cm])
        #Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
            [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(3,0),'CENTER'),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]
        ))
        #Establecemos el tamaño de la hoja que ocupará la tabla 
        detalle_orden.wrapOn(pdf, 2000, 1500)
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 100, 400)


    def get(self, request, id_especialidad, *args, **kwargs):
        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer, pagesize = A3)
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf, id_especialidad)
        y = 900
        self.tabla(pdf, y, id_especialidad)
        #Con show page hacemos un corte de página para pasar a la siguiente
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response


from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle, TA_CENTER
from reportlab.lib.units import inch, mm
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, SimpleDocTemplate, Spacer
 
########################################################################
class Test(object):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.width, self.height = letter
        self.styles = getSampleStyleSheet()
 
    #----------------------------------------------------------------------
    def coord(self, x, y, unit=1):
        """
        http://stackoverflow.com/questions/4726011/wrap-text-in-a-table-reportlab
        Helper class to help position flowables in Canvas objects
        """
        x, y = x * unit, self.height -  y * unit
        return x, y
 
    #----------------------------------------------------------------------
    def run(self):
        """
        Run the report
        """
        self.doc = SimpleDocTemplate("test.pdf")
        self.story = [Spacer(1, 2.5*inch)]
        self.createLineItems()
 
        self.doc.build(self.story, onFirstPage=self.createDocument)
        print "finished!"
 
    #----------------------------------------------------------------------
    def createDocument(self, canvas, doc):
        """
        Create the document
        """
        self.c = canvas
        normal = self.styles["Normal"]
 
        header_text = "<b>This is a test header</b>"
        p = Paragraph(header_text, normal)
        p.wrapOn(self.c, self.width, self.height)
        p.drawOn(self.c, *self.coord(100, 12, mm))
 
        ptext = """Lorem ipsum dolor sit amet, consectetur adipisicing elit,
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
        nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
        reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
        pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
        culpa qui officia deserunt mollit anim id est laborum."""
 
        p = Paragraph(ptext, style=normal)
        p.wrapOn(self.c, self.width-50, self.height)
        p.drawOn(self.c, 30, 700)
 
        ptext = """
        At vero eos et accusamus et iusto odio dignissimos ducimus qui 
        blanditiis praesentium voluptatum deleniti atque corrupti quos dolores 
        et quas molestias excepturi sint occaecati cupiditate non provident, 
        similique sunt in culpa qui officia deserunt mollitia animi, id est laborum
        et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. 
        Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit
        quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est,
        omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut 
        rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et 
        molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus,
        ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis
        doloribus asperiores repellat.
        """
        p = Paragraph(ptext, style=normal)
        p.wrapOn(self.c, self.width-50, self.height)
        p.drawOn(self.c, 30, 600)
 
    #----------------------------------------------------------------------
    def createLineItems(self):
        """
        Create the line items
        """
        text_data = ["Line", "DOS", "Procedure<br/>/Modifier",
                     "Description", "Units", "Billed<br/>Charges",
                     "Type1<br/>Reductions", "Type2<br/>Reductions",
                     "Type3<br/>Reductions", "Allowance",
                     "Qualify<br/>Code"]
        d = []
        font_size = 8
        centered = ParagraphStyle(name="centered", alignment=TA_CENTER)
        for text in text_data:
            ptext = "<font size=%s><b>%s</b></font>" % (font_size, text)
            p = Paragraph(ptext, centered)
            d.append(p)
 
        data = [d]
 
        line_num = 1
 
        formatted_line_data = []
 
        for x in range(200):
            line_data = [str(line_num), "04/12/2013", "73090", 
                         "Test Reflexes", "1", "131.00", "0.00", 
                         "0.00", "0.00", "0.00", "1234"]
 
            for item in line_data:
                ptext = "<font size=%s>%s</font>" % (font_size-1, item)
                p = Paragraph(ptext, centered)
                formatted_line_data.append(p)
            data.append(formatted_line_data)
            formatted_line_data = []
            line_num += 1
 
        table = Table(data, colWidths=[20, 40, 45, 120, 30, 40, 
                                       50, 50, 50, 50, 30])
 
        self.story.append(table)
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    t = Test()
    t.run()



from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
 
class CaseInsensitiveModelBackend(ModelBackend):
  def authenticate(self, username=None, password=None):
    try:
      user = User.objects.get(username__iexact=username)
      if user.check_password(password):
        return user
      return None
    except User.DoesNotExist:
      return None