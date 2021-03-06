# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-15 03:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='owing',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='owing_since',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='help_request',
            name='solved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='help_request',
            name='start',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='value',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='transaction_type',
            name='name',
            field=models.CharField(choices=[('Saque', 'Saque'), ('Depósito', 'Depósito'), ('Pagamento de Extrato', 'Pagamento de Extrato'), ('Juros sobre saldo negativo', 'Juros sobre saldo negativo'), ('Transferência bancária', 'Transferência bancária'), ('Pagamento de taxa de transferência bancária', 'Pagamento de taxa de transferência bancária'), ('Solicitação de visita do gerente', 'Solicitação de visita do gerente')], max_length=50),
        ),
    ]
