from django.shortcuts import render
from django.http import HttpResponse

def saludar(request):
    return HttpResponse("Hola desde Django!")
def saludar2(request):
    return HttpResponse("<h1> Este es mi tutilo <h1>")

def index(request):
    return render(request,"prueba/index.html")