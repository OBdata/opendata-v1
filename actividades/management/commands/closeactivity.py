from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from actividades.models import Actividad
from actividades.jobs import limpiar_cron_job
from pytz import timezone
from datetime import datetime

class Command(BaseCommand):
    help = "Closes the specified activity"
    
    def add_arguments(self, parser):
        parser.add_argument('actividad_id', nargs='+', type=int)

    def handle(self, *args, **options):
        for actividad_id in options['actividad_id']:
            try:
                actividad = Actividad.objects.get(id=actividad_id)
            except Actividad.DoesNotExist:
                raise CommandError('Actividad "%s" does not exist' % actividad_id)
            
            if actividad.fecha_termino <= timezone(settings.TIME_ZONE).localize(datetime.now()):
                actividad.terminada = True
                actividad.save()
                limpiar_cron_job(actividad)
                self.stdout.write(self.style.SUCCESS('Successfully closed activity "%s"' % actividad.nombre))