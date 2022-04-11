from django.db import models
from ProyectoGuia.Apps.facultad.models import Facultad
# Create your models here.

class Estudiante(models.Model):
    tiposEstudiantes = (
        ('0', 'Nivelación'),
        ('1', 'Pregrado'),
        ('2', 'Maestría'),
        ('3', 'Doctorado')
    )
    primerNombre = models.CharField('Nombre', max_length=50)
    apellido = models.CharField('Apellidos', max_length=50)
    tipo = models.CharField('Tipo', max_length=1, choices=tiposEstudiantes)
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)
    
    class Meta:
        #nombre singular
        verbose_name='Estudiante'
        #nombre plural
        verbose_name_plural = 'Estudiantes matriculados'

    def __str__(self):
        return self.primerNombre + ' '+ self.apellido + ' - Facultad: ' +self.facultad.nombreCorto