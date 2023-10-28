from django.db import models
from ckeditor.fields import RichTextField

# Importar modelo departamento
from applications.departamento.models import Departamento

# Create your models here.


# Tabla Habilidades
class Habilidades(models.Model):
    """ Modelo para tabla habilidades """

    # Campos de la tabla habilidades
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'

    def __str__(self):
        return str(self.id) + '- ' + self.habilidad


# Tabla Empleado
class Empleado(models.Model):
    """ Modelo para tabla empleado """

    # Tipos de trabajos
    job_choices = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro'),
    )

    # Campos de la tabla empleado
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)

    full_name = models.CharField(
        'Nombre Completo',
        max_length=120,
        blank=True
    )

    job = models.CharField('trabajo', max_length=1, choices=job_choices)

    # Foreign key
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    # Many to Many
    habilidades = models.ManyToManyField(Habilidades)

    # ckeditor
    hoja_vida = RichTextField(blank=True)

    image = models.ImageField(upload_to='empleados', blank=True, null=True)

    def __str__(self):
        return str(self.id) + '- ' + self.first_name + ' ' + self.last_name