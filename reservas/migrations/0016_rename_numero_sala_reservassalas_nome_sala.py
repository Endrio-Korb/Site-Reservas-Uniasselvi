# Generated by Django 4.2.3 on 2023-07-11 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0015_alter_reservaslaboratorios_data_reserva'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservassalas',
            old_name='numero_sala',
            new_name='nome_sala',
        ),
    ]