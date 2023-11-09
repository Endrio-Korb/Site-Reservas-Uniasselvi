# Generated by Django 4.2.3 on 2023-11-06 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0019_reservaslaboratorios_bloco_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blocos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_bloco', models.IntegerField(max_length=2)),
                ('nome_bloco', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'tb_blocos',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_status', models.IntegerField(max_length=2)),
                ('nome_status', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'tb_status',
            },
        ),
        migrations.DeleteModel(
            name='Mes',
        ),
        migrations.AlterField(
            model_name='reservaslaboratorios',
            name='bloco',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='reservaslaboratorios',
            name='periodo',
            field=models.CharField(default='Vespertino', max_length=20),
        ),
    ]