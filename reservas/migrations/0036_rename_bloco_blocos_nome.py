# Generated by Django 4.2.7 on 2023-12-01 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0035_alter_laboratorios_bloco_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blocos',
            old_name='bloco',
            new_name='nome',
        ),
    ]