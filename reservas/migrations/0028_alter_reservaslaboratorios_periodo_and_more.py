# Generated by Django 4.2.3 on 2023-11-06 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0027_alter_laboratorios_bloco_alter_reservassalas_bloco_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservaslaboratorios',
            name='periodo',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='reservassalas',
            name='periodo',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='Periodo',
        ),
    ]
