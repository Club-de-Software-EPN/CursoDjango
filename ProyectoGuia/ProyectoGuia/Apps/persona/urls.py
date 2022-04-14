from django.urls import path
from . import views

urlpatterns = [
    # 'path', 'vista', nombre
    path('estudiantes', views.estudiantes, name='estudiantes'),
    path('listaEstudiantes', views.ListarEstudiantes.as_view(), name='listaEstudiantes'),
    path('listaEstudiantesFacultad/<facultad>', views.ListarEstudiantesPorFacultad.as_view(), name='listaEstudiantesFacultad'),
    ]

