from django.urls import path
from .views import *

urlpatterns = [
    path('', visualizar_data, name='visualizar_data'),
    path('descarga/', descargar_data, name='descargar_data'),
]