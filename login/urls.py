from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = 'accounts'


urlpatterns = [
    path("cadastro/", views.Cadastrar, name="cadastro"),
    path("accounts/login/", views.Login, name="login"),
    path('', views.Sair, name='sair'),
]
