from django.db import models

# Create your models here.

# Creacion de tabla prueba
class Prueba(models.Model):

    # Definir el campo titulo
    titulo = models.CharField(max_length=30)

    # Definir el campo subtitulo
    subtitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo + ' ' + self.subtitulo