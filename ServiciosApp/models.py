from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to= 'servicios')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    #nombre que tendra el servicio en la BBDD
    class Meta():
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'

    #retorna el titulo del servicio
    def __str__(self):
        return self.titulo
