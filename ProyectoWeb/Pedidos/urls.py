from django.urls import path
from . import views

urlpatterns = [
    path("", views.procesar_pedido, name="pedido"),
    path("generar_pdf/", views.generar_pdf, name="generar_pdf"),
]
