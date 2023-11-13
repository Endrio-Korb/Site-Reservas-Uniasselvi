from django.urls import path

from .views import CriarReservaSala, AtualizarReservaLaboratorio, AtualizarReservaSala
from .views import DeletarReservaLaboratorio, DeletarReservaSala
from . import views

app_name = "reservas"

app_name = 'reservas'

urlpatterns = [
    #path('laboratorio/', views.MostrarRegistroLaboratorio, name='reservar_laboratorio'),
    path('laboratorio/',  views.ReservarLaboratorio, name='reservar_laboratorio'),
    path('sala/', CriarReservaSala.as_view(), name='reservar_sala'),
    path('editar/laboratorio/<int:pk>', AtualizarReservaLaboratorio.as_view(), name="editar_laboratorio"),
    path('editar/sala/<int:pk>', AtualizarReservaSala.as_view(), name="editar_sala"),
    path('excluir/laboratorio/<int:pk>', DeletarReservaLaboratorio.as_view(), name="excluir_laboratorio"),
    path('excluir/sala/<int:pk>', DeletarReservaSala.as_view(), name="excluir_sala"),
]

