from django.shortcuts import render
from django.views.generic import CreateView
from .models import Prueba
from .forms import PruebaForm
# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def prueba(request):
    return render(request, 'prueba.html')

class PruebaCreateView(CreateView):
    template_name = 'home/add.html'
    model = Prueba
    #fields = ['titulo', 'subtitulo', 'cantidad']
    form_class = PruebaForm
    success_url = '/'
