from django.shortcuts import render, redirect
from .Carro import *
from Tienda.models import Producto

# Create your views here.
def agrega_producto(request, producto_id):
    carro = Carro(request)
    producto_a_agregar = Producto.objects.get(id=producto_id)
    carro.agregar(producto_a_agregar)

    return redirect("tienda")

def elimina_producto(request, producto_id):
    carro = Carro(request)
    producto_a_eliminar = Producto.objects.get(id=producto_id)
    carro.eliminar(producto_a_eliminar)
    return redirect("tienda")

def resta_producto(request, producto_id):
    carro = Carro(request)
    producto_a_restar = Producto.objects.get(id=producto_id)
    carro.restar_producto(producto_a_restar)

    return redirect("tienda")


def limpia_carro(request):
    carro = Carro(request)
    carro.limpia_carro()
    return redirect("tienda")
