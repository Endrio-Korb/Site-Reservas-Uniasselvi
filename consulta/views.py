from django.shortcuts import render, HttpResponse

from reservas.models import ReservasLaboratorios, ReservasSalas, Laboratorios


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






# def mostrarEnsalamentoLabs(request):
#     bloco = request.POST.get('blocos')
#     bloco = bloco.upper()
#     if request.method == "POST":
#         if bloco == "A" or bloco == "B" or bloco =="C":
#             data = request.POST.get('data')           
#             laboratorios_reservados = ReservasLaboratorios.objects.filter(data_reserva=data).filter(bloco=bloco).order_by("nome_laboratorio")
#             return render(request, "ensalamento_labs.html", {"laboratorios_reservados": laboratorios_reservados})
#         else:
#             mensagem = "Bloco Inválido"
#             return render(request, "consulta.html", {"mensagem": mensagem})

def MostrarEnsalamentoSalas(request):
    bloco = request.POST.get('bloco')
    salas = ReservasSalas.objects.all().filter(bloco=bloco).order_by("numero_sala")
    return render(request, "ensalamento_salas.html", {"salas":salas})