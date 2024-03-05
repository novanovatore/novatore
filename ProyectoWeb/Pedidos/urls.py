from django.urls import path
from . import views

urlpatterns = [
    path("", views.procesar_pedido, name="pedido"),
    #path("descargar/", views.descargar_pdf, name="descargar_pdf"),
]
