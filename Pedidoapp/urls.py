from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url
from .import views
from django.contrib.auth.views import login_required


from Pedidoapp.views import home, Cant_ingresar, ListAll, ListEspeci, Cant_update, Update_stock, PedidoExtra
from Pedidoapp.views import ExtraView, Cant_upex, Update_stockex, ReportePedidosPDF, ReporteTotalPDF, ReporteTotalFarmacia, ReporteTotalEcono 
from Pedidoapp.views import Reset, Acces_open, Acces_close, VistaAsigna, Asigna, DeletePedido, IngresarExtra, VerTodo, Entregar, Ped_entregados, ListAllEnt, Esp_total

admin.autodiscover()

urlpatterns = [

url(r'^home/$', login_required(home), name="home"),
url(r'^pedidos-entregados/$', login_required(Ped_entregados), name="ped_entre"),
url(r'^especialidades/$', login_required(Esp_total), name="esp_total"),


url(r'^lista_super/(?P<id_especialidad>\d+)/$', login_required(ListAll), name='lita_todo'),
url(r'^lista_super_entregados/(?P<id_especialidad>\d+)/$', login_required(ListAllEnt), name='lita_todo_entre'),

url(r'^lista_active/(?P<id_especialidad>\d+)/$', login_required(ListEspeci), name='lita_active'),

url(r'^ingresar/(?P<id_pedido>\d+)/(?P<id_especialidad>\d+)/$', Cant_ingresar, name="cant_ingresar"),
url(r'^modificar/(?P<id_pedido>\d+)/(?P<id_especialidad>\d+)/$', Cant_update, name="cant_update"),
url(r'^entregar/(?P<id_pedido>\d+)/(?P<id_especialidad>\d+)/(?P<cod_experto>[^/]+)/$', Update_stock, name="entregado"),
url(r'^entregar/(?P<id_especialidad>\d+)/$', Entregar, name="entregar"),

url(r'^pedido-extra/(?P<id_especialidad>\d+)/$', PedidoExtra , name='pedido_extra'),
url(r'^pedidos-extra/$', ExtraView , name='ped_ex'),
url(r'^modificar/(?P<id_pedido_ex>\d+)/$', Cant_upex, name="cant_extra"),
url(r'^ingresa-extra/(?P<id_especialidad>\d+)/(?P<cod_experto>[^/]+)/$', IngresarExtra, name="ingresa_extra"),
url(r'^entregar/(?P<id_pedido_ex>\d+)/(?P<cod_experto>[^/]+)/$', Update_stockex, name="entregado_ex"),

url(r'^reset-estadis/$', login_required(Reset), name="reset"),
url(r'^acces-open/$', login_required(Acces_open), name="open"),
url(r'^acces-close/$', login_required(Acces_close), name="close"),

url(r'^reporte_pedidos_pdf/(?P<id_especialidad>\d+)/$', login_required(ReportePedidosPDF.as_view()), name="reporte_pedidos_pdf"),
url(r'^reporte_insumo_pdf/$', login_required(ReporteTotalPDF.as_view()), name="reporte_insumo_pdf"),
url(r'^reporte_farmacia_pdf/$', login_required(ReporteTotalFarmacia.as_view()), name="reporte_farma_pdf"),
url(r'^reporte_economato_pdf/$', login_required(ReporteTotalEcono.as_view()), name="reporte_econo_pdf"),

url(r'^asignar-nuevo/(?P<id_especialidad>\d+)/$', login_required(VistaAsigna), name='vista_asigna'),
url(r'^vista-art-extra/(?P<id_especialidad>\d+)/$', login_required(VistaAsigna), name="vista_extra"),
url(r'^btn-asigna/(?P<id_especialidad>\d+)/(?P<cod_experto>[^/]+)/$', Asigna, name="asignar"),
url(r'^delete-pedido/(?P<id_pedido>\d+)/(?P<id_especialidad>\d+)/(?P<cod_experto>[^/]+)/$', DeletePedido, name="confirm_delete_pedido"),
url(r'^ver_todo/(?P<id_especialidad>\d+)/$', login_required(VerTodo), name='ver_todo'),



]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)      
