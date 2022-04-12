from django.urls import path
from . import views

urlpatterns = [
    # 'path', 'vista', nombre
    path('listaEstudiantes', views.ListarEstudiantes.as_view(), name='listaEstudiantes')
    ]

