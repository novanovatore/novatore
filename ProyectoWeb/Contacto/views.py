from django.shortcuts import render, redirect
from .forms import *
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def contacto(request):
    formulario = FormularioContacto()
    
    if request.method == "POST": 
        formulario = FormularioContacto(data=request.POST)

        if formulario.is_valid():
            subject = "Mensaje de " + formulario.cleaned_data["nombre"]
            message = formulario.cleaned_data["contenido"] + " " + formulario.cleaned_data["email"]
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [settings.EMAIL_HOST_USER]

            url = reverse("contacto")
            
            try:
                send_mail(
                    subject, message, email_from, recipient_list
                )
                url += "?valido=1"
            except:
                url += "?valido=0"

            return redirect(url) 

    return render(request, "Contacto/contacto.html", {"formulario": formulario})

