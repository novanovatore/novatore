from django.shortcuts import render
from .models import *

# Create your views here.

def servicios(request):
    
    # importa todos los objetos que tengamos de la clase
    # Servicio
    servs = Servicio.objects.all()


    return render(request, "Servicios/servicios.html", {"servicios": servs})