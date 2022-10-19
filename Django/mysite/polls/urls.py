from django.urls import path
from .views import ListaInventario

from polls import views

urlpatterns = [
    path('', ListaInventario.as_view(), name='Inventario')

]

