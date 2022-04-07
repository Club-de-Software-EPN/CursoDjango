from django.shortcuts import render
from .models import Publicaciones

def publicaciones(request):
    pub = Publicaciones()
    listaPublicaciones = pub.getTodasPublicaciones()
    context = {'publicaciones': listaPublicaciones}
    return render(request,'publicaciones.html', context)

# Renderizar vistas estáticas
def index(request):
    return render(request,'index.html')

def historia(request):
    return render(request, 'historia.html')

def aficiones(request):
    return render(request, 'aficiones.html')

def educacion(request):
    return render(request, 'educacion.html')