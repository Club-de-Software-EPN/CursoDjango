from django.shortcuts import render
from django.views.generic import (TemplateView, CreateView)
from .models import Denuncia
from .forms import FormDenuncia
from django.urls import reverse_lazy
# Create your views here.

class SuccessView(TemplateView):
    template_name = 'success.html'

class CrearDenuncia(CreateView):
    model = Denuncia
    template_name = 'index.html'
    #fields = ['titulo', 'tema', 'codigo', 'acusado', 'mensaje']
    form_class = FormDenuncia
    success_url = reverse_lazy('denuncias:success')

