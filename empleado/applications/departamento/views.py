from django.http import HttpResponse
from django.shortcuts import render

# Crear aplicacion de registro. Y como el departamento necesita un 
# empleado encargado. Utilizaremos FormView.

from django.views.generic import FormView, ListView
from .forms import NewDepartamentoForm
from applications.empleados.models import Empleado
from .models import Departamento
# Create your views here.

class DepartamentoListView(ListView):
    template_name = "departamento/lista.html"
    context_object_name = "departamentos"
    model = Departamento

    

class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'

    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        print('*********Estamos en el form_valid**********')

        # Asignacion de la varibale departamento
        depa = Departamento(
            name = form.cleaned_data['departamento'],
            shor_name = form.cleaned_data['shor_name']
        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']

        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job = '1',
            departamento = depa
        )

        return super(NewDepartamentoView,self).form_valid(form)
