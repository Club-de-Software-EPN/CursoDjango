from django.contrib import admin
from django.urls import path
from . import views
app_name = 'denuncias'
urlpatterns = [
    path('', views.CrearDenuncia.as_view(), name='index'),
    path('success', views.SuccessView.as_view(), name='success')
]

