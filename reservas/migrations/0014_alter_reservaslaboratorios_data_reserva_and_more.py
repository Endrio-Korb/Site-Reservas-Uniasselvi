# Generated by Django 4.2.3 on 2023-07-10 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0013_alter_reservaslaboratorios_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservaslaboratorios',
            name='data_reserva',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='reservaslaboratorios',
            name='periodo',
            field=models.CharField(default='Noturno', max_length=20),
        ),
    ]
