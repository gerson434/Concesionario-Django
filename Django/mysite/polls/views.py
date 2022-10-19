from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Inventario

# Create your views here.
class ListaInventario(ListView):
    model = Inventario
