from django.shortcuts import render
from django.http import HttpResponse  #importar
import datetime


# Create your views here.
def display(request):
    return HttpResponse("<h1>holamundo</h1>")

def displayDateTime(request):
    dt= datetime.datetime.now()
    s = "<b>fecha y hora actual: </b>"+str(dt)
    return HttpResponse(s)

def form(request):
    return HttpResponse("<h1>vbienvenido</h1> <br> Nombre: <input></input> <br> Pass: <input></input> </br> <br> <button>Ingresar</button>")