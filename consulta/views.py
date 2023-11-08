from django.shortcuts import render

from reservas.models import ReservasLaboratorios, ReservasSalas


def consulta(request):
    return render(request, "consulta.html")


def mostrarEnsalamentoLabs(request):
    bloco = request.POST.get('bloco')
    bloco = bloco.upper()
    if request.method == "POST":
        if bloco == "A" or bloco == "B" or bloco =="C":
            data = request.POST.get('data')           
            laboratorios_reservados = ReservasLaboratorios.objects.filter(data_reserva=data).filter(bloco=bloco).order_by("nome_laboratorio")
            return render(request, "ensalamento_labs.html", {"laboratorios_reservados": laboratorios_reservados})
        else:
            mensagem = "Bloco Inválido"
            return render(request, "consulta.html", {"mensagem": mensagem})

def MostrarEnsalamentoSalas(request):
    bloco = request.POST.get('bloco')
    salas = ReservasSalas.objects.all().filter(bloco=bloco).order_by("numero_sala")
    return render(request, "ensalamento_salas.html", {"salas":salas})