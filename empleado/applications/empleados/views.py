from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
    )
# models
from .models import Empleado


# forms
from .forms import EmpleadoForm

class InicioView(TemplateView):
    """ Vista que carga la pagina de inicio """
    template_name = 'inicio.html'

    
# Create your views here.
# 1. Lista todos los empleados de la empresa

class ListAllEmpleados(ListView):
    template_name = 'empleado/list_all.html'
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'lista'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        lista = Empleado.objects.filter(
            first_name__icontains=palabra_clave
        )
        return lista
    

class ListaEmpleadosAdmin(ListView):
    template_name = 'empleado/lista_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'lista'
    model = Empleado


# 2. Lista todos los empleados que pertenecen a un area de la empresa

class ListByAreaEmpleado(ListView):
    template_name = 'empleado/list_by_area.html'
    context_object_name = 'empleados'

    # Determinar con que empleo se va a filtrar
    def get_queryset(self):
        area = self.kwargs['shor_name']
        lista = Empleado.objects.filter(
            departamento__shor_name=area
        )
        return lista

# 3. Listar empleados por trabajo

class ListByJobEmpleado(ListView):
    template_name = 'empleado/list_by_job.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        trabajo = self.kwargs['job']
        lista = Empleado.objects.filter(
            job=trabajo
        )
        return lista

# 4. Listar los empleados por palabra clave

class ListEmpleadosByWord(ListView):
    template_name = 'empleado/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        lista = Empleado.objects.filter(
            first_name=palabra_clave
        )
        return lista

# 5. Listar habilidades de un empleado

class ListHabilidadesEmpleado(ListView):
    template_name = 'empleado/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado_id = self.kwargs['empleado_id']
        empleado = Empleado.objects.get(id=empleado_id)
        empleado = Empleado.objects.get(id=3)
        return empleado.habilidades.all()


# Mostrar detalle de un empleado en especifico
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "empleado/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'empleado del mes'
        return context
    
# Template para la redireccion al guardar un empleado    
class SuccessView(TemplateView):
    template_name = "empleado/success.html"    

# Create view
class EmpleadoCreateView(CreateView):
    template_name = "empleado/add.html"
    model = Empleado
    # Parametro necesario en el Create View y la variable predeterminada en form
    form_class = EmpleadoForm

    # Url a donde se redirecciona al guardar la informacion
    # empleados_app es el conjunto de URLS de la aplicación persona
    success_url = reverse_lazy('empleado_app:empleados_admin')

    # Metodo cuando todos los campos ya han sido validados
    def form_valid(self, form):
        # Indicar el full name del empleado cuando ya esten validados los empleados
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


# Clase para modificar datos empleado
class EmpleadoUpdateView(UpdateView):
    template_name = "empleado/update.html"
    model = Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
        
        #'image',
    ]

    # Url a donde se redirecciona al guardar la informacion
    # empleados_app es el conjunto de URLS de la aplicación persona
    success_url = reverse_lazy('empleado_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        return super(EmpleadoUpdateView, self).form_valid(form)
    
    
# Clase para eliminar un empleado
class EmpleadoDeleteView(DeleteView):
    template_name = "empleado/delete.html"
    model = Empleado
    success_url = reverse_lazy('empleado_app:empleados_admin')

    # Metodo para eliminar un empleado
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())