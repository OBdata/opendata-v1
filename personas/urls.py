from django.urls import path
from .views import *

urlpatterns = [
    path('', ingresar, name='ingresar'),
    path('salir/', salir, name='salir'),
    path('cambiar_clave/', nueva_constrasena, name='contrasena'),
    path('actualizar_clave/', cambiar_contrasena, name='actualizar_clave'),
    path('olvide_contrasena/', olvide_contresena, name='olvide_contrasena')
]