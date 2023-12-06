"""Parcial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from futbol import views as ap1
import futbol.urls as api
# Se configuran las url de la api 
# y las url de las páginas de html.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(api)),
    path('api-aut',include('rest_framework.urls')),
    path('inicio/',ap1.index,name="home"),
    path('registro/',ap1.reg_user,name='registro'),
    path('login/',ap1.iniciar_sesion,name="login"),
    path('logout/',ap1.cerrar_sesion,name='logout'),
    path('add_equi/',ap1.add_equi,name='add_equi'),
    path('equipos/',ap1.list_equi,name="equipos"),
    path('add_jug/',ap1.add_jug,name='add_jug'),
    path('jugadores/',ap1.list_jug,name='jugadores'),
    path('add_notic/',ap1.add_notic,name='add_notic'),
    path('noticias/',ap1.list_notic,name='noticias'),
    path('sin_permiso/',ap1.sin_permiso,name='sin_permiso'),
]
