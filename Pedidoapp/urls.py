from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url
from .import views
from django.contrib.auth.views import login_required

from Pedidoapp.views import home, Pedido_Edit, add,  Aprobado, UroloList, CardioList, EdaList, FibroList, PabMenorList, CuracionAvList, ClinicaList, OtorrinoList, OftalList, PlumbarList, EggList, TmtList,NeuroList, SaladanList, RecuperaList, DermaList, BroncoList, SalainfoProcList, AdmisionList, AseoProcList, PoliTacoList, DiabetesList, VihList, HepatiList, SalainfoConsList, AdmisionConsList, PrepaListA, PrepaListB, EstacionEnfList, DraCasList

admin.autodiscover()

urlpatterns = [

url(r'^home/$', login_required(home), name="home"),

url(r'^lista/$', (UroloList), name="listar_urologia"),
url(r'^lista/$', (EdaList), name="listar_eda"),
url(r'^lista/$', (FibroList), name="listar_fibro"),
url(r'^lista/$', (PabMenorList), name="listar_pabmenor"),
url(r'^lista/$', (CuracionAvList), name="listar_curacionav"),
url(r'^lista/$', (ClinicaList), name="listar_clinicat"),
url(r'^lista/$', (CardioList), name="listar_cardio"),
url(r'^lista/$', (OtorrinoList), name="listar_otorrino"),
url(r'^lista/$', (OftalList), name="listar_oftalmolo"),
url(r'^lista/$', (PlumbarList), name="listar_plumbar"),
url(r'^lista/$', (EggList), name="listar_egg"),
url(r'^lista/$', (TmtList), name="listar_tmt"),
url(r'^lista/$', (NeuroList), name="listar_neuro"),
url(r'^lista/$', (SaladanList), name="listar_sala"),
url(r'^lista/$', (RecuperaList), name="listar_recuperacion"),
url(r'^lista/$', (DermaList), name="listar_derma"),
url(r'^lista/$', (BroncoList), name="listar_bronco"),
url(r'^lista/$', (SalainfoProcList), name="listar_salainfoproc"),
url(r'^lista/$', (AdmisionList), name="listar_admision"),
url(r'^lista/$', (AseoProcList), name="listar_aseoproc"),
url(r'^lista/$', (PoliTacoList), name="listar_taco"), 
url(r'^lista/$', (DiabetesList), name="listar_diabetes"),
url(r'^lista/$', (VihList), name="listar_vih"),
url(r'^lista/$', (HepatiList), name="listar_hepa"),
url(r'^lista/$', (SalainfoConsList), name="listar_salainfocons"),
url(r'^lista/$', (AdmisionConsList), name="listar_admisioncons"),
url(r'^lista/$', (PrepaListA), name="listar_prepa_a"),
url(r'^lista/$', (PrepaListB), name="listar_prepa_b"),
url(r'^lista/$', (EstacionEnfList), name="listar_estacionenf"),
url(r'^lista/$', (DraCasList), name="listar_dracas"),

url(r'^confirmar/(?P<id_pedido>\d+)/$', login_required(Aprobado), name='aprobar_pedido'),
#url(r'^ingresar/$', login_required(add), name="ingresar_cant"),
url(r'^ingresar/(?P<id_pedido>\d+)/$', Pedido_Edit, name="ingresar_cant"),







]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#(?P<cod_experto>\d+)