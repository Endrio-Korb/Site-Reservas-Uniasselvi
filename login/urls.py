from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

from . import views

app_name = 'accounts'


urlpatterns = [
    #path("cadastro/", views.Cadastrar, name="cadastro"),
    #path("accounts/login/", views.Login, name="login"),
    #path('accounts/sair', views.Sair, name='sair'),

    path('entrar/', auth_views.LoginView.as_view(
        template_name='login/entrar.html'
    ), name='entrar'),
]
