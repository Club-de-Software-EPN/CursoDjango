from django.db import models

# Create your models here.

class CodigosEstudiantes(models.Model):
    codigoUnico = models.CharField(max_length=100)

class Denuncia(models.Model):
    titulo = models.CharField(max_length=100)
    tema = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    acusado = models.CharField(max_length=150)
    mensaje = models.CharField(max_length=1500)

