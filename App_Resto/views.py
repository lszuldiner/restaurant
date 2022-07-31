from django.http import HttpResponse
from django.shortcuts import render
from django.urls import is_valid_path

from App_Resto.forms import ContactoFormulario
from App_Resto.models import Consultas, Productos

# Create your views here.
def inicio(self):
    return render(self, "inicio.html")

def menu(self):
    return render(self, "menu.html")

def consultas(self):
    return render(self, "contacto.html")

def contacto(request):
    if request.method=="POST":

        miFormulario = ContactoFormulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            consulta = Consultas(nombre=data.POST['nombre'], asunto=data.POST['asunto'], email=data.POST['email'], mensaje=data.POST['mensaje'])

            consulta.save()

            return render(request, "gracias.html")
        
    else:

        miFormulario = ContactoFormulario()

        return render(request, "contacto.html", {"miFormulario": miFormulario})

    
    return render(request, "contacto.html")

def nosotros(self):
    return render(self, "nosotros.html")

def busquedaProducto(request):
    return render(request, "busquedaProducto.html")

def buscar(request):

    if request.GET["prd"]:

        producto=request.GET["prd"]

        productos=Productos.objects.filter(nombre__icontains=producto)
        
        return render(request, "resultadoBusqueda.html", {"productos": productos, "producto": producto})
    
    else:
        mensaje ="No se ha introducido nada"

    return render(request, "resultadoBusqueda.html")


