from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url
from .import views
from django.contrib.auth.views import login_required

from Pedidoapp.views import home,  ArticuloListView, Pedido_Edit, add,  Aprobado


admin.autodiscover()

urlpatterns = [

url(r'^home/$', login_required(home), name="home"),
url(r'^lista/(?P<id>\d+)/$', ArticuloListView, name="listar_esp"),
url(r'^confirmar/(?P<id_pedido>\d+)/$', login_required(Aprobado), name='aprobar_pedido'),
#url(r'^ingresar/$', login_required(add), name="ingresar_cant"),
url(r'^ingresar/(?P<id_pedido>\d+)/$', Pedido_Edit, name="ingresar_cant"),







]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#(?P<cod_experto>\d+)