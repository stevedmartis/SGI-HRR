from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url
from .import views
from django.contrib.auth.views import login_required

from Pedidoapp.views import home, Pedido_Edit, add,  Aprobado, UroloList, EdaList

admin.autodiscover()

urlpatterns = [

url(r'^home/$', login_required(home), name="home"),

url(r'^lista_uro/$', UroloList, name="listar_urologia"),
url(r'^lista_eda/$', EdaList, name="listar_eda"),


url(r'^confirmar/(?P<id_pedido>\d+)/$', login_required(Aprobado), name='aprobar_pedido'),
#url(r'^ingresar/$', login_required(add), name="ingresar_cant"),
url(r'^ingresar/(?P<id_pedido>\d+)/$', Pedido_Edit, name="ingresar_cant"),







]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#(?P<cod_experto>\d+)