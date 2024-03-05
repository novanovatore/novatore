from django.urls import path
from .views import VistaRegistro, cerrar_sesion, loguear_usuario


urlpatterns = [
    path("", VistaRegistro.as_view(), name="auth_reg_user"),
    path("logout/", cerrar_sesion, name="logout"),
    path("login/", loguear_usuario, name="auth_login_user"),
]