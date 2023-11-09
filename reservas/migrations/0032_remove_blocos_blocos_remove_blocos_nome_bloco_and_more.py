# Generated by Django 4.2.3 on 2023-11-09 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0031_blocos_periodos_alter_reservaslaboratorios_periodo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blocos',
            name='blocos',
        ),
        migrations.RemoveField(
            model_name='blocos',
            name='nome_bloco',
        ),
        migrations.AddField(
            model_name='blocos',
            name='bloco',
            field=models.CharField(default='x', max_length=1),
        ),
        migrations.AddField(
            model_name='blocos',
            name='id_bloco',
            field=models.IntegerField(default=0),
        ),
    ]