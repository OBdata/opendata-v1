from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from actividades.models import Actividad, Asistencia
from .models import *


@login_required(login_url='/personas/login/')
def index(request):
    if request.user.is_authenticated and request.user.persona.rol == '2':
        return redirect('/emprendimientos/mi_emprendimiento/')
    emprendimientos = Emprendimiento.objects.all()
    if(request.user.is_authenticated):
        id_emp = []
        for e in emprendimientos:
            if(request.user.id in e.persona.values_list('id',flat=True)):
                id_emp += [str(e.id)]
        own = emprendimientos.filter(id__in = id_emp)
    else:
        own = emprendimientos
        
    return render(request, 'emprendimientos/listado-emprendimientos.html', {"emprendimientos":emprendimientos, "own": own})

@login_required(login_url='/personas/login/')
def nuevo_emprendimiento(request):
    ejecutivos = Persona.objects.all().filter(rol='1')
    return render(request, 'emprendimientos/formulario-nuevo-emprendimiento.html', {'ejecutivos': ejecutivos})

def guardar_nuevo_emprendimiento(request):
    if request.POST:
        nombre_emprendimiento = request.POST.get('nombre-emp')
        fecha_inscripcion = request.POST.get('fecha-inscripcion')
        ano_de_creacion = fecha_inscripcion.split("-")[0]
        monitores = request.POST.getlist('monitor')

        emprendimiento = Emprendimiento.objects.create(
            nombre=nombre_emprendimiento,
            ano_creacion=ano_de_creacion,
            fecha_de_ingreso=fecha_inscripcion
        )

        emprendimiento.save()
        for monitor in monitores:
            emprendimiento.persona.add(Persona.objects.get(id=monitor))
        actividades = Actividad.objects.all()
        for actividad in actividades:
            asistencia = Asistencia.objects.create(
                emprendimiento=emprendimiento,
                actividad=actividad
            )
            asistencia.save()

        return redirect('../../ficha/'+str(emprendimiento.id))


def mi_emprendimiento(request):
    emprendimiento = None
    asistencias = None
    if request.user.is_authenticated:
        emprendimiento = Emprendimiento.objects.filter(persona=request.user.persona)[0]
        print(emprendimiento.id)
        asistencias = Asistencia.objects.filter(emprendimiento__id=emprendimiento.id).all()
    return render(request, "ficha/ficha-emprendimiento.html", {'emprendimiento': emprendimiento, 'actividades': asistencias})
