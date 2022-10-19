from django.db import models

# Create your models here.
class Inventario(models.Model):
    placa = models.CharField(null=False, max_length=6)
    modelo = models.CharField(null=True, max_length=400)
    descripcion = models.TextField(max_length=200)
    disponiible=models.IntegerField(null=True)
    valor=models.IntegerField(null=False)