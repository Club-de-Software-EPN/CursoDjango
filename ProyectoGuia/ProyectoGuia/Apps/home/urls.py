from django.urls import path
from . import views

urlpatterns = [
    # 'path', 'vista', nombre
    path('', views.index, name='index'),
    path('prueba', views.prueba, name='prueba'),
    path('add/', views.PruebaCreateView.as_view()),
    ]

