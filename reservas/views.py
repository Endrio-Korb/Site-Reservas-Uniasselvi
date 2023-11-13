from .models import ReservasLaboratorios, ReservasSalas, Laboratorios
from .models import Periodos, Blocos

from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from consulta.views import mostrarEnsalamentoLabs

# Create your views here.
# class CriarReservaLaboratorio(CreateView):
        
#         model = ReservasLaboratorios
#         fields = ['nome_laboratorio', 'data_reserva', 'nome_professor', 'periodo', 'bloco']
#         template_name = 'reserva_laboratorio.html'
#         mensagem="Reserva registrada"
#         success_url = reverse_lazy('consulta:consulta')


def ReservarLaboratorio(request):
    if request.method == 'GET':
        return render(request, 'reserva_laboratorio.html')
    else:
        bloco =  request.POST.get('bloco')
        data = request.POST.get('data')
        nome_lab = request.POST.get('nome_lab')

        lista = [bloco, data, nome_lab]
        return HttpResponse(lista)
        # laboratorio = ReservasLaboratorios.objects.filter(nome_laboratorio=nome_lab).filter(data_reserva=data).filter(bloco=bloco)
        # if laboratorio:
        #     return HttpResponse('Laboratório indisponível')
        # else:

# def CriarReservaLaboratorio(request):
#     nome_lab = request.POST.get('nome_lab')
#     data = request.POST.get('data_reserva')
#     nome_prof = request.POST.get('nome_professor')
#     periodo = request.POST.get('periodo')
#     bloco =  request.POST.get('bloco')

#     lab_reservados = ReservasLaboratorios.objects.filter(data_reserva=data).filter(bloco=bloco).filter(periodo)
#     if lab_reservados:
#         mensagem = f'O {nome_lab} já está reservado na data {data} e no periodo {periodo}'
#         return render(request, 'reserva_laboratorio.html', {'mensagem': mensagem})
#     else:
#         reserva = ReservasLaboratorios.objects.create(
#             nome_laboratorio = f'{nome_lab}',
#             data_reserva = f'{data}',
#             nome_professor = f'{nome_prof}',
#             periodo = f'{periodo}',
#             bloco = f'{bloco}',
#         )
#         reserva.save()
#         mensagem = 'Reserva registrada com sucesso'
#         return render(request, 'consulta.html', {'mensagem':mensagem})


class CriarReservaSala(CreateView):
    model = ReservasSalas
    fields = ['nome_professor', 'numero_sala', 'periodo', 'bloco']
    template_name = 'reserva_salas.html'
    success_url = reverse_lazy('consulta:consulta')

class AtualizarReservaLaboratorio(UpdateView):
    model = ReservasLaboratorios
    fields = ['nome_laboratorio', 'data_reserva', 'nome_professor', 'periodo', 'bloco']
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