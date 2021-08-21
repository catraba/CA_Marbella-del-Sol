from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from .models import Atleta, Marca

from .forms import AtletaForm, MarcaForm

from datetime import datetime

from .functions import disciplina_por_atleta, establecerFechas, calculoMMP, calculoMaxSpeed, calculoDisTotal, comparacionRecordMundial

# Create your views here.

def club(request):
    return render(request, 'atletas/club.html')


def inlogin(request):
    if request.user.is_authenticated:
        return redirect('club')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect('club')

            else:
                messages.warning(request, 'Datos incorrectos')         

        return render(request, 'atletas/login.html')

def outlogin(request):
    logout(request)

    return redirect('login')


def atletas(request):
    atletas = Atleta.objects.all()

    return render(request, 'atletas/atletas.html', {'atletas': atletas})


def logros(request):
    return render(request, 'atletas/logros.html')


def record(request, atleta_slug):
    atleta = Atleta.objects.get(slug=atleta_slug)

    pruebas = disciplina_por_atleta(atleta.disciplina)

    temporada = datetime.today().year

    ficha = {prueba: {"Fechas": [], "Tiempos": []} for prueba in pruebas}
    ficha_temporada = {prueba: {"Fechas": [], "Tiempos": []} for prueba in pruebas}

    for prueba in pruebas:
        marcas = Marca.objects.filter(usuario=atleta_slug).filter(prueba=prueba)
        
        for marca in marcas:
            ficha[marca.prueba]["Fechas"].append(establecerFechas(marca.fecha))
            ficha[marca.prueba]["Tiempos"].append(float(marca.tiempo))

            if marca.fecha.year == temporada:
                ficha_temporada[marca.prueba]["Fechas"].append(establecerFechas(marca.fecha))
                ficha_temporada[marca.prueba]["Tiempos"].append(float(marca.tiempo))
    
    MMPs = calculoMMP(ficha)

    top_speed = {}

    if MMPs:
        if atleta.disciplina == 'Velocista':
            top_speed = calculoMaxSpeed(MMPs)

    dis_total = calculoDisTotal(ficha)

    comparaciones = comparacionRecordMundial(MMPs, atleta.sexo)

    return render(request, 'atletas/record.html', {'atleta': atleta, 
                                                'MMPs': MMPs, 
                                                'temporada': temporada, 
                                                'ficha': ficha,
                                                'ficha_temporada': ficha_temporada,
                                                'top_speed': top_speed,
                                                'dis_total': dis_total,
                                                'comparaciones': comparaciones})


@login_required(login_url='login')
def password(request):
    user = User.objects.get(username=request.user)

    if request.method == 'POST':
        old_password = request.POST.get('old_password')

        if check_password(old_password, user.password):
            new_password = request.POST.get('new_password')
            new_again_password = request.POST.get('new_again_password')

            if new_password == new_again_password:
                user.set_password(new_password)
                user.save()

                messages.success(request, 'Contraseña actualiza correctamente')

            else:
                messages.warning(request, 'Las contraseñas no coindicen')
            
        else:
            messages.warning(request, 'Contraseña incorrecta')

    return render(request, 'atletas/password.html')


@login_required(login_url='login')
def ficha(request):
    try:
        atleta = Atleta.objects.get(usuario=request.user)

    except:
        atleta = None

    if request.method == 'POST':
        form = AtletaForm(request.POST)
        
        if form.is_valid():
            new_atleta = form.save(commit=False)
            new_atleta.usuario = request.user
            new_atleta.save()

            return redirect('atletas')

    else:
       form = AtletaForm()

    return render(request, 'atletas/ficha.html', {'atleta': atleta, 
                                                'form': form})


@login_required(login_url='login')
def marcas(request):
    atleta = Atleta.objects.get(usuario=request.user)
    marcas = Marca.objects.filter(usuario=atleta).order_by('-fecha')

    #lugares = lugar_por_atleta()
    #pruebas = disciplina_por_atleta(atleta.disciplina)

    if request.method == 'POST':
        form = MarcaForm(request.POST)

        if form.is_valid():
            atleta = Atleta.objects.get(slug=atleta.slug)
            new_marca = form.save(commit=False)
            new_marca.usuario = atleta
            new_marca.save()

            return redirect('marcas')

    else:
        form = MarcaForm()

    return render(request, 'atletas/marcas.html', {'marcas': marcas,
                                                    'form': form})