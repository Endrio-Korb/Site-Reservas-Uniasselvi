from django.db import models
   
class Status(models.Model):
    id_status = models.IntegerField(null=False, blank=False)
    nome_status = models.CharField(max_length=20, null=False, blank=False)

    class Meta:
        db_table = "tb_status"

    def __str__(self):
        return self.nome_status
    
class Periodos(models.Model):
    id_periodo = models.IntegerField(null=False, blank=False)
    nome_periodo = models.CharField(max_length=20, null=False, blank=False)
  
    class Meta:
        db_table = "tb_periodos"

    def __str__(self):
        return self.nome_periodo


class Blocos(models.Model):
    id_bloco = models.IntegerField(null=False, blank=False)
    bloco = models.CharField(max_length=1, null=False, blank=False, default='x')
  
    class Meta:
        db_table = "tb_blocos"

    def __str__(self):
        return self.bloco


class Laboratorios(models.Model):
    blocos = [
        ('A', 'Bloco A'),
        ('B', 'Bloco B'),
        ('C', 'Bloco C'),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    bloco = models.CharField(max_length=1, choices=blocos ,null=False, blank=False)
    numero_sala = models.IntegerField(null=False, blank=False)
    capacidade = models.IntegerField(null=False, blank=False)

    class Meta:
        db_table = "tb_laboratorios"

    def __str__(self):
        return "{} {}{} ".format(self.nome ,self.bloco, self.numero_sala)
    

class ReservasLaboratorios(models.Model):
    blocos = [
        ('A', 'Bloco A'),
        ('B', 'Bloco B'),
        ('C', 'Bloco C'),
    ]

    periodos = [
        ('Matutino', 'Matutino'),
        ('Vespertino', 'Vespertino'),
        ('Noturno', 'Noturno'),
    ]

    nome_laboratorio = models.ForeignKey(Laboratorios, on_delete=models.CASCADE)
    data_reserva = models.DateField()
    nome_professor = models.CharField(max_length=100, null=False, blank=False)
    periodo = models.CharField(max_length=20, choices=periodos,null=False, blank=False)
    bloco = models.CharField(max_length=1, choices=blocos ,null=False, blank=False)

    class Meta:
        db_table = "tb_reservas_laboratorios"

    def __str__(self):
        return "{} {} {} {}".format(self.nome_laboratorio,self.nome_professor, self.data_reserva, self.periodo)
