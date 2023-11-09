# Generated by Django 4.2.3 on 2023-11-06 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0020_blocos_status_delete_mes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_periodo', models.IntegerField(max_length=2)),
                ('nome_periodo', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='salas',
            name='reservada',
        ),
        migrations.AlterField(
            model_name='reservaslaboratorios',
            name='bloco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.blocos'),
        ),
        migrations.AlterField(
            model_name='reservaslaboratorios',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.status'),
        ),
        migrations.AlterField(
            model_name='reservassalas',
            name='bloco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.blocos'),
        ),
        migrations.AlterField(
            model_name='salas',
            name='bloco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.blocos'),
        ),
        migrations.AlterField(
            model_name='reservaslaboratorios',
            name='periodo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.periodo'),
        ),
        migrations.AlterField(
            model_name='reservassalas',
            name='periodo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.periodo'),
        ),
    ]