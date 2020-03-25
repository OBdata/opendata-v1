from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Persona(models.Model):

    EJECUTIVO = '1'
    EMPRENDEDOR = '2'

    ROLES_CHOICES = (
        (EJECUTIVO, 'Ejecutivo'),
        (EMPRENDEDOR, 'Emprendedor')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=2, choices=ROLES_CHOICES)
    profesion = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, null=True, blank=True)
    fecha_cumpleanos = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_persona(sender, instance, created, **kwargs):
    if created:
        Persona.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_persona(sender, instance, **kwargs):
    instance.persona.save()


