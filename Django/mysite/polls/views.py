from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Inventario

# Create your views here.
class ListaInventario(ListView):
    model = Inventario
    context_object_name = "inventario"

class DetalleInventario(ListView):
    model = Inventario
    template_name = "polls/detalle_inventario.html"
    context_object_name = "inventario"
