from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def historia(request):
    return render(request, 'historia.html')

def aficiones(request):
    return render(request, 'aficiones.html')

def educacion(request):
    return render(request, 'educacion.html')