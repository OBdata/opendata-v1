from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect


def inicio(request):
    if request.user.is_authenticated and request.user.persona.rol != '2':
        return redirect('/emprendimientos/')
    elif request.user.is_authenticated and request.user.persona.rol == '2':
        return redirect('emprendimientos/mi_emprendimiento/')
    return render(request, "registration/login.html")