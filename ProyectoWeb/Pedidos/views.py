from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Carro.context_processor import importe_total_carro
from .models import *
from Carro.Carro import Carro
from django.core.mail import send_mail
from django.conf import settings

# esto es necesario para la generación de pdf #
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML
import os

os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")

# Create your views here.

# si está logueado se ejecutará la vista con 
# normalidad, si no, entonces lo redigirá al
# login
@login_required(login_url="{'login'}")
def procesar_pedido(request):
    """
    Procesa el pedido realizado y envía email al usuario
    que efectuó el pedido.
    """
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
    info_compra = carro.get_compra_str()
    carro.limpia_carro()

    # mandamos el email con el pedido
    texto_compra = envio_email(
        pedido=pedido, 
        compra=info_compra, 
        total_compra=total_compra,
        usuario=request.user)

    return render(
        request, "exito.html", {"compra": texto_compra})





def envio_email(pedido, compra, total_compra, usuario):
    """
    Envía email al usuario que realizó el pedido
    - pedido: instancia de modelo Pedido
    - compra: String
    - total_compra: Float
    - usuario: SimpleLazyObject
    """
    msg = f"Estimado {usuario.username}\nEl pedido ID:{pedido} fue realizado con éxito.\nSu carro de compras es el siguiente:\n\n{compra}\nEl total de la compra es: CLP${total_compra}\nMuchas gracias."
    print(msg, type(msg))
    send_mail(
        subject="Pedido Realizado",
        message=msg,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[usuario.email]
    )

    return msg



#----- pdf esto aun no esta terminado -----#
def generar_pdf(request):
    if request.method == "POST":
        compra = request.POST.get("compra")

        html_string = render_to_string(
            template_name="exito.html",
            context={"compra": compra},
            request=request)

        print("render\n", html_string)
        # Crea un objeto HTML a partir del string
        html = HTML(string=html_string)

        # Genera el PDF
        pdf_file = html.write_pdf()

        # Crea una respuesta HTTP con el contenido del PDF
        response = HttpResponse(pdf_file, content_type='pdf')
        response['Content-Disposition'] = 'attachment; filename="archivo.pdf"'
        return response
