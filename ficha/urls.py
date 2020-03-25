from django.urls import path
from .views import *

urlpatterns = [
    path('<str:id>', ficha, name='ficha'),
    path('<str:id>/<str:success>', ficha, name='ficha_success'),
    path('<str:id>/nuevo_trabajador/', guardar_nuevo_trabajador, name='nuevo_trabajador'),
    path('<str:id>/nueva_venta/', guardar_nueva_venta, name='nueva_venta'),
    path('<str:id>/nuevo_costo/', guardar_nuevo_costo, name='nuevo_costo'),
    path('<str:id>/nueva_patente/', guardar_nueva_patente, name='nueva_patente'),
    path('<str:id>/nueva_inversion/', guardar_nueva_inversion, name='nueva_inversion'),
    path('<str:id>/nuevo_assesment/', guardar_nuevo_assesment, name='nuevo_assesment'),
    path('guardar_descripcion/', guardar_nueva_descripcion, name='nueva_descripcion'),
    path('guardar_necesidades/', guardar_nuevas_necesidades, name='nuevas_necesidades'),
    path('guardar_desafios/', guardar_nuevos_desafios, name='nuevos_desafios'),
    path('guardar_informacion/', guardar_nueva_informacion, name='nueva_informacion')
]