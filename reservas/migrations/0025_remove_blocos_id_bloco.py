# Generated by Django 4.2.3 on 2023-11-06 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0024_alter_laboratorios_bloco'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blocos',
            name='id_bloco',
        ),
    ]
