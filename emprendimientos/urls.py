from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('nuevo/', nuevo_emprendimiento, name='nuevo-emp'),
    path('guardar/', guardar_nuevo_emprendimiento, name='guardar-nuevo-emp'),
    path('mi_emprendimiento/', mi_emprendimiento, name="mi-empr")
]