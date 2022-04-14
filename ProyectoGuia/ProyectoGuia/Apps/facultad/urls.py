from django.urls import path
from . import views

urlpatterns = [
    # 'path', 'vista', nombre
    path('facultades', views.facultades, name='facultades'),

    ]
