from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Carro.context_processor import importe_total_carro
from .models import *
from Carro.Carro import Carro
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

# si está logueado se ejecutará la vista con 
# normalidad, si no, entonces lo redigirá al
# login
@login_required(login_url="{'login'}")
def procesar_pedido(request):
    
    # creamos un pedido para el usuario activo
    pedido = Pedidos.objects.create(user=request.user)
    # recorrermos el carro para almacenarlo en 
    # LineaPedido y conectarlo con el pedido
    # correspondiente
    linea_pedido_carro = []
    carro = Carro(request)
    for key, value in carro.carro.items():
        linea_pedido_carro.append(
            LineaPedido(
                pedido=pedido, 
                producto_id=key,
                cantidad=value["cantidad"]
            )
        )

    # insertamos en la db todo el lote de LineasPedido
    LineaPedido.objects.bulk_create(linea_pedido_carro)

    # limpiamos el carro
    total_compra = importe_total_carro(request)["importe_total_carro"]
    carro_info = carro.limpia_carro()

    #datos_pedido = configura_linea_pedido_email(pedido)
    # mandamos el email con el pedido
    envio_email(pedido, linea_pedido_carro, request.user)

    # le informamos al usuario el exito de la operacion
    messages.success(
        request,
        ("Pedido realizado correctamente.",
        "Se le envío al correo la información de su pedido")
    )

    return render(
        request, "exito.html", {"pedido": pedido, "carro":carro_info, "total": total_compra})


def envio_email(pedido, linea_pedido, usuario):
    send_mail(
        subject="Pedido Realizado",
        message="",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[usuario.email]
    )


"""
def configura_linea_pedido_email(pedido):
    print(pedido)
    
    # filtrame los productos que esten el pedido
    productos_pedido = Producto.objects.filter(lineapedido__pedido_id=pedido.id)
    # filtrame las lineaspedidos que sean parte
    # del pedido
    lineas_pedido = LineaPedido.objects.filter(pedido_id=pedido.id)

    datos_pedido = {
        "pedido": pedido,
        "lineas_pedido": lineas_pedido,
        "productos": productos_pedido
    }


    return datos_pedido
"""
    
    

