from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
# Create your views here.


def Login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(username=usuario, password=senha)

        if user:
            mensagem = "Logado com sucesso"
            return render(request,"consulta.html", {"mensagem": mensagem})
        else:
            mensagem = "Usuário ou senha errado"
            return render(request, "login.html", {"mensagem": mensagem})


def Cadastrar(request):
    if request.method == "GET":
        return render(request, "cadastro.html")
    else:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        user = User.objects.filter(username=usuario).first()
        
        if user:
            mensagem = "Usuário já cadastrado"
            return render(request, "cadastro.html", {"mensagem": mensagem})
        else:
            if senha == confirmar_senha:
                user = User.objects.create_user(username=usuario, password=senha, is_staff=False )
                user.save()
                mensagem = 'Usuário cadastrado com sucesso'
                return render(request, "login.html", {"mensagem":mensagem})
            else:
                mensagem = "As senhas não são iguais"
                return render(request, "cadastro.html", {"mensagem":mensagem})
            

def Sair(request):
    logout(request)
    return render(request,'consulta.html')