from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Vista de inicio
def inicio(request):
    return HttpResponse("Vista inicio")

# Vistas para candidatos
def perfil_candidato(request):
    return HttpResponse("Vista Mi perfil - Candidato")

def busquedas_activas(request):
    return HttpResponse("Vista Búsquedas activas - Candidato")

def mis_postulaciones(request):
    return HttpResponse("Vista Mis postulaciones - Candidato")

def empresas(request):
    return HttpResponse("Vista Empresas - Candidato")

# Vistas para empresas
def perfil_empresa(request):
    return HttpResponse("Vista Mi perfil - Empresa")

def mis_busquedas(request):
    return HttpResponse("Vista Mis búsquedas - Empresa")

def candidatos(request):
    return HttpResponse("Vista Candidatos - Empresa")