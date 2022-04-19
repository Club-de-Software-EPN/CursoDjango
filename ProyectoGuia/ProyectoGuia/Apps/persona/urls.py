from django.urls import path
from . import views

urlpatterns = [
    # 'path', 'vista', nombre
    path('estudiantes', views.estudiantes, name='estudiantes'),
    path('estudiantesFacultad', views.estudiantesFacultad, name='estudiantesFacultad'),
    path('listaEstudiantes', views.ListarEstudiantes.as_view(), name='listaEstudiantes'),
    path('listaEstudiantesNombre', views.ListarEstudiantesBusqueda.as_view(), name='listaEstudiantesNombre'),
    path('listaEstudiantesHabilidad', views.ListarEstudiantesHabilidades.as_view(), name='listaEstudiantesHabilidad'),
    path('detailEstudiante/<pk>', views.EstudiantesDetailView.as_view(),),
    #Facultad
    path('facultad/<str:facultad>',views.ListarEstudiantesPorFacultad.as_view(), name='listaEstudiantesFacultad'),

    ]

