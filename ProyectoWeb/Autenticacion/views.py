from django.shortcuts import render, redirect
from django.views.generic import View
#from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreationForm


from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.


class VistaRegistro(View):

    def get(self, request):
        # encargado de mostrar el formulario

        # este es el formulario para crear usuarios
        form = UserCreationForm()

        return render(request, "registro/registro.html", {"form": form})

    def post(self, request):
        # encargardo de enviar los datos a la bd
        # el objeto request si se envía por post transporta todos
        # los datos enviados por el usuario en el formulario

        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            # si el formulario es valido guardalo en la base de datos  
            usuario = form.save() 

            # si se guarda en la bd, redirige al usuario al home y
            # loguea automaticamente al usuario recien registrado
            login(request, usuario)

            return redirect("home")
        
        else:
            messages.error(request, "ERROR en registro")
            
            return render(request, "registro/registro.html", {"form": form})


def cerrar_sesion(request):
    logout(request)

    return redirect("home")


def loguear_usuario(request):
    form = AuthenticationForm()
    if request.method == "POST":
        # guardamos la data enviada por el usuario
        form = AuthenticationForm(request, request.POST)

        # si el formulario es valido
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            # comparamos con la info que está en la bd
            usuario = authenticate(username=username, password=password)

            # si es correcta la info, entonces usuario != None
            if usuario is not None:
                login(request, usuario)
                return redirect("home")
            else:
                messages.error(request, "Error: No se encuentra el usuario")
                
        else:
            messages.error(request, "Error: Datos incorrectos")
            

    return render(request, "login/login.html", {"form": form})