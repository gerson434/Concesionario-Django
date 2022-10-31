from django.urls import path
from .views import *

from polls import views

urlpatterns = [
    path('', ListaInventario.as_view(), name='Inventario'),
    path('<int:pk>', DetalleInventario.as_view(), name='DetalleInventario')


]

