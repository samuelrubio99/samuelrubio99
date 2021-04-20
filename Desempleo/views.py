from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Usuarios, Nivel_estudio, Formacion, Representante_empresa, Empresa, Forma_juridica, Usuario_desempeno, Seleccion, Actividad_economica, Empresa_actividad, Area_desempeno
from rest_framework import viewsets
from .Serializers import UsuariosSerializer, Nivel_estudioSerializer, FormacionSerializer, Representante_empresaSerializer, EmpresaSerializer, Forma_juridicaSerializer, Usuario_desempenoSerializer,Area_desempenoSerializer, SeleccionSerializer, Actividad_economicaSerializer, Empresa_actividadSerializer


from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

# Create your views here.
#class HomePageView(TemplateView): 
 #   template_name = 'home.html'

#class AboutPageView(TemplateView): 
 #   template_name = 'about.html'
    
class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer


class Nivel_estudioViewSet(viewsets.ModelViewSet):
    queryset = Nivel_estudio.objects.all()
    serializer_class = Nivel_estudioSerializer

class FormacionViewSet(viewsets.ModelViewSet):
    queryset = Formacion.objects.all()
    serializer_class = FormacionSerializer


class Representante_empresaViewSet(viewsets.ModelViewSet):
    queryset = Representante_empresa.objects.all()
    serializer_class = Representante_empresaSerializer


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class Forma_juridicaViewSet(viewsets.ModelViewSet):
    queryset = Forma_juridica.objects.all()
    serializer_class = Forma_juridicaSerializer

class Usuario_desempenoViewSet(viewsets.ModelViewSet):
    queryset = Usuario_desempeno.objects.all()
    serializer_class = Usuario_desempenoSerializer

class Area_desempenoViewSet(viewsets.ModelViewSet):
    queryset = Area_desempeno.objects.all()
    serializer_class = Area_desempenoSerializer

class SeleccionViewSet(viewsets.ModelViewSet):
    queryset = Seleccion.objects.all()
    serializer_class = SeleccionSerializer

class Actividad_economicaViewSet(viewsets.ModelViewSet):
    queryset = Actividad_economica.objects.all()
    serializer_class = Actividad_economicaSerializer

class Empresa_actividadViewSet(viewsets.ModelViewSet):
    queryset = Empresa_actividad.objects.all()
    serializer_class = Empresa_actividadSerializer
