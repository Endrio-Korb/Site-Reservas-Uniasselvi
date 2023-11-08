from django.urls import path

from . import views

app_name='consulta'

urlpatterns = [
    path("", views.consulta, name='consulta'),
    path('ensalamento_labs/', views.mostrarEnsalamentoLabs, name="ensalamento_labs"),
    path('ensalamento_salas/', views.MostrarEnsalamentoSalas, name="ensalamento_salas"),
]
