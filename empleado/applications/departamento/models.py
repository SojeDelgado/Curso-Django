from django.db import models

# Create your models here.

# Crear tabla departamento
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    shor_name = models.CharField('Nombre Corto', max_length=20)
    anulate = models.BooleanField('Anulado', default=False)

    class Meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural = 'Areas de la empresa'

        # Ordenar por nombre
        ordering = ['name']

        # Validar para evitar un registro similar en name y short_name
        unique_together = ('name', 'shor_name')

    def __str__(self):
        return str(self.id) + '- ' + self.name + ': ' + self.shor_name 