"""bodega URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from Pedidoapp import urls
from django.contrib.auth.views import login, logout_then_login
from django.contrib.auth.decorators import login_required
from django.conf import settings


admin.autodiscover()


urlpatterns = [
    # Examples:
    url(r'^solicitar/', include(urls, namespace="usuario")),
  #  url(r'^home_user/$', login_required(Pedidoapp.views.homeuser), name="homeuser"),
    #url(r'^add/$', login_required(add), name=""), 

    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli /',include('grappelli.urls')),
    url(r'^grappelli /',include('grappelli.urls')),
    url(r'^$', login, {'template_name':'login.html'}, name="login"),
    url(r'^check_login/', (auth_views.check_login), name="check_login"),
    url(r'^logout/', logout_then_login, name="logout"),


    

]


