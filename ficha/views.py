import os
from django.conf import settings
from django.core.files.storage import default_storage
from django.shortcuts import render, redirect
from emprendimientos.models import *
from .models import *
from actividades.models import Actividad, Asistencia
from django.db import transaction
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required


@login_required(login_url='/personas/login/')
def ficha(request, nombre):
    emprendimiento = Emprendimiento.objects.get(id=nombre)
    return render(request, 'ficha/ficha-emprendimiento.html', {'emprendimiento': emprendimiento})


@login_required(login_url='/personas/login/')
def guardar_nueva_informacion(request):
    if request.POST:
        emprendimiento_id = request.POST.get("empId")
        emprendimiento_nombre = request.POST.get("nombre-emp")
        emprendimiento_logo = request.FILES.get('logo-emp', False)
        emprendimiento_desc_corta = request.POST.get("descripcion-corta")
        emprendimiento_modelo_negocio = request.POST.get("modelo-negocios")
        emprendimiento_categorias = request.POST.get("categorias-emp")
        emprendimiento_programa = request.POST.get("programa-emp")
        emprendimiento_web = request.POST.get("sitio-web")
        emprendimiento_patente = request.POST.get("patente-emp")
        emprendimiento_rep = request.POST.get("rep-legal")
        emprendimiento_rut = request.POST.get("rut-empresa")
        emprendimiento_presencia = request.POST.get("presencia-emp")
        emprendimiento_ingreso = request.POST.get("modelo-ingreso")
        emprendimiento_start = request.POST.get("startup-spinoff")
        emprendimiento_ubicacion = request.POST.get("ubicacion-emp")
        emprendimiento_ano_creacion= request.POST.get("ano-creacion")
        emprendimiento_fecha_ingreso = request.POST.get("fecha-ingreso")
        if not emprendimiento_logo:
            Emprendimiento.objects.filter(id=emprendimiento_id).update(
                nombre=emprendimiento_nombre,
                descripcion_corta=emprendimiento_desc_corta,
                modelo_negocio=emprendimiento_modelo_negocio,
                categoria=emprendimiento_categorias,
                sitio_web=emprendimiento_web,
                patente=int(emprendimiento_patente),
                representante_legal=emprendimiento_rep,
                programa=emprendimiento_programa,
                rut=emprendimiento_rut,
                presencia=emprendimiento_presencia,
                modelo_ingreso=emprendimiento_ingreso,
                startup_spinoff=int(emprendimiento_start),
                ubicacion=emprendimiento_ubicacion,
                ano_creacion=int(emprendimiento_ano_creacion),
                fecha_de_ingreso=emprendimiento_fecha_ingreso)
        else:
            Emprendimiento.objects.filter(id=emprendimiento_id).update(
                nombre=emprendimiento_nombre,
                foto_perfil=emprendimiento_logo,
                descripcion_corta=emprendimiento_desc_corta,
                modelo_negocio=emprendimiento_modelo_negocio,
                categoria=emprendimiento_categorias,
                sitio_web=emprendimiento_web,
                patente=int(emprendimiento_patente),
                representante_legal=emprendimiento_rep,
                rut=emprendimiento_rut,
                presencia=emprendimiento_presencia,
                modelo_ingreso=emprendimiento_ingreso,
                startup_spinoff=int(emprendimiento_start),
                ubicacion=emprendimiento_ubicacion,
                ano_creacion=int(emprendimiento_ano_creacion),
                fecha_de_ingreso=emprendimiento_fecha_ingreso)
            guardar_ruta = os.path.join(settings.MEDIA_ROOT, 'logos', emprendimiento_logo.name)
            default_storage.save(guardar_ruta, emprendimiento_logo)
    return redirect('../../ficha/' + str(emprendimiento_id) + '/success')


@login_required(login_url='/personas/login/')
def guardar_nuevos_desafios(request):
    if request.POST:
        emprendimiento_id = request.POST.get("empId")
        nuevos_desafios = request.POST.get("text-desafios")
    Emprendimiento.objects.filter(id=emprendimiento_id).update(desafio_problema=nuevos_desafios)
    return redirect('../../ficha/' + str(emprendimiento_id) + '/success')


@login_required(login_url='/personas/login/')
def guardar_nuevas_necesidades(request):
    if request.POST:
        emprendimiento_id = request.POST.get("empId")
        nuevas_necesidades = request.POST.get("text-necesidades")
    Emprendimiento.objects.filter(id=emprendimiento_id).update(necesidades=nuevas_necesidades)
    return redirect('../../ficha/' + str(emprendimiento_id) + '/success')


@login_required(login_url='/personas/login/')
def guardar_nueva_descripcion(request):
    if request.POST:
        emprendimiento_id = request.POST.get("empId")
        nueva_descripcion = request.POST.get("text-descripcion")
    Emprendimiento.objects.filter(id=emprendimiento_id).update(descripcion_larga=nueva_descripcion)
    return redirect('../../ficha/' + str(emprendimiento_id) + '/success')


@login_required(login_url='/personas/login/')
def ficha(request, id, success=False):
    emprendimiento = Emprendimiento.objects.get(id=id)
    asistencias = Asistencia.objects.filter(emprendimiento__id=id).all()
    trabajadores = Trabajador.objects.filter(emprendimiento__id=id).all()
    #actividades = Actividad.objects.filter(id__in=actividades_id).all()
    return render(request, 'ficha/ficha-emprendimiento.html', {'emprendimiento': emprendimiento, 'actividades': asistencias, 'success': success=='success', 'trabajadores': trabajadores})


@login_required(login_url='/personas/login/')
def guardar_nuevo_trabajador(request, id):
    if request.POST:
        emprendimiento_id = request.POST.get("empId")
        nombres = request.POST.get("nombre-trabajador")
        apellidos = request.POST.get("apellido-trabajador")
        cargo = request.POST.get("cargo-trabajador")
        profesion = request.POST.get("profesion-trabajador")
        contrato = request.POST.get("contrato-trabajador")
        horas = request.POST.get("horas-trabajador")
        sueldo = request.POST.get("sueldo-trabajador")
        vinculo = request.POST.get("vinculo-uchile")
        facultad = request.POST.get("facultad-uchile")
        genero = request.POST.get("genero-trabajador")
        equity = request.POST.get("equity-trabajador")
        rut = request.POST.get("rut-trabajador") 
        nacimiento_trabajador = request.POST.get("nacimiento-trabajador")

        nuevo_trabajador = Trabajador.objects.create(  
            nombres=nombres,
            apellidos=apellidos,
            rol=cargo,
            tipo_contrato=contrato,
            horas_dedicadas=horas,
            sueldo=sueldo,
            vinculo_uchile=vinculo,
            facultad_uchile=facultad,
            profesion=profesion,
            genero=genero,
            equity=equity,
            rut=rut,
            fecha_cumpleanos=nacimiento_trabajador
        )
        nuevo_trabajador.save()

        with transaction.atomic():
            emp = Emprendimiento.objects.filter(id=emprendimiento_id).select_for_update()[0]
            emp.trabajador.add(nuevo_trabajador)
            emp.numero_trabajadores += 1
            emp.save()

        return redirect('../../../ficha/' + emprendimiento_id + '/success')


@login_required(login_url='/personas/login/')
def guardar_nueva_venta(request, id):
    if request.POST:
        valor = request.POST.get("monto-venta")
        mes = request.POST.get("mes-venta")
        ano = request.POST.get("ano-venta")
        emprendimiento_id = request.POST.get("empId")
        persona_id = request.POST.get("perId")
        emprendimiento = Emprendimiento.objects.get(id=emprendimiento_id)
        persona = Persona.objects.get(id=persona_id)

        with transaction.atomic():
            fila = Fila.objects.create()
            fila.save()
            venta = Venta(
                empredimiento = emprendimiento,
                persona = persona,
                fila = fila,
                monto = valor,
                mes = mes,
                anno = ano
            )
        

        venta.save()

        return redirect('../../../ficha/' + str(emprendimiento.id) + '/success')

@login_required(login_url='/personas/login/')
def guardar_nuevo_costo(request, id):
    if request.POST:
        valor = request.POST.get("monto-costo")
        mes = request.POST.get("mes-costo")
        ano = request.POST.get("ano-costo")
        emprendimiento_id = request.POST.get("empId")
        persona_id = request.POST.get("perId")
        emprendimiento = Emprendimiento.objects.get(id=emprendimiento_id)
        persona = Persona.objects.get(id=persona_id)

        with transaction.atomic():
            fila = Fila.objects.create()
            fila.save()
            costo = Costo(
                empredimiento = emprendimiento,
                persona = persona,
                fila = fila,
                monto = valor,
                mes = mes,
                anno = ano
            )
        

        costo.save()

        return redirect('../../../ficha/' + str(emprendimiento.id) + '/success')




@login_required(login_url='/personas/login/')
def guardar_nueva_patente(request, id):
    if request.POST:
        id_patente = request.POST.get("id-patente")
        nombre_patente = request.POST.get("nombre-patente")
        emprendimiento_id = request.POST.get("empId")
        persona_id = request.POST.get("perId")
        emprendimiento = Emprendimiento.objects.get(id=emprendimiento_id)
        emprendimiento.patente = True
        emprendimiento.save()
        persona = Persona.objects.get(id=persona_id)
        fila = Fila.objects.create()
        fila.save()
        with transaction.atomic():
            patente = Pat(
                emprendimiento=emprendimiento,
                persona = persona,
                fila = fila,
                iden = id_patente,
                name = nombre_patente
            )
            patente.save()
        return redirect('../../../ficha/' + str(emprendimiento.id) + '/success')


@login_required(login_url='/personas/login/')
def guardar_nueva_inversion(request, id):
    if request.POST:
        valor = request.POST.get("monto-inversion")
        mes = request.POST.get("mes-inversion")
        ano = request.POST.get("ano-inversion")
        tipo = request.POST.get("tipo-inversion")
        organizacion = request.POST.get("nombre-organizacion")
        fondo = request.POST.get("nombre-fondo")
        emprendimiento_id = request.POST.get("empId")
        persona_id = request.POST.get("perId")

        emprendimiento = Emprendimiento.objects.get(id=emprendimiento_id)
        persona = Persona.objects.get(id=persona_id)
        fila = Fila.objects.create()
        fila.save()

        with transaction.atomic():
            inversion = Inversion(
                emprendimiento = emprendimiento,
                persona = persona,
                fila = fila,
                monto = valor,
                mes = mes,
                anno = ano,
                tipo = tipo,
                organizacion = organizacion,
                fondo = fondo
            )
            inversion.save()
        return redirect('../../../ficha/' + str(emprendimiento.id) + '/success')



@login_required(login_url='/personas/login/')
def guardar_nuevo_assesment(request, id):
        if request.POST:

            equipo_1 = request.POST.get("equipo-1")
            equipo_2 = request.POST.get("equipo-2")
            equipo_3 = request.POST.get("equipo-3")
            equipo_4 = request.POST.get("equipo-4")
            equipo_5 = request.POST.get("equipo-5")
            equipo_6 = request.POST.get("equipo-nota")

            mercado_1 = request.POST.get("mercado-1")
            mercado_2 = request.POST.get("mercado-2")
            mercado_3 = request.POST.get("mercado-3")
            mercado_4 = request.POST.get("mercado-4")
            mercado_5 = request.POST.get("mercado-5")
            mercado_6 = request.POST.get("mercado-nota")

            modelo_1 = request.POST.get("modelo-1")
            modelo_2 = request.POST.get("modelo-2")
            modelo_3 = request.POST.get("modelo-3")
            modelo_4 = request.POST.get("modelo-4")
            modelo_5 = request.POST.get("modelo-5")
            modelo_6 = request.POST.get("modelo-nota")

            tecnologia_1 = request.POST.get("tecnologia-1")
            tecnologia_2 = request.POST.get("tecnologia-2")
            tecnologia_3 = request.POST.get("tecnologia-3")
            tecnologia_4 = request.POST.get("tecnologia-4")
            tecnologia_5 = request.POST.get("tecnologia-5")
            tecnologia_6 = request.POST.get("tecnologia-nota")

            finanzas_1 = request.POST.get("finanzas-1")
            finanzas_2 = request.POST.get("finanzas-2")
            finanzas_3 = request.POST.get("finanzas-3")
            finanzas_4 = request.POST.get("finanzas-4")
            finanzas_5 = request.POST.get("finanzas-5")
            finanzas_6 = request.POST.get("finanzas-nota")

            emprendimiento_id = request.POST.get("empId")
            persona_id = request.POST.get("perId")

            emprendimiento = Emprendimiento.objects.get(id=emprendimiento_id)
            persona = Persona.objects.get(id=persona_id)

            assessment = Assessment(
                emprendimiento = emprendimiento,
                persona = persona,
                finanzas_estrategia = finanzas_1,
                finanzas_capital = finanzas_2,
                finanzas_retorno = finanzas_3,
                finanzas_flujo = finanzas_4,
                finanzas_proyeccion = finanzas_5,
                finanzas_comentario=finanzas_6,
                tecnologia_estado = tecnologia_1,
                tecnologia_propiedad = tecnologia_2,
                tecnologia_variedad = tecnologia_3,
                tecnologia_factibilidad = tecnologia_4,
                tecnologia_ventaja = tecnologia_5,
                tecnologias_comentario = tecnologia_6,
                modelo_sustentabilidad = modelo_1,
                modelo_estrategia = modelo_2,
                modelo_escabilidad = modelo_3,
                modelo_tiempo = modelo_4,
                modelo_claridad = modelo_5,
                modelo_comentario = modelo_6,
                mercado_barreras = mercado_1,
                mercado_necesidad = mercado_2,
                mercado_tendencias = mercado_3,
                mercado_acceso = mercado_4,
                mercado_tamano = mercado_5,
                mercado_comentario = mercado_6,
                equipo_experiencia_pre = equipo_1,
                equipo_experiencia_rel = equipo_2,
                equipo_nivel = equipo_3,
                equipo_balance = equipo_4,
                equipo_dedidacion = equipo_5,
                equipo_comentario = equipo_6
            )

            assessment.save()
            return redirect('../../../ficha/' + str(emprendimiento.id) + '/success')