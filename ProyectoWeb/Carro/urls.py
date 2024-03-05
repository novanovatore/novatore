from django.urls import path
from . import views


# creamos un especie de namespace
# para que sea mas facil usar las urls de carro
app_name = "carro"

urlpatterns = [
    path("agregar/<int:producto_id>/", views.agrega_producto, name="agregar"),
    path("eliminar/<int:producto_id>/", views.elimina_producto, name="eliminar"),
    path("resta/<int:producto_id>/", views.resta_producto, name="restar"),
    path("limpia/", views.limpia_carro, name="limpiar"),

]
