from django.db import models
from personas.models import Persona
from emprendimientos.models import Emprendimiento


class Actividad(models.Model):
    persona = models.ForeignKey(
        'personas.Persona',
        on_delete=models.CASCADE
    )
    nombre = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=1000)
    fecha_inicial = models.DateTimeField(null=True, blank=True)
    fecha_termino = models.DateTimeField(null=True, blank=True)
    lugar = models.CharField(max_length=250, null=True)
    tipo = models.CharField(max_length=100, null=True)
    terminada = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Actividades"

class Asistencia(models.Model):
    actividad = models.ForeignKey(
        'actividades.Actividad',
        on_delete=models.CASCADE
    )
    emprendimiento = models.ForeignKey(
        'emprendimientos.Emprendimiento',
        on_delete=models.CASCADE
    )
    estado = models.BooleanField(default=False)
    invitado = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return "\"{}\" asiste a \"{}\"".format(self.emprendimiento, self.actividad)

class Anotacion(models.Model):
    persona = models.ForeignKey(
        'personas.Persona',
        on_delete=models.CASCADE
    )
    actividad = models.ForeignKey(
        'Actividad',
        on_delete=models.CASCADE
    )
    nota = models.CharField(max_length=10000)
    fecha = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return "Anotacion de {} en {}".format(self.persona, self.actividad)
    
    class Meta:
        verbose_name_plural = "Anotaciones"
