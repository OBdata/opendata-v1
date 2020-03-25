from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='listado'),
    path('nueva/', nueva_actividad, name='nueva_actividad'),
    path('agregar_nueva/', agregar_nueva, name='agregar_nueva'),
    path('<str:id>/', ver_actividad, name='ver'),
    path('<str:id>/<str:success>', ver_actividad, name='ver'),
    path('<str:id>/actualizar_asistencia/', actualizar_asistencia, name='asistencia'),
    path('<str:id>/nuevas_invitaciones/', nuevas_invitaciones, name='nuevas_invitaciones'),
    path('<str:id>/editar_informacion/', editar_informacion, name='editar_informacion'),
    path('<str:id>/guardar_nota/', guardar_anotacion, name='guardar_anotacion')
]