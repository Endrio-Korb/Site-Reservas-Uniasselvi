from .models import ReservasLaboratorios, Laboratorios
from .models import Periodos, Blocos

from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .forms import LocationForm

def ReservarLaboratorio(request):

    if request.method == 'POST':
        nome_lab = request.POST.get('nome_lab')
        nome_professor = request.POST.get('nome_professor')
        bloco =  request.POST.get('bloco')
        data = request.POST.get('data')
        periodo = request.POST.get('periodo')
        nome_lab = request.POST.get('nome_lab')

        lab = Laboratorios.objects.only('id').get(nome=nome_lab).id
        laboratorio = ReservasLaboratorios.objects.filter(nome_laboratorio=lab).filter(data_reserva=data).filter(bloco=bloco)

        if laboratorio:
            mensagem = f'{nome_lab} já está reservado para data {data} e periodo {periodo}'
            return render(request, 'reserva_laboratorio.html', {'mensagem': mensagem})
        else:
            reserva = ReservasLaboratorios.objects.create(
                nome_laboratorio = Laboratorios.objects.get(nome=nome_lab),
                nome_professor = f'{nome_professor}',
                data_reserva = f'{data}',
                periodo = f'{periodo}',
                bloco = f'{bloco}',
            )
            reserva.save()
            mensagem = 'Reserva registrada com sucesso'
            return render(request, 'consulta.html', {'mensagem': mensagem})
    else:
        labs = Laboratorios.objects.all().order_by('bloco')
        blocos = Blocos.objects.all().order_by('bloco')
        periodos = Periodos.objects.all().order_by('id_periodo')

 
        return render(request, 'reserva_laboratorio.html',{'labs':labs,
                                                           'blocos':blocos,
                                                           'periodos':periodos} )