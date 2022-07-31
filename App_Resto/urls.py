from django.contrib import admin
from django.urls import path

from App_Resto.models import Clientes, Pedidos, Productos

from .views import buscar, busquedaProducto, consultas, contacto, inicio, menu, nosotros

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('menu/', menu, name="Menu"),
    path('consultas/', consultas, name="Consultas"),
    path('nosotros/', nosotros, name="Nosotros"),
    path('busquedaProducto/', busquedaProducto, name="BusquedaProducto"),
    path('contacto/', contacto, name="Contacto"),
    path('buscar/', buscar, name="Buscar"),
    ]