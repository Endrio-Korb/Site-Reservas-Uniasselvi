# Generated by Django 4.2.3 on 2023-07-11 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0017_rename_nome_sala_reservassalas_numero_sala'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservassalas',
            name='bloco',
            field=models.CharField(default='X', max_length=1),
        ),
    ]
