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

url(r'^lista_uro/$', (UroloList), name="listar_urologia"),
url(r'^lista_eda/$', (EdaList), name="listar_eda"),
url(r'^lista_fibro/$', (FibroList), name="listar_fibro"),
url(r'^lista_pbmenor/$', (PabMenorList), name="listar_pabmenor"),
url(r'^lista_curaav/$', (CuracionAvList), name="listar_curacionav"),
url(r'^lista_cli/$', (ClinicaList), name="listar_clinicat"),
url(r'^lista_cardio/$', (CardioList), name="listar_cardio"),
url(r'^lista_otri/$', (OtorrinoList), name="listar_otorrino"),
url(r'^lista_oftal/$', (OftalList), name="listar_oftalmolo"),
url(r'^lista_plum/$', (PlumbarList), name="listar_plumbar"),
url(r'^lista_egg/$', (EggList), name="listar_egg"),
url(r'^lista_tmt/$', (TmtList), name="listar_tmt"),
url(r'^lista_neuro/$', (NeuroList), name="listar_neuro"),
url(r'^lista_dan/$', (SaladanList), name="listar_sala"),
url(r'^lista_recu/$', (RecuperaList), name="listar_recuperacion"),
url(r'^lista_derma/$', (DermaList), name="listar_derma"),
url(r'^lista_bronco/$', (BroncoList), name="listar_bronco"),
url(r'^lista_salaproc/$', (SalainfoProcList), name="listar_salainfoproc"),
url(r'^lista_admis/$', (AdmisionList), name="listar_admision"),
url(r'^lista_aseoproc/$', (AseoProcList), name="listar_aseoproc"),
url(r'^lista_taco/$', (PoliTacoList), name="listar_taco"), 
url(r'^lista_diab/$', (DiabetesList), name="listar_diabetes"),
url(r'^lista_vih/$', (VihList), name="listar_vih"),
url(r'^lista_hepa/$', (HepatiList), name="listar_hepa"),
url(r'^lista:infocons/$', (SalainfoConsList), name="listar_salainfocons"),
url(r'^lista_adminscon/$', (AdmisionConsList), name="listar_admisioncons"),
url(r'^lista_prepaa/$', (PrepaListA), name="listar_prepa_a"),
url(r'^lista_prepab/$', (PrepaListB), name="listar_prepa_b"),
url(r'^lista_estenf/$', (EstacionEnfList), name="listar_estacionenf"),
url(r'^lista_drcast/$', (DraCasList), name="listar_dracas"),

url(r'^confirmar/(?P<id_pedido>\d+)/$', login_required(Aprobado), name='aprobar_pedido'),
#url(r'^ingresar/$', login_required(add), name="ingresar_cant"),
url(r'^ingresar/(?P<id_pedido>\d+)/$', Pedido_Edit, name="ingresar_cant"),







]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#(?P<cod_experto>\d+)