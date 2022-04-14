from django.shortcuts import render
from .models import Facultad
# Create your views here.

def facultades(request):
    return render(request,'facultad/facultades.html')