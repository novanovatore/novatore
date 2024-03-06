from django.shortcuts import render, redirect
from .Carro import *
from Tienda.models import Producto

# Create your views here.
def agrega_producto(request, producto_id, pagina):
    carro = Carro(request)
    producto_a_agregar = Producto.objects.get(id=producto_id)
    carro.agregar(producto_a_agregar)

    # enviar mensaje
    
    if pagina == "tienda":
        return redirect("tienda")
    else:
        return redirect("carro:carro")

def elimina_producto(request, producto_id):
    carro = Carro(request)
    producto_a_eliminar = Producto.objects.get(id=producto_id)
    carro.eliminar(producto_a_eliminar)
    return redirect("carro:carro")

def resta_producto(request, producto_id):
    carro = Carro(request)
    producto_a_restar = Producto.objects.get(id=producto_id)
    carro.restar_producto(producto_a_restar)

    return redirect("carro:carro")


def limpia_carro(request):
    carro = Carro(request)
    carro.limpia_carro()
    return redirect("tienda")


def muestra_carro(request):
    return render(request, "Carro/carro.html")