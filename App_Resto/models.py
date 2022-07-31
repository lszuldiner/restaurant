from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Clientes(models.Model):
    
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self) -> str:
        return f'{self.nombre} - {self.direccion} - {self.email}'

    class Meta():
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

class Productos(models.Model):
    
    nombre = models.CharField(max_length=150)
    precio = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.nombre} - {self.precio}'

    class Meta():
        verbose_name = 'Plato'
        verbose_name_plural = 'Platos'

class Pedidos(models.Model):
    
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.numero} - {self.fecha} - {self.entregado}'

    class Meta():
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

class Consultas(models.Model):
    
    nombre = models.CharField(max_length=30)
    asunto = models.CharField(max_length=50)
    email = models.EmailField()
    mensaje = models.CharField(max_length=150)

    def __str__(self) -> str:
        return f'{self.nombre} - {self.asunto} - {self.email} - {self.mensaje}'

    class Meta():
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'