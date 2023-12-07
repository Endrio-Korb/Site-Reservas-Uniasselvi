from django.shortcuts import render, HttpResponse

from reservas.models import ReservasLaboratorios, Laboratorios, Blocos

from django.db.models import Value as V
from django.db.models.functions import Concat
from django import forms


def consulta(request):
    blocos = Blocos.objects.all()
    return render(request, "consulta.html", {'blocos':blocos})


def mostrarEnsalamentoLabs(request):

    if request.method=="POST":
            
        bloco = request.POST.get('bloco')
        data = request.POST.get('data')
    
        blocos = Blocos.objects.all()

        

        if not data or bloco == int:
            mensagem = 'Data ou Bloco faltando'
            return render(request, 'consulta.html', {'mensagem':mensagem,
                                                     'blocos':blocos})

        laboratorios = Laboratorios.objects.filter(bloco_id=bloco).order_by('nome')

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

        nome_bloco = Blocos.objects.get(id_bloco=bloco)

        return render(request, 'ensalamento_labs.html', {'labs_disponiveis': labs_disponiveis,
                                                        'labs_reservados':labs_reservados,
                                                        'data':data,
                                                        'nome_bloco':nome_bloco})




def mostrarEnsalamentoLabsNome(request):
    data = request.POST.get('data')
    nome_prof = request.POST.get('nome_professor')
    nome_prof = nome_prof.upper()

    if not data or not nome_prof:
        blocos = Blocos.objects.all()
        mensagem = 'Data ou nome do professor faltando'
        return render(request, 'consulta.html', {'mensagem':mensagem,
                                                 'blocos':blocos})

    labs_reservados = ReservasLaboratorios.objects.annotate(full_name=Concat('nome_professor', V(' '))).filter(full_name__icontains=nome_prof).filter(data_reserva=data).order_by('nome_laboratorio')

    return render(request, 'ensalamento_labs_nome.html', {'labs_reservados': labs_reservados,
                                                          'data': data})