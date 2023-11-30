from .models import ReservasLaboratorios, Laboratorios
from .models import Periodos, Blocos

from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .forms import LocationForm

from consulta import views

# def registrarReservarLaboratorio(request):

#     if request.method == 'POST':
#         bloco =  request.POST.get('blocos')
#         nome_professor = request.POST.get('nome_professor')
#         data = request.POST.get('data')
#         periodo = request.POST.get('periodo')
#         nome_lab = request.POST.get('nome_lab')

#         nome_lab = nome_lab[:-6]
#         lab = Laboratorios.objects.only('id').get(nome=nome_lab).id
#         laboratorio = ReservasLaboratorios.objects.filter(nome_laboratorio=lab).filter(data_reserva=data).filter(bloco=bloco)

#         if laboratorio:
#             mensagem = f'{nome_lab} já está reservado para data {data} e periodo {periodo}'
#             return render(request, 'consulta.html', {'mensagem': mensagem})
#         else:
#             reserva = ReservasLaboratorios.objects.create(
#                 nome_laboratorio = Laboratorios.objects.get(nome=nome_lab),
#                 nome_professor = f'{nome_professor}',
#                 data_reserva = f'{data}',
#                 periodo = f'{periodo}',
#                 bloco = f'{bloco}',
#             )
#             reserva.save()
#             mensagem = 'Reserva registrada com sucesso'
#             return render(request, 'consulta.html', {'mensagem': mensagem})
#     else:
#         labs = Laboratorios.objects.all().order_by('bloco')
#         blocos = Blocos.objects.all().order_by('bloco')
#         periodos = Periodos.objects.all().order_by('id_periodo')

 
#         return render(request, 'reserva_laboratorio.html',{'labs':labs,
#                                                            'blocos':blocos,
#                                                            'periodos':periodos} )

def ReservarLaboratorio(request):
    blocos = Blocos.objects.all()
    contexto = {'blocos': blocos}
    return render(request, 'reserva_labs.html', contexto)


def modules(request):
    bloco = request.GET.get('blocos')

    laboratorios = Laboratorios.objects.filter(bloco_id=bloco)
    periodos = Periodos.objects.all()

    contexto = {'laboratorios': laboratorios,
                'periodos':periodos,}
    return render(request, 'partials/modules.html', contexto)


def registrarReservarLaboratorio(request):
    blocos = Blocos.objects.all()
    

    if request.method == 'POST':
        bloco = request.POST.get('blocos')
        data = request.POST.get('data')
        periodo = request.POST.get('periodo')
        lab = request.POST.get('nome_lab')
        professor = request.POST.get('nome_professor')

        verificar_reserva = ReservasLaboratorios.objects.filter(nome_laboratorio_id=lab).filter(data_reserva=data).filter(bloco_id=bloco)

        if verificar_reserva:
            nome_lab = Laboratorios.objects.get(id=lab)
            str_periodo = Periodos.objects.get(id=periodo)

            mensagem = f'{nome_lab} já está reservado no periodo {str_periodo} para data {data} '
            contexto = {'blocos': blocos,
                         'mensagem': mensagem}
            return render(request, 'consulta.html', {'contexto':contexto})
        
        else:
            reserva = ReservasLaboratorios.objects.create(
                data_reserva = f'{data}',
                nome_professor = f'{professor}',
                periodo_id = f'{periodo}',
                nome_laboratorio = Laboratorios.objects.get(id=lab),
                bloco_id = f'{bloco}',
            )
            reserva.save()
            mensagem = 'Reserva registrada com sucesso'
            contexto = {'blocos': blocos,
                        'mensagem': mensagem}
            return render(request, 'consulta.html', {'contexto': contexto})

