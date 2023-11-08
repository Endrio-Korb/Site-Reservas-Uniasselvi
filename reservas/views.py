from .models import ReservasLaboratorios, ReservasSalas, Laboratorios
from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect



from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy
# Create your views here.
class CriarReservaLaboratorio(CreateView):
        model = ReservasLaboratorios
        fields = ['nome_laboratorio', 'data_reserva', 'nome_professor', 'periodo', 'estado', 'bloco']
        template_name = 'reserva_laboratorio.html'
        mensagem="Reserva registrada"
        success_url = reverse_lazy('consulta:consulta')


class CriarReservaSala(CreateView):
    model = ReservasSalas
    fields = ['nome_professor', 'numero_sala', 'periodo', 'bloco']
    template_name = 'reserva_salas.html'
    success_url = reverse_lazy('consulta:consulta')

class AtualizarReservaLaboratorio(UpdateView):
    model = ReservasLaboratorios
    fields = ['nome_laboratorio', 'data_reserva', 'nome_professor', 'periodo', 'estado', 'bloco']
    template_name = 'reserva_laboratorio.html'
    success_url = reverse_lazy('consulta:consulta')

class AtualizarReservaSala(UpdateView):
    model = ReservasSalas
    fields = ['nome_professor', 'numero_sala', 'periodo', 'bloco']
    template_name = 'reserva_salas.html'
    success_url = reverse_lazy('consulta:consulta')


class DeletarReservaLaboratorio(DeleteView):
    model = ReservasLaboratorios
    template_name = 'excluir.html'
    success_url = reverse_lazy('consulta:consulta')


class DeletarReservaSala(DeleteView):
    model = ReservasSalas
    template_name = 'excluir.html'
    success_url = reverse_lazy('consulta:consulta')