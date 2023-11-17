from django.urls import path

from . import views

app_name = "reservas"

urlpatterns = [
    path('laboratorio/',  views.ReservarLaboratorio, name='reservar_laboratorio'),
    path('laboratorio/',  views.reservaLaboratorioP2, name='reservar_laboratorio_p2'),
]

