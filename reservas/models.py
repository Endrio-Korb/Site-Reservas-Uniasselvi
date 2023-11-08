from django.db import models
   
class Status(models.Model):
    id_status = models.IntegerField(null=False, blank=False)
    nome_status = models.CharField(max_length=20, null=False, blank=False)

    class Meta:
        db_table = "tb_status"

    def __str__(self):
        return self.nome_status
    

class Laboratorios(models.Model):

    nome = models.CharField(max_length=100, null=False, blank=False)
    bloco = models.CharField(max_length=1, null=False, blank=False)
    numero_sala = models.IntegerField(null=False, blank=False)
    capacidade = models.IntegerField(null=False, blank=False)

    class Meta:
        db_table = "tb_laboratorios"

    def __str__(self):
        return "{} {}{} ".format(self.nome ,self.bloco, self.numero_sala)
    

class ReservasLaboratorios(models.Model):

    nome_laboratorio = models.ForeignKey(Laboratorios, on_delete=models.CASCADE)
    data_reserva = models.DateField()
    nome_professor = models.CharField(max_length=100, null=False, blank=False)
    periodo = models.CharField(max_length=20, null=False, blank=False)
    estado = models.ForeignKey(Status, on_delete=models.CASCADE)
    bloco = models.CharField(max_length=1, null=False, blank=False)

    class Meta:
        db_table = "tb_reservas_laboratorios"

    def __str__(self):
        return "{} {} {} {}".format(self.nome_laboratorio,self.nome_professor, self.data_reserva, self.periodo)


class Salas(models.Model):

    numero_sala = models.CharField(max_length=5,null=False, blank=False)
    bloco = models.CharField(max_length=1, null=False, blank=False)
    capacidade = models.IntegerField(null=False, blank=False)

    class Meta:
        db_table = "tb_salas"

    def __str__(self):
        return "{} {}".format(self.numero_sala, self.bloco)
    

class ReservasSalas(models.Model):

    nome_professor = models.CharField(max_length=100, null=False, blank=False)
    numero_sala = models.IntegerField(null=False, blank=False)
    periodo = models.CharField(max_length=20, null=False, blank=False)
    bloco = models.CharField(max_length=1, null=False, blank=False)

    class Meta:
        db_table = "tb_reserva_salas"

    def __str__(self):
        return "{}{} {} {}".format(self.bloco, self.numero_sala, self.nome_professor, self.periodo)