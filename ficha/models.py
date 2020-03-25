from django.db import models
from personas.models import Persona
from reporte.models import Fila

# class Eje(models.Model):
#     eje = models.CharField(max_length=250)

#     def __str__(self):
#         return str(self.eje)


# class CategoriaEje(models.Model):
#     eje = models.ForeignKey(
#         'Eje',
#         on_delete=models.CASCADE
#     )
#     nombre = models.CharField(max_length=250)

#     def __str__(self):
#         return "{}.{}".format(self.eje, self.nombre)

class Assessment(models.Model):
    emprendimiento = models.ForeignKey(
        'emprendimientos.Emprendimiento',
        on_delete=models.CASCADE
    )
    persona = models.ForeignKey(
        'personas.Persona',
        on_delete=models.CASCADE
    )

    finanzas_estrategia = models.IntegerField()
    finanzas_capital = models.IntegerField()
    finanzas_retorno = models.IntegerField()
    finanzas_flujo = models.IntegerField()
    finanzas_proyeccion = models.IntegerField()

    finanzas_comentario = models.CharField(max_length=1000)

    tecnologia_estado = models.IntegerField()
    tecnologia_propiedad = models.IntegerField()
    tecnologia_variedad = models.IntegerField()
    tecnologia_factibilidad = models.IntegerField()
    tecnologia_ventaja = models.IntegerField()

    tecnologias_comentario = models.CharField(max_length=1000)

    modelo_sustentabilidad = models.IntegerField()
    modelo_estrategia = models.IntegerField()
    modelo_escabilidad = models.IntegerField()
    modelo_tiempo = models.IntegerField()
    modelo_claridad = models.IntegerField()

    modelo_comentario = models.CharField(max_length=1000)

    mercado_barreras = models.IntegerField()
    mercado_necesidad = models.IntegerField()
    mercado_tendencias = models.IntegerField()
    mercado_acceso = models.IntegerField()
    mercado_tamano = models.IntegerField()

    mercado_comentario = models.CharField(max_length=1000)

    equipo_experiencia_pre = models.IntegerField()
    equipo_experiencia_rel = models.IntegerField()
    equipo_nivel = models.IntegerField()
    equipo_balance = models.IntegerField()
    equipo_dedidacion = models.IntegerField()

    equipo_comentario = models.CharField(max_length=1000)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return "\{}".format(self.emprendimiento)

    class Meta:
        verbose_name_plural = "Diagnósticos"


# Primero consulta a la nota para tener toda la data
# class NotaAssessment(models.Model):
#     emprendimiento = models.ForeignKey(
#         'emprendimientos.Emprendimiento',
#         on_delete=models.CASCADE
#     )
#     persona = models.ForeignKey(
#         'personas.Persona',
#         on_delete=models.CASCADE
#     )
#     categoria = models.ForeignKey(
#         'CategoriaEje',
#         on_delete=models.CASCADE
#     )
#     nota = models.IntegerField()

#     created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

#     def __str__(self):
#         return "\"{}\" en {}: {}".format(self.emprendimiento, self.categoria, self.nota)

#     class Meta:
#         verbose_name_plural = "Notas assesments"


# class NombreVariable(models.Model):
#     nombre = models.CharField(max_length=250)

#     def __str__(self):
#         return self.nombre


# class Caracteristica(models.Model):
#     nombre = models.CharField(max_length=250)

#     def __str__(self):
#         return self.nombre


# class VariableDinamica(models.Model):
#     empredimiento = models.ForeignKey(
#         'emprendimientos.Emprendimiento',
#         on_delete=models.CASCADE
#     )
#     persona = models.ForeignKey(
#         'personas.Persona',
#         on_delete=models.CASCADE
#     )
#     nombre_variable = models.ForeignKey(
#         'NombreVariable',
#         on_delete=models.CASCADE
#     )
#     caracteristica = models.ForeignKey(
#         'Caracteristica',
#         on_delete=models.CASCADE
#     )
#     fila = models.ForeignKey(
#         'reporte.Fila',
#         on_delete=models.CASCADE
#     )
#     fecha = models.DateTimeField()
#     valor = models.CharField(max_length=250)
#     estado = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

#     def __str__(self):
#         return "\"{}\": {}.{} = {}".format(self.empredimiento, self.nombre_variable, self.caracteristica, self.valor)

#     class Meta:
#         verbose_name_plural = "Variables dinamicas"

class Venta(models.Model):
    empredimiento = models.ForeignKey(
        'emprendimientos.Emprendimiento',
        on_delete=models.CASCADE
    )
    persona = models.ForeignKey(
        'personas.Persona',
        on_delete=models.CASCADE
    )
    fila = models.ForeignKey(
        'reporte.Fila',
        on_delete=models.CASCADE
    )

    monto = models.IntegerField()
    mes = models.CharField(max_length=20)
    anno = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{self.empredimiento}'

    class Meta:
        verbose_name_plural = "Ventas"

class Costo(models.Model):
    empredimiento = models.ForeignKey(
        'emprendimientos.Emprendimiento',
        on_delete=models.CASCADE
    )
    persona = models.ForeignKey(
        'personas.Persona',
        on_delete=models.CASCADE
    )
    fila = models.ForeignKey(
        'reporte.Fila',
        on_delete=models.CASCADE
    )

    monto = models.IntegerField()
    mes = models.CharField(max_length=20)
    anno = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{self.empredimiento}'

    class Meta:
        verbose_name_plural = "Costos"

class Pat(models.Model):
    emprendimiento = models.ForeignKey(
        'emprendimientos.Emprendimiento',
        on_delete=models.CASCADE
    )
    persona = models.ForeignKey(
        'personas.Persona',
        on_delete=models.CASCADE
    )
    fila = models.ForeignKey(
        'reporte.Fila',
        on_delete=models.CASCADE
    )

    iden = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{self.emprendimiento}'

    class Meta:
        verbose_name_plural = "Patente"

class Inversion(models.Model):
    emprendimiento = models.ForeignKey(
        'emprendimientos.Emprendimiento',
        on_delete=models.CASCADE
    )
    persona = models.ForeignKey(
        'personas.Persona',
        on_delete=models.CASCADE
    )
    fila = models.ForeignKey(
        'reporte.Fila',
        on_delete=models.CASCADE
    )

    monto = models.IntegerField()
    mes = models.CharField(max_length=20)
    anno = models.IntegerField()
    tipo = models.CharField(max_length=10)
    organizacion = models.CharField(max_length=100)
    fondo = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{self.emprendimiento}'

    class Meta:
        verbose_name_plural = "Inversiones"

class FacultadesUchile(models.Model):
    nombre = models.CharField(max_length=200)

class Programas(models.Model):
    nombre = models.CharField(max_length=200)