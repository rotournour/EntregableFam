from django.shortcuts import render
from django.http import HttpResponse
from familia_app.models import Familia

def crear_familiar (requets): 
    nuevo_familiar = Familia.objects.create(nombre = "Constanza", edad = 5, mayor_edad = False)
    return HttpResponse('Se ha creado el nuevo integrante de la familia')

def listar_familiar (requets):
    familiares = Familia.objects.all()
    context = {
        'lista_familiares' : familiares
    }
    return render (requets, 'lista_familiares.html', context=context)