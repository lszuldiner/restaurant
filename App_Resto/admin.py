from django.contrib import admin

from App_Resto.models import Clientes, Consultas, Productos, Pedidos

# Register your models here.
admin.site.register(Clientes)
admin.site.register(Productos)
admin.site.register(Pedidos)
admin.site.register(Consultas)

