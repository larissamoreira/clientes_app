# Generated by Django 2.0.5 on 2018-05-15 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cep',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cidade',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='endereço',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='estado',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='país',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(max_length=11),
        ),
    ]