from django.contrib import admin

from .models import Laboratorios, Salas, ReservasLaboratorios, ReservasSalas, Status
admin.site.register(Laboratorios)
admin.site.register(Salas)
admin.site.register(ReservasLaboratorios)
admin.site.register(ReservasSalas)
admin.site.register(Status)