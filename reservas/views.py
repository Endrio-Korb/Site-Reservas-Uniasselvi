from .models import ReservasLaboratorios, Laboratorios
from .models import Periodos, Blocos

from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .forms import LocationForm

from professores.models import Professores

from consulta import views


from datetime import date

def ReservarLaboratorio(request):
    blocos = Blocos.objects.all()
    professores = Professores.objects.all()
    return render(request, 'reserva_labs.html', {'blocos': blocos,
                                                 'professores':professores})


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
            professor = professor.lower()
            professor = professor.title()

            salva_nome_professor = Professores.objects.create(
               nome = f'{professor}'
           )
            salva_nome_professor.save()

            reserva = ReservasLaboratorios.objects.create(
                data_reserva = f'{data}',
                nome_professor = f'{professor}',
                periodo_id = f'{periodo}',
                nome_laboratorio = Laboratorios.objects.get(id=lab),
                bloco_id = f'{bloco}',
            )
            reserva.save()
            mensagem = 'Reserva registrada com sucesso'
            return render(request, 'consulta.html', {'blocos': blocos,
                                                      'mensagem': mensagem})
        
