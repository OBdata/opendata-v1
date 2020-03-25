import pytz
from pytz import timezone
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.conf import settings
from actividades.models import Actividad, Asistencia, Anotacion
from emprendimientos.models import Emprendimiento
from personas.models import Persona
from django.http import JsonResponse
from django.db import transaction
from actividades.jobs import agendar_cierre, limpiar_cron_job, modificar_agenda


@login_required(login_url='/personas/login/')
def index(request):
    actividades = Actividad.objects.all()
    return render(request, 'actividades/listado-actividades.html', {"actividades": actividades})

@login_required(login_url='/personas/login/')
def nueva_actividad(request):
    emprendimientos = Emprendimiento.objects.all()
    return render(request, 'actividades/formulario-nueva-actividad.html',{'emprendimientos': emprendimientos})


@login_required(login_url='/personas/login/')
def ver_actividad(request, id, success=False):
    actividad = Actividad.objects.get(id=id)
    invitados = Asistencia.objects.filter(actividad=actividad)
    return render(request, 'actividades/ver-actividad.html', {
        'actividad': actividad, 
        'invitados': invitados, 
        'success': success=='success'
    })


@login_required(login_url='/personas/login/')
def agregar_nueva(request):
    emprendimientos = Emprendimiento.objects.all()
    if request.POST:
        termino = request.POST.get("fecha-fin-actividad")
        if termino != '':
            nombre_actividad = request.POST.get("nombre-nueva-actividad")
            lugar_actividad = request.POST.get("lugar-nueva-actividad")
            fecha_inicio_actividad = datetime.strptime(request.POST.get("fecha-inicio-actividad"), '%Y-%m-%d').date()
            hora_inicio_actividad = datetime.strptime(request.POST.get("hora-inicio-actividad"), '%H:%M').time()
            print(type(request.POST.get("fecha-fin-actividad")))
            fecha_fin_actividad = datetime.strptime(request.POST.get("fecha-fin-actividad"), '%Y-%m-%d').date()
            hora_fin_actividad = datetime.strptime(request.POST.get("hora-fin-actividad"), '%H:%M').time()
            descripcion_actividad = request.POST.get("descripcion-actividad")
            tipo_actividad = request.POST.get("tipo-actividad")
            fecha_hora_inicio = datetime.combine(fecha_inicio_actividad,hora_inicio_actividad)
            fecha_hora_fin = datetime.combine(fecha_fin_actividad, hora_fin_actividad)
            ejecutivo_id = int(request.POST.get("ejecId"))
            persona = Persona.objects.get(id=ejecutivo_id)
            actividad = Actividad.objects.create(
                persona=persona,
                nombre=nombre_actividad,
                descripcion=descripcion_actividad,
                fecha_inicial=timezone(settings.TIME_ZONE).localize(fecha_hora_inicio),
                fecha_termino=timezone(settings.TIME_ZONE).localize(fecha_hora_fin),
                lugar=lugar_actividad,
                tipo=tipo_actividad,
                terminada=False
            )
            actividad.save()

            if actividad.fecha_termino < timezone(settings.TIME_ZONE).localize(datetime.now()):
                actividad.terminada = True
                actividad.save()
            else:
                agendar_cierre(actividad)
            
            for e in emprendimientos:
                asistencia = Asistencia.objects.create(
                    actividad=actividad,
                    emprendimiento=e
                )
                checkbox_emp = request.POST.get("invitar-emp-" + str(e.id))
                if checkbox_emp:
                    asistencia.invitado = True
                asistencia.save()
        else:
            nombre_actividad = request.POST.get("nombre-nueva-actividad")
            lugar_actividad = request.POST.get("lugar-nueva-actividad")
            fecha_inicio_actividad = datetime.strptime(request.POST.get("fecha-inicio-actividad"), '%Y-%m-%d').date()
            hora_inicio_actividad = datetime.strptime(request.POST.get("hora-inicio-actividad"), '%H:%M').time()
            descripcion_actividad = request.POST.get("descripcion-actividad")
            tipo_actividad = request.POST.get("tipo-actividad")
            fecha_hora_inicio = datetime.combine(fecha_inicio_actividad,hora_inicio_actividad)
            ejecutivo_id = int(request.POST.get("ejecId"))
            persona = Persona.objects.get(id=ejecutivo_id)
            actividad = Actividad.objects.create(
                persona=persona,
                nombre=nombre_actividad,
                descripcion=descripcion_actividad,
                fecha_inicial=timezone(settings.TIME_ZONE).localize(fecha_hora_inicio),
                lugar=lugar_actividad,
                tipo=tipo_actividad,
                terminada=False
            )
            actividad.save()
            
            
            for e in emprendimientos:
                asistencia = Asistencia.objects.create(
                    actividad=actividad,
                    emprendimiento=e
                )
                checkbox_emp = request.POST.get("invitar-emp-" + str(e.id))
                if checkbox_emp:
                    asistencia.invitado = True
                asistencia.save()
    actividades = Actividad.objects.all()
    return redirect('../')


