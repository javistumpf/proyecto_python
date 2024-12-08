"""
URL configuration for Proyecto_Javier project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.inicio),

    # URLs para candidatos
    path('candidato/perfil/', views.perfil_candidato),
    path('candidato/busquedas/', views.busquedas_activas),
    path('candidato/postulaciones/', views.mis_postulaciones),
    path('candidato/empresas/', views.empresas),

    # URLs para empresas
    path('empresa/perfil/', views.perfil_empresa),
    path('empresa/busquedas/', views.mis_busquedas),
    path('empresa/candidatos/', views.candidatos)
]
