from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.

#Registrar modelo departamento al administrador
admin.site.register(Habilidades)


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
        'id',
    )

    # declarando full name
    def full_name(self, obj):
        # obj es el objeto que se esta iterando
        return obj.first_name + ' ' + obj.last_name

    # Buscar por nombre
    search_fields = ('first_name',)

    # Filtrar por trabajo
    list_filter = ('departamento', 'job', 'habilidades', )
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)
