from django.shortcuts import render
from django.http import HttpResponse  #importar
# Create your views here.
def sapp(request):
    return HttpResponse("<h1>Bienvenido a la segunda app</h1>")