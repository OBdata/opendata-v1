from django.shortcuts import render
from django.urls import reverse_lazy
from emprendimientos.models import *
from ficha.models import *
from actividades.models import *
import django_excel as excel
import pyexcel
import datetime
from django.contrib.auth.decorators import login_required


meses = {
    1:'Enero',
    2:'Febrero',
    3:'Marzo',
    4:'Abril',
    5:'Mayo',
    6:'Junio',
    7:'Julio',
    8:'Agosto',
    9:'Septiembre',
    10:'Octubre',
    11:'Noviembre',
    12:'Diciembre'
}

horas = {
    0: 21,
    1: 22,
    2: 23,
    3: 0,
    4: 1,
    5: 2,
    6: 3,
    7: 4,
    8: 5,
    9: 6,
    10: 7,
    11: 8,
    12: 9,
    13: 10,
    14: 11,
    15: 12,
    16: 13,
    17: 14,
    18: 15,
    19: 16,
    20: 17,
    21: 18,
    22: 19,
    23: 20,
}



def retrieve_data():
    emprendimientos = Emprendimiento.objects.all()
    trabajadores = Trabajador.objects.all()
    actividades = Actividad.objects.all()
    personas = Persona.objects.all()
    asistencias = Asistencia.objects.all()
    anotaciones = Anotacion.objects.all()

    assess = Assessment.objects.all()
    ventas = Venta.objects.all()
    costos = Costo.objects.all()
    patentes = Pat.objects.all()
    inversiones = Inversion.objects.all()

    # //////////////////////////// EMPRENDIMIENTOS //////////////////////////////////////////////////////////////////

    emps = pyexcel.Sheet(colnames=[
        'ID',
        'Dia',
        'Mes',
        'Año',
        'Hora',
        'Nombre',
        'Ejecutivo',
        'Rut Empresa',
        'Fecha Ingreso OB',
        'Año creación',
        'Descripción Corta',
        'Descripción Larga',
        'Ubicación',
        'Modelo e Negocios',
        'Sitio Web',
        'Programa',
        'Representante legal',
        'Número de trabajadores',
        'Presencia',
        'Modelo e Ingresos',
        'Patente',
        'StartUp o SpinOff',
        'Desafío y/o Problema',
        'Necesidades',
        'Categoría',
        'Mes de agregado'
    ])
        
    
    for emp in emprendimientos:
        e = Emprendimiento.objects.get(id=emp.id)
        name = e.persona.filter(rol='1')[0].user.first_name
        lastname = e.persona.filter(rol='1')[0].user.last_name
        ejecutivo = f'{name} {lastname}'
        row = [
            emp.id,
            emp.created_at.day,
            meses[emp.created_at.month],
            emp.created_at.year,
            f'{horas[emp.created_at.hour]}:{emp.created_at.minute}',
            emp.nombre,
            ejecutivo,
            emp.rut,
            emp.fecha_de_ingreso,
            emp.ano_creacion,
            emp.descripcion_corta,
            emp.descripcion_larga,
            emp.ubicacion,
            emp.modelo_negocio,
            emp.sitio_web,
            emp.programa,
            emp.representante_legal,
            emp.numero_trabajadores,
            emp.presencia,
            emp.modelo_ingreso,
            'Sí' if emp.patente else 'No',
            'StartUp' if emp.startup_spinoff else 'SpinOff',
            emp.desafio_problema,
            emp.necesidades,
            emp.categoria,
            emp.created_at.month
        ]
        emps.row += row
    # //////////////////////////// TRABAJADORES //////////////////////////////////////////////////////////////////

    trs = pyexcel.Sheet(colnames=[
        'ID',
        'Emprendimiento',
        'Dia',
        'Mes',
        'Año',
        'Hora',
        'Nombres',
        'Apellidos',
        'Género',
        'Rut',
        'Nacimiento',
        'Equity',
        'Cargo',
        'Profesion',
        'Tipo de Contrato',
        'Horas dedicadas',
        'Sueldo',
        'Vínculo Uchile',
        'Facultad Uchile'
    ])
    for t in trabajadores:
        row = [
            t.id,
            emprendimientos.filter(trabajador__id=t.id).get().nombre,
            t.created_at.day,
            meses[t.created_at.month],
            t.created_at.year,
            f'{horas[t.created_at.hour]}:{t.created_at.minute}',
            t.nombres,
            t.apellidos,
            t.genero,
            t.rut,
            t.fecha_cumpleanos,
            t.equity,
            t.rol,
            t.profesion,
            t.tipo_contrato,
            t.horas_dedicadas,
            t.sueldo,
            t.vinculo_uchile,
            t.facultad_uchile
        ]
        trs.row += row

    # //////////////////////////// ACTIVIDADES //////////////////////////////////////////////////////////////////

    act = pyexcel.Sheet(colnames=[
        'ID',
        'Dia',
        'Mes',
        'Año',
        'Hora',
        'Nombre',
        'Descripcion',
        'Fecha de Inicio',
        'Hora fecha de Inicio',
        'Fecha de Termino',
        'Hora fecha de Término',
        'Lugar',
        'Tipo',
        'Ingresada por',
        
    ])
    for a in actividades:
        row = [
            a.id,
            a.created_at.day,
            meses[a.created_at.month],
            a.created_at.year,
            f'{horas[a.created_at.hour]}:{a.created_at.minute}',
            a.nombre,
            a.descripcion,
            a.fecha_inicial,
            f'{horas[a.fecha_inicial.hour]}:{a.fecha_inicial.minute}',
            a.fecha_termino,
            f'{horas[a.fecha_termino.hour]}:{a.fecha_termino.minute}' if a.fecha_termino is not None else '' ,
            a.lugar,
            a.tipo,
            a.persona.user.first_name + " " + a.persona.user.last_name,
            
        ]
        act.row += row

    # //////////////////////////// PERSONAS //////////////////////////////////////////////////////////////////

    per = pyexcel.Sheet(colnames=[
        'ID',
        'Dia',
        'Mes',
        'Año',
        'Hora',
        'Nombres',
        'Apellidos',
        'Nombre de Usuario',
        'Correo',
        'Rol',
        'Profesión',
        'Rut',
        'Fecha de nacimiento'
    ])
    for p in personas:
        row = [
            p.id,
            p.created_at.day,
            meses[p.created_at.month],
            p.created_at.year,
            p.user.first_name,
            p.user.last_name,
            p.user.username,
            p.user.email,
            p.rol,
            p.profesion,
            p.rut,
            p.fecha_cumpleanos
        ]
        per.row += row

    # //////////////////////////// Ventas //////////////////////////////////////////////////////////////////

    ven = pyexcel.Sheet(colnames=[
        "ID",
        "Día", 
        "Mes", 
        "Año",
        "Hora",
        "Emprendimiento",
        "Ingresado por",
        "Monto",
        "Mes",
        "Año"
    ])

    for v in ventas:
        row = [
            v.id,
            v.created_at.day,
            meses[v.created_at.month],
            v.created_at.year,
            f'{horas[v.created_at.hour]}:{v.created_at.minute}',
            v.empredimiento.nombre,
            f'{v.persona.user.first_name} {v.persona.user.last_name}',
            v.monto,
            v.mes,
            v.anno
        ]
        ven.row += row

    # //////////////////////////// Costos //////////////////////////////////////////////////////////////////

    cos = pyexcel.Sheet(colnames=[
        "ID",
        "Día", 
        "Mes", 
        "Año",
        "Hora",
        "Emprendimiento",
        "Ingresado por",
        "Monto",
        "Mes",
        "Año"
    ])

    for c in costos:
        row = [
            c.id,
            c.created_at.day,
            meses[c.created_at.month],
            c.created_at.year,
            f'{horas[c.created_at.hour]}:{c.created_at.minute}',
            c.empredimiento.nombre,
            f'{c.persona.user.first_name} {c.persona.user.last_name}',
            c.monto,
            c.mes,
            c.anno
        ]
        cos.row += row

    # //////////////////////////// ASSESSMENT //////////////////////////////////////////////////////////////////
    asm = pyexcel.Sheet(colnames=[
        "ID",
        "Día", 
        "Mes", 
        "Año",
        "Hora",
        "Emprendimiento",
        "Ingresado por",

        "Equipo Experiencia Prevalencia", 
        "Equipo Experiencia Relevancia", 
        "Equipo Nivel", 
        "Equipo Balance", 
        "Equipo Dedidación",
        "Nota Equipo", 

        "Mercado Barreras", 
        "Mercado Necesidad", 
        "Mercado Tendencias", 
        "Mercado Acceso", 
        "Mercado Tamaño",
        "Nota Mercado",

        "Modelo Sustentabilidad", 
        "Modelo Estrategia", 
        "Modelo Escabilidad", 
        "Modelo Tiempo", 
        "Modelo Claridad",
        "Nota Modelo",

        "Tecnología Estado", 
        "Tecnología Propiedad", 
        "Tecnología Variedad", 
        "Tecnología Factibilidad", 
        "Tecnología Ventaja",
        "Nota Tecnología",

        "Finanzas Estrategia",
        "Finanzas Capital",
        "Finanzas Retorno",
        "Finanzas Flujo",
        "Finanzas Proyección",
        "Nota Finanzas",
 
    ])
    for a in assess:
        row = [
            a.id,
            a.created_at.day,
            meses[a.created_at.month],
            a.created_at.year,
            f'{horas[a.created_at.hour]}:{str(a.created_at.minute)}',
            a.emprendimiento.nombre,
            a.persona.user.first_name + " " + a.persona.user.last_name,

            a.equipo_experiencia_pre,
            a.equipo_experiencia_rel,
            a.equipo_nivel,
            a.equipo_balance,
            a.equipo_dedidacion,
            a.equipo_comentario,

            a.mercado_barreras,
            a.mercado_necesidad,
            a.mercado_tendencias,
            a.mercado_acceso,
            a.mercado_tamano,
            a.mercado_comentario,

            a.modelo_sustentabilidad,
            a.modelo_estrategia,
            a.modelo_escabilidad,
            a.modelo_tiempo,
            a.modelo_claridad,
            a.modelo_comentario,

            a.tecnologia_estado,
            a.tecnologia_propiedad,
            a.tecnologia_variedad,
            a.tecnologia_factibilidad,
            a.tecnologia_ventaja,
            a.tecnologias_comentario,

            a.finanzas_estrategia,
            a.finanzas_capital,
            a.finanzas_retorno,
            a.finanzas_flujo,
            a.finanzas_proyeccion,
            a.finanzas_comentario,

        ]
        asm.row += row
    # //////////////////////////// ASISTENCIAS //////////////////////////////////////////////////////////////////

    asis = pyexcel.Sheet(colnames=[
        "ID",
        "Dia",
        "Mes",
        "Año",
        'Hora',
        "Actividad",
        "Emprendimiento",
        "Invitado",
        "Asistencia"
    ])

    for a in asistencias:
        row = [
            a.id,
            a.created_at.day,
            meses[a.created_at.month],
            a.created_at.year,
            f'{horas[a.created_at.hour]}:{a.created_at.minute}',
            a.actividad.nombre,
            a.emprendimiento.nombre,
            'Sí' if a.invitado == 1 else 'No',
            'Sí' if a.estado == 1 else 'No',
        ]
        asis.row += row

    # //////////////////////////// ANOTACIONES //////////////////////////////////////////////////////////////////

    an = pyexcel.Sheet(colnames=[
        "ID",
        "Dia",
        "Mes",
        "Año",
        'Hora',
        "Ingresado por",
        "Actividad",
        "Anotacion"
    ])

    for a in anotaciones:
        row = [
            a.id,
            a.created_at.day,
            meses[a.created_at.month],
            a.created_at.year,
            f'{horas[a.created_at.hour]}:{a.created_at.minute}',
            a.persona.user.first_name + " " + a.persona.user.last_name,
            a.actividad.nombre,
            a.nota
        ]
        an.row += row
    
    # //////////////////////////// Patentes //////////////////////////////////////////////////////////////////

    pat = pyexcel.Sheet(colnames=[
        "ID",
        "Día", 
        "Mes", 
        "Año",
        "Hora",
        "Emprendimiento",
        "Ingresado por",
        "ID Patente",
        "Nombre",
    ])

    for p in patentes:
        row = [
            p.id,
            p.created_at.day,
            meses[p.created_at.month],
            p.created_at.year,
            f'{horas[p.created_at.hour]}:{p.created_at.minute}',
            p.emprendimiento.nombre,
            f'{p.persona.user.first_name} {p.persona.user.last_name}',
            p.iden,
            p.name
        ]
        pat.row += row

    # //////////////////////////// Inversiones //////////////////////////////////////////////////////////////////

    inv = pyexcel.Sheet(colnames=[
        "ID",
        "Día", 
        "Mes", 
        "Año",
        "Hora",
        "Emprendimiento",
        "Ejecutivo",
        "Monto",
        "Mes",
        "Año",
        "Tipo Institución",
        "Organización",
        "Fondo"
    ])

    for i in inversiones:
        row = [
            i.id,
            i.created_at.day,
            meses[i.created_at.month],
            i.created_at.year,
            f'{horas[i.created_at.hour]}:{i.created_at.minute}',
            i.emprendimiento.nombre,
            f'{i.persona.user.first_name} {i.persona.user.last_name}',
            i.monto,
            i.mes,
            i.anno,
            i.tipo,
            i.organizacion,
            i.fondo
        ]
        inv.row += row

    sheets = {

        '6. Trabajadores': trs,
        '0. Emprendimientos': emps,
        '1. Actividades': act,
        #'Personas': per,
        '4. Ventas': ven,
        '5. Costos': cos,
        '9. Diagnóstico': asm,
        '2. Asistencias': asis,
        '3. Anotaciones': an,
        '8. Patentes':pat,
        '7. Inversiones':inv
    }
    book = pyexcel.Book(sheets)
    return book


@login_required(login_url='/personas/login/')
def descargar_data(request):
    date = datetime.date.today().strftime('%d-%m-%Y')
    book = retrieve_data()
    return excel.make_response(
        book,
        "xlsx",
        file_name=f'{date}_Base_de_datos_Aceleracion_OpenBeauchef'
    )


@login_required(login_url='/personas/login/')
def visualizar_data(request):
    if request.user.persona.rol != '2':
        book = retrieve_data()
        #print(book)
        book.save_as(filename='data.xlsx')
        content = excel.pe.save_book_as(file_name='data.xlsx', dest_file_type='handsontable.html', dest_embed=True)
        return render(request, 'custom-handson-table.html', {'handsontable_content': content.read()})
    return reverse_lazy('emprendimientos:mi-empr')

