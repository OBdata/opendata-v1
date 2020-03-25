from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def ingresar(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        if user.persona.rol != '2':
            return HttpResponseRedirect(reverse('emprendimientos:index'))
        else:
            return HttpResponseRedirect(reverse('emprendimientos:mi-empr'))
    else:
        invalido = True
        return render(request, 'registration/login.html', {'invalido':invalido})


def salir(request):
    logout(request)
    return render(request, "registration/login.html")


@login_required(login_url='/personas/login/')
def nueva_constrasena(request):
    return render(request, 'cambiar-contrasena.html')


@login_required(login_url='/personas/login/')
def cambiar_contrasena(request):
    nueva_clave = request.POST.get('nueva_contrasena')
    confirmar_clave = request.POST.get('confirmar_contrasena')
    if nueva_clave == confirmar_clave:
        user = request.user
        user.set_password(nueva_clave)
        user.save()
        logout(request)
        success = True
        return render(request, 'registration/login.html', {'success':success})
    else:
        fail = True
        return render(request, 'cambiar-contrasena.html', {'fail':fail})


def olvide_contresena(request):
    print("hsjahsja")
    return render(request, "olvide-contrasena.html")