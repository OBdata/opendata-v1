from django.db import models
from personas.models import Persona


class Trabajador(models.Model):
    nombres = models.CharField(max_length=250)
    apellidos = models.CharField(max_length=250)
    equity = models.IntegerField()
    rol = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    tipo_contrato = models.CharField(max_length=100)
    horas_dedicadas = models.IntegerField()
    sueldo = models.BigIntegerField()
    genero = models.CharField(max_length=50)
    vinculo_uchile = models.CharField(max_length=100)
    facultad_uchile = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, null=True, blank=True)
    fecha_cumpleanos = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.nombres, self.apellidos)
    
    class Meta:
        verbose_name_plural = "Trabajadores"


class Emprendimiento(models.Model):
    persona = models.ManyToManyField(Persona)
    trabajador = models.ManyToManyField(Trabajador, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    foto_perfil = models.ImageField(upload_to='logos/', blank=True)
    nombre = models.CharField(max_length=250)
    rut = models.CharField(max_length=250, blank=True)
    descripcion_corta = models.CharField(max_length=10000, blank=True)
    descripcion_larga = models.CharField(max_length=10000, blank=True)
    ubicacion = models.CharField(max_length=250, blank=True)
    ano_creacion = models.SmallIntegerField()
    modelo_negocio = models.CharField(max_length=250, blank=True)
    sitio_web = models.CharField(max_length=250, blank=True)
    programa = models.CharField(max_length=250, blank=True)
    representante_legal = models.CharField(max_length=250, blank=True)
    numero_trabajadores = models.IntegerField(default=0)
    presencia = models.CharField(max_length=250, blank=True)
    modelo_ingreso = models.CharField(max_length=250, blank=True)
    patente = models.BooleanField(default=False)
    startup_spinoff = models.BooleanField(default=True)
    desafio_problema = models.CharField(max_length=1000, blank=True)
    necesidades = models.CharField(max_length=1000, blank=True)
    categoria = models.CharField(max_length=250, blank=True)
    fecha_de_ingreso = models.DateField()

    def __str__(self):
        return self.nombre
    
class Postulacion(models.Model):
    emprendimiento = models.ForeignKey(Emprendimiento, on_delete=models.CASCADE)
    emprendedor = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True)
    campo = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)
    fecha = models.DateField()
    estado = models.BooleanField(default=False)

class Historial(models.Model):
    emprendimiento = models.ForeignKey(Emprendimiento, on_delete=models.CASCADE)

    persona = models.ManyToManyField(Persona)
    trabajador = models.ManyToManyField(Trabajador)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    foto_perfil = models.ImageField(upload_to='fotos_perfiles/', default='path/to/my/default/image.jpg')
    nombre = models.CharField(max_length=250)
    rut = models.CharField(max_length=250)
    descripcion_corta = models.CharField(max_length=300)
    descripcion_larga = models.CharField(max_length=1000, blank=True)
    ubicacion = models.CharField(max_length=250, blank=True)
    ano_creacion = models.SmallIntegerField()
    modelo_negocio = models.CharField(max_length=250, blank=True)
    sitio_web = models.CharField(max_length=250, blank=True)
    programa = models.CharField(max_length=250)
    representante_legal = models.CharField(max_length=250)
    numero_trabajadores = models.IntegerField(default=0)
    presencia = models.CharField(max_length=250)
    modelo_ingreso = models.CharField(max_length=250)
    patente = models.BooleanField(default=False)
    startup_spinoff = models.BooleanField(default=True)
    desafio_problema = models.CharField(max_length=1000)
    necesidades = models.CharField(max_length=1000)
    categoria = models.CharField(max_length=250)
    fecha_de_ingreso = models.DateField()

    fecha_de_validez = models.DateField()

    def __str__(self):
        return "{} en {}".format(Emprendimiento, fecha_de_validez)
