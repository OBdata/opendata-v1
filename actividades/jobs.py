import os
import pytz
from crontab import CronTab
from django.conf import settings

PY = os.path.join(settings.BASE_DIR, "../venv/bin/python")

def agendar_cierre(actividad):
    cron = CronTab(user=True)
    cm = f"{PY} {settings.BASE_DIR}/manage.py closeactivity {actividad.pk} > /tmp/cronlog.txt 2>&1"
    job = cron.new(command=cm)
    time = actividad.fecha_termino.astimezone(pytz.timezone(settings.TIME_ZONE))
    job.setall(time)
    cron.write()

def limpiar_cron_job(actividad):
    cron = CronTab(user=True)
    cm = f"{PY} {settings.BASE_DIR}/manage.py closeactivity {actividad.pk} > /tmp/cronlog.txt 2>&1"
    cron.remove_all(command=cm) 
    cron.write()

def modificar_agenda(actividad):
    limpiar_cron_job(actividad)
    agendar_cierre(actividad)
