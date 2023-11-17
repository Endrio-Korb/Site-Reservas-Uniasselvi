from django.shortcuts import render, HttpResponse

from reservas.models import ReservasLaboratorios, Laboratorios

from django.db.models import Value as V
from django.db.models.functions import Concat


def consulta(request):
    return render(request, "consulta.html")


def mostrarEnsalamentoLabs(request):
    bloco = request.POST.get('blocos')
    bloco = bloco.upper()
    data = request.POST.get('data')

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

    return render(request, 'ensalamento_labs.html', {'labs_disponiveis': labs_disponiveis,
                                                     'labs_reservados':labs_reservados,
                                                     'data':data,
                                                     'bloco':bloco})


def mostrarEnsalamentoNome(request):
    data = request.POST.get('data')
    nome_prof = request.POST.get('nome_professor')

    labs_reservados = ReservasLaboratorios.objects.annotate(full_name=Concat('nome_professor', V(' '))).filter(full_name__icontains=nome_prof).filter(data_reserva=data).order_by('nome_laboratorio')

    return render(request, 'ensalamento_labs_nome.html', {'labs_reservados': labs_reservados,
                                                          'data':data})