from django.shortcuts import render

from reservas.models import ReservasLaboratorios, ReservasSalas, Laboratorios


def consulta(request):
    return render(request, "consulta.html")


def mostrarEnsalamentoLabs(request):
    bloco = request.POST.get('blocos')
    bloco = bloco.upper()
    data = request.POST.get('data')

    laboratorios = Laboratorios.objects.filter(bloco=bloco).order_by('nome')
    saida = {}
    lista_labs = []
    info_labs = []
    lista_saida = []
    item = 0
    for lab in laboratorios:
        saida[lab] = f'{lab}'

    laboratorio_reservado = ReservasLaboratorios.objects.filter(bloco=bloco).filter(data_reserva=data).order_by('nome_laboratorio')
    if laboratorio_reservado:
        for lab_reservado in laboratorio_reservado:
            #if saida[f'{lab}'] == lab:
            #       saida[f'{lab_reservado}'] = lab_reservado
            lab_reservado = str(lab_reservado)
            labs = lab_reservado.split()
            lista_labs.append(labs)
            info_labs = lista_labs[item]
            nome_lab = f'{info_labs[0]} {info_labs[1]} {info_labs[2]} {info_labs[3]} {info_labs[4]}'
            perido = f'{info_labs[-1]}'
            nome_professor = f'{info_labs[5:-2]}'

            if saida.get(nome_lab):
                saida[nome_lab] = f'{nome_lab} {nome_professor} {data} {perido}'

    for item in saida.keys():
        lista_saida.append(item)



    return render(request, 'ensalamento_labs.html', {'saida': saida})






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