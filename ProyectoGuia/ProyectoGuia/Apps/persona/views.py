from django.shortcuts import render
from django.views.generic import (ListView)
from .models import Estudiante
# Create your views here.
# 1. Lista de todos los estudiantes
class ListarEstudiantes(ListView):
    # configurar modelo de la vista
    model = Estudiante
    # Parámetro específico para las vistas
    context_object_name = 'listaEstudiantes'
    # definir el template de salida
    template_name = 'persona/listaEstudiantes.html'

# 2

# 3

# 4