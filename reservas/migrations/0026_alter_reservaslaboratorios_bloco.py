# Generated by Django 4.2.3 on 2023-11-06 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0025_remove_blocos_id_bloco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservaslaboratorios',
            name='bloco',
            field=models.CharField(max_length=1),
        ),
    ]
