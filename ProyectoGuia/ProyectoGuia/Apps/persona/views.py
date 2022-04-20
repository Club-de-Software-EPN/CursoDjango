from django.shortcuts import render
from django.views.generic import (ListView, TemplateView, DetailView, CreateView,
                                  UpdateView, DeleteView)
from .models import Estudiante
from django.urls import reverse_lazy
# Create your views here.

def estudiantes(request):
    return render(request, 'persona/estudiantes.html')

def estudiantesFacultad(request):
    return render(request, 'persona/listaFacultadesEstudiantes.html')

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

# 3 Listar por búsqueda de nombre (pasado por get)
class ListarEstudiantesBusqueda(ListView):
    template_name = 'persona/listaEstudiantesBusqueda.html'
    model = Estudiante
    context_object_name = 'estudiantes'

    def get_queryset(self):
        nombre = self.request.GET.get('nombre', '')
        #print('Nombre en back', nombre)
        listaResultados = Estudiante.objects.filter(primerNombre=nombre)

        return listaResultados

# 4 Listar Habilidades del estudiantes (m2m)
class ListarEstudiantesHabilidades(ListView):
    template_name = 'persona/listaEstudiantesHabilidad.html'
    model = Estudiante
    context_object_name = 'habilidades'

    def get_queryset(self):
        estudiante = Estudiante.objects.get(id=2)
        return estudiante.habilidad.all()


#   CRUD views

# Detailed View

class EstudiantesDetailView(DetailView):
    model = Estudiante
    template_name = 'persona/detailEstudiante.html'

    def get_context_data(self, **kwargs):
        # Permite agregar  hacer validaciones previo a mostrar el detalle en el navegador
        context = super(EstudiantesDetailView, self).get_context_data(**kwargs)   # todos los atributos
        context['titulo'] = 'Mejor estudiante'
        context['otroDato'] = 'otro dato'
        return context

# Crear
class SuccesView(TemplateView):
    template_name = 'persona/success.html'

class EstudianteCreateView(CreateView):
    model = Estudiante
    template_name = 'persona/crearEstudiante.html'
    #fields = ('__all__')
    fields = ['primerNombre','apellido','tipo','facultad', 'cartaMotivacion','habilidad']
    success_url = reverse_lazy('persona_app:success')

    def form_valid(self, form):
        # trabajo
        #hacer validaciones, crear parametros sin que se pase desde el html
        # validaciones
        estudiante = form.save()
        estudiante.nombreCompleto = estudiante.primerNombre + ' ' + estudiante.apellido
        estudiante.save()
        return super(EstudianteCreateView, self).form_valid(form)

## Update

## Delete View
class EstudianteDeleteView(DeleteView):
    model = Estudiante
    template_name = 'persona/delete.html'
    success_url = reverse_lazy('persona_app:success')
