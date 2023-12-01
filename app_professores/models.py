from django.db import models

class Professores(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = 'tb_professores'
