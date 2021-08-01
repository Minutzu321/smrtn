from django.shortcuts import render, redirect
from django.http import JsonResponse 
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import *
import logging
import json
from shutil import copyfile
from .forms import LoginForm

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#functii ajutatoare
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def cookie_protocol(request):
    cookie = request.COOKIES.get('sesiune_smrtn')
    if cookie:
        try:
            ip = get_client_ip(request).strip()
            user = Utilizator.objects.get(cod_secret=cookie)
            try:
                ipo = user.ipuri.get(ip=ip)
                ipo.ora_data = timezone.now()
                ipo.save()
                user.ultima_logare = timezone.now()
                user.save()
            except Exception as e:
                user.ipuri.create(ip=ip)
            return user
        except:
            return None

def getExecutabil():
    try:
        exec = Executabil.objects.latest('ora_data_upload')
        if exec:
            return exec
        else:
            return None
    except:
        return None

def pregatesteExecutabilul(exec, nume):
    pth = os.path.join(BASE_DIR, 'executabile_utilizatori', nume)
    try:
        os.makedirs(os.path.join(BASE_DIR, 'executabile_utilizatori'))
    except: pass
    copyfile(exec.program.path, pth)
    return pth



# PAGINI
@ensure_csrf_cookie
def index(request):
    user = cookie_protocol(request)
    if user:
        if not user.acceptat:
            return render(request, 'templates/login.html', {'eroare': "<h2 style='color: red'>Contul a fost dezactivat.</h2>"})
        if request.method == 'POST':
            e = getExecutabil()
            if e:
                pregatesteExecutabilul(e, user.nume)
            return JsonResponse({'raspuns': 'da'})
        raspuns = render(request, 'templates/index.html')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                nume = form.cleaned_data['nume']
                parola = form.cleaned_data['parola']
                try:
                    user = Utilizator.objects.get(nume=nume, parola=parola)
                    if user.acceptat:
                        raspuns = redirect('/')
                        raspuns.set_cookie('sesiune_smrtn', user.cod_secret, max_age=60*60*24*31*12)
                        return raspuns
                    else:
                        return render(request, 'templates/login.html', {'eroare': "<h2 style='color: red'>Contul a fost dezactivat.</h2>"})
                except:
                    return render(request, 'templates/login.html', {'form': form, 'eroare': "<h2 style='color: red'>Combinatia de utilizator si parola nu este corecta.</h2>"})
        else:
            form = LoginForm()
        raspuns = render(request, 'templates/login.html', {'form': form})
    return raspuns
