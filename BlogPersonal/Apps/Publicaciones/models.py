from django.db import models
from datetime import date, datetime
# Create your models here.

class Publicaciones(models.Model):
    idPublicacion = models.AutoField(primary_key=True)
    tituloPublicacion = models.CharField(max_length=1020)
    descripcionPublicacion = models.CharField(max_length=5000, default='Descripción no disponible')
    fecha = models.DateField(("Date"), default=date.today)

    def getTodasPublicaciones(self):
        return list(Publicaciones.objects.all())

    def crearPublicacion(self, titulo, descripcion):
        Publicaciones.objects.create(tituloPublicacion=titulo, descripcionPublicacion=descripcion)