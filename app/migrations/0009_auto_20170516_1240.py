# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-16 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20170516_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='help_request',
            name='start',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]