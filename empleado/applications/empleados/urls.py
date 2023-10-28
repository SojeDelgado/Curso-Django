from django.urls import path, include
from applications.home. views import IndexView

from . import views

app_name = 'empleado_app'

urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    path(
        'listar-todo-empleados/', 
        views.ListAllEmpleados.as_view(),
        name='empleados_all'
    ),

    # shor_name es el parametro que se va a recibir
    path(
        'list-by-area/<shor_name>/', 
        views.ListByAreaEmpleado.as_view(), 
        name="empleados_area"),

    path(
        'lista-empleados-admin/', 
        views.ListaEmpleadosAdmin.as_view(), 
        name="empleados_admin"),

    path('listar-por-trabajo/<job>/', views.ListByJobEmpleado.as_view()),
    path('buscar-empleado/', views.ListEmpleadosByWord.as_view()),
    path('habilidades/<int:empleado_id>/', views.ListHabilidadesEmpleado.as_view()),
    path(
            'ver-empleado/<pk>/', 
            views.EmpleadoDetailView.as_view(),
            name='empleado_detail'
        ),
    path(
        'add-empleado/', 
        views.EmpleadoCreateView.as_view(), 
         name="empleado_add"),

    # La etiqueta name hará referencia a la URL  
    path('success/',views.SuccessView.as_view(),name='correcto'),
    path(
        'update-empleado/<pk>/', 
        views.EmpleadoUpdateView.as_view(),
        name='modificar_empleado'
    ),
    path(
        'delete-empleado/<pk>/', 
        views.EmpleadoDeleteView.as_view(),
        name='eliminar_empleado'
    ),
]
