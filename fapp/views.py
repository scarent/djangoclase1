from django.shortcuts import render
from django.http import HttpResponse  #importar


# Create your views here.
def display(request):
    return HttpResponse("<h1>holamundo</h1>")
