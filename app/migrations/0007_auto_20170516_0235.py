# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-16 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20170516_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='owing_since',
            field=models.DateTimeField(null=True),
        ),
    ]