@login_required(login_url='/personas/login/')
def actualizar_asistencia(request, id):
    checked = request.GET.get('checked', None)
    as_id = request.GET.get('as_id', None)
    with transaction.atomic():
        asistencia = Asistencia.objects.filter(id=as_id).select_for_update()[0]
        asistencia.estado = True if checked == "true" else False
        asistencia.save()
    data = {
    }
    return JsonResponse(data)


@login_required(login_url='/personas/login/')
def nuevas_invitaciones(request,id):
    emprendimientos = Emprendimiento.objects.all()
    actividad = Actividad.objects.get(id=id)
    asistencias = Asistencia.objects.filter(actividad=actividad)
    if request.POST:
        for e in emprendimientos:
            checkbox_emp = request.POST.get("invitar-emp-"+str(e.id))
            if checkbox_emp:
                print("hola")
            asistencia = asistencias.get(emprendimiento=e)
            if checkbox_emp and not asistencia.invitado:
                asistencia.invitado = True
            elif not checkbox_emp and asistencia.invitado:
                asistencia.invitado = False
            asistencia.save()

    return redirect('../../../actividades/' + str(id))


@login_required(login_url='/personas/login/')
def editar_informacion(request,id):
    if request.POST:
        termino = request.POST.get("fecha-fin-actividad")
        if termino != '':
            nombre_actividad = request.POST.get("nombre-actividad")
            lugar_actividad = request.POST.get("lugar-actividad")
            fecha_inicio_actividad = datetime.strptime(request.POST.get("fecha-inicio-actividad"), '%Y-%m-%d').date()
            hora_inicio_actividad = datetime.strptime(request.POST.get("hora-inicio-actividad"), '%H:%M').time()
            fecha_fin_actividad = datetime.strptime(request.POST.get("fecha-fin-actividad"), '%Y-%m-%d').date()
            hora_fin_actividad = datetime.strptime(request.POST.get("hora-fin-actividad"), '%H:%M').time()
            descripcion_actividad = request.POST.get("descripcion-actividad")
            tipo_actividad = request.POST.get("tipo-actividad")
            fecha_hora_inicio = datetime.combine(fecha_inicio_actividad, hora_inicio_actividad)
            fecha_hora_fin = datetime.combine(fecha_fin_actividad, hora_fin_actividad)
            Actividad.objects.filter(id=id).update(
                nombre=nombre_actividad,
                descripcion=descripcion_actividad,
                fecha_inicial=timezone(settings.TIME_ZONE).localize(fecha_hora_inicio),
                fecha_termino=timezone(settings.TIME_ZONE).localize(fecha_hora_fin),
                lugar=lugar_actividad,
                tipo=tipo_actividad,
                terminada=False
            )
            actividad = Actividad.objects.get(id=id)
            if actividad.fecha_termino < timezone(settings.TIME_ZONE).localize(datetime.now()):
                actividad.terminada = True
                actividad.save()
                limpiar_cron_job(actividad)
            else:
                modificar_agenda(actividad)
        else:
            nombre_actividad = request.POST.get("nombre-actividad")
            lugar_actividad = request.POST.get("lugar-actividad")
            fecha_inicio_actividad = datetime.strptime(request.POST.get("fecha-inicio-actividad"), '%Y-%m-%d').date()
            hora_inicio_actividad = datetime.strptime(request.POST.get("hora-inicio-actividad"), '%H:%M').time()
            descripcion_actividad = request.POST.get("descripcion-actividad")
            tipo_actividad = request.POST.get("tipo-actividad")
            fecha_hora_inicio = datetime.combine(fecha_inicio_actividad, hora_inicio_actividad)
            Actividad.objects.filter(id=id).update(
                nombre=nombre_actividad,
                descripcion=descripcion_actividad,
                fecha_inicial=timezone(settings.TIME_ZONE).localize(fecha_hora_inicio),
                lugar=lugar_actividad,
                tipo=tipo_actividad,
                terminada=False
            )

    return redirect('../../../actividades/' + str(id))

@login_required(login_url='/personas/login/')
def guardar_anotacion(request, id):
    if request.POST:
        persona_id = request.POST.get("ejecId")
        actividad_id = request.POST.get("actId")
        nota = request.POST.get('anotacion-actividad')
        persona = Persona.objects.get(id=persona_id)
        actividad = Actividad.objects.get(id=actividad_id)

        with transaction.atomic():
            nota = Anotacion.objects.create(
                    persona=persona,
                    actividad=actividad,
                    nota=nota
                )
            nota.save()
    return redirect(f'../../../actividades/{id}/success')
    #return redirect('../../../actividades/' + str(id))