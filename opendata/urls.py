"""opendata URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', inicio),
    path('actividades/', include(('actividades.urls', 'actividades'), namespace='actividades')),
    path('emprendimientos/', include(('emprendimientos.urls', 'emprendimientos'), namespace='emprendimientos')),
    path('ficha/', include(('ficha.urls', 'ficha'), namespace='ficha')),
    path('personas/', include(('personas.urls', 'personas')), name='persona'),
    path('personas/', include('django.contrib.auth.urls')),
    path('reporte/', include(('reporte.urls', 'reporte')), name='reporte'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
