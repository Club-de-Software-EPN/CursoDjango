from django.shortcuts import render
from .models import Publicaciones
pub = Publicaciones()
def publicaciones(request):

    listaPublicaciones = pub.getTodasPublicaciones()
    context = {'publicaciones': listaPublicaciones}
    return render(request,'publicaciones.html', context)

def crearPublicacion(request):
    if request.method == 'POST':
        print('Me esta llegando info')
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        pub.crearPublicacion(titulo, descripcion)

    return render(request, 'crearPublicacion.html')

# Renderizar vistas estáticas
def index(request):
    return render(request,'index.html')

def historia(request):
    return render(request, 'historia.html')

def aficiones(request):
    return render(request, 'aficiones.html')

def educacion(request):
    return render(request, 'educacion.html')