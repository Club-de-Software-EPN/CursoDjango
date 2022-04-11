from django.db import models

# Create your models here.

class Facultad(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    nombreCorto = models.CharField('NombreCorto', max_length=10, blank=True, unique=True)
    activo = models.BooleanField('FacultadActiva', default=True)
    
    class Meta:
        verbose_name='Facultad'
        verbose_name_plural='Nuestras Facultades'
        # modifiar el orden de presentación
        ordering = ['nombre']
        # Restricciones
        unique_together = ('nombre', 'nombreCorto')

    # str -> permite modificar el nombre a mostrarse en la
    def __str__(self):
        return self.nombre + '-' + self.nombreCorto