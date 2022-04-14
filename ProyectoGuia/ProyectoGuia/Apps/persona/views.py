from django.shortcuts import render
from django.views.generic import (ListView)
from .models import Estudiante

# Create your views here.

def estudiantes(request):
    return render(request, 'persona/estudiantes.html')

#   Lists View

# 1. Lista de todos los estudiantes
class ListarEstudiantes(ListView):
    # configurar modelo de la vista
    model = Estudiante
    # Parámetro específico para las vistas
    context_object_name = 'listaEstudiantes'
    # definir el template de salida
    template_name = 'persona/listaEstudiantes.html'

# 2 Listar todos los estudiantes por Facultad, filtros con el ORM
class ListarEstudiantesPorFacultad(ListView):
    #modelo
    model = Estudiante
    # template
    template_name = 'persona/listaEstudiantesFacultad.html'
    # Tomar nombre corto de facultad desde la url
    def get_queryset(self):
        # Recoger el parámetro GET desde la url
        facultadBusqueda = self.kwargs['facultad']
        # Select Estudiante -> Atributo Facultad -> Del atributo facultad sacar el nombre corto
        # -> Nombre corto en url == Nombre corto facultad estudiantes
        # Usaremos el operador __
        listaResultados = Estudiante.objects.filter(facultad__nombreCorto=facultadBusqueda)
        return listaResultados

# 3 Listar por búsqueda de nombre

# 4 Listar Habilidades del estudiantes (m2m)

#   CRUD views

