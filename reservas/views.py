from .models import ReservasLaboratorios, Laboratorios
from .models import Periodos, Blocos

from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


def ReservarLaboratorio(request):
    labs = Laboratorios.objects.all()
    blocos = Blocos.objects.all()
    periodos = Periodos.objects.all()

    if request.method == 'GET':
        return render(request, 'reserva_laboratorio_p1.html', {'labs': labs,
                                                            'blocos': blocos,
                                                            'periodos':periodos})
    else:
       return reservaLaboratorioP2(request)
    # else:
    #     bloco =  request.POST.get('bloco')
    #     data = request.POST.get('data')
    #     nome_lab = request.POST.get('nome_lab')
    #     nome_professor = request.POST.get('nome_professor')
    #     periodo = request.POST.get('periodo')

    #     nome_lab = nome_lab[:-6]
    #     lab = Laboratorios.objects.only('id').get(nome=nome_lab).id
    #     laboratorio = ReservasLaboratorios.objects.filter(nome_laboratorio=lab).filter(data_reserva=data).filter(bloco=bloco)
        
        

    #     if laboratorio:
    #         mensagem = f'{nome_lab} já está reservado para data {data} e periodo {periodo}'
    #         return render(request, 'reserva_laboratorio.html', {'mensagem': mensagem,
    #                                                             'labs': labs,
    #                                                             'blocos': blocos,
    #                                                             'periodos':periodos})
    #     else:
    #         reserva = ReservasLaboratorios.objects.create(
    #             nome_laboratorio = Laboratorios.objects.get(nome=nome_lab),
    #             data_reserva = f'{data}',
    #             nome_professor = f'{nome_professor}',
    #             periodo = f'{periodo}',
    #             bloco = f'{bloco}',
    #         )
    #         reserva.save()
    #         mensagem = 'Reserva registrada com sucesso'
    #         return render(request, 'consulta.html', {'mensagem': mensagem})

def reservaLaboratorioP2(request):
    bloco = request.POST.get('bloco')
    periodo = request.POST.get('periodo')
    data = request.POST.get('data')
    
    bloco = bloco.upper()

        
    laboratorios = Laboratorios.objects.filter(bloco=bloco).order_by('nome')

    labs_disponiveis = {}
    lista_labs = []
    info_labs = []
    contador = 0

    for lab in laboratorios:
        labs_disponiveis[f'{lab}'] = f'{lab}'

    labs_reservados = ReservasLaboratorios.objects.filter(bloco=bloco).filter(data_reserva=data).order_by('nome_laboratorio')
    
    if labs_reservados:
        for lab_reservado in labs_reservados:
            lab_reservado = str(lab_reservado)
            lista_labs.append(lab_reservado.split())
            info_labs = lista_labs[contador]
            nome_lab = f'{info_labs[0]} {info_labs[1]} {info_labs[2]} {info_labs[3]} {info_labs[4]} '
            contador += 1
            labs_disponiveis.pop(nome_lab)
    
    return render(request, 'reserva_laboratorio_p2.html', {'data':data,
                                                            'periodo':periodo,
                                                            'bloco':bloco,
                                                            'labs_disponiveis': labs_disponiveis})