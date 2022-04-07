from django.urls import path
from . import views

urlpatterns = [
    # 'path', 'vista', nombre
    path('', views.index, name='index'),
    path('historia', views.historia, name='historia'),
    path('educacion', views.educacion, name='educacion'),
    path('aficiones', views.aficiones, name='aficiones'),
    path('publicaciones', views.publicaciones, name='publicaciones')
]