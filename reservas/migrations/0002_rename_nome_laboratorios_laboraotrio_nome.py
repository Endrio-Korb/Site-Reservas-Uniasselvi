# Generated by Django 4.2.2 on 2023-06-28 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='laboratorios',
            old_name='nome',
            new_name='laboraotrio_nome',
        ),
    ]