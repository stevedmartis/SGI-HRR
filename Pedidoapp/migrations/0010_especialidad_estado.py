# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pedidoapp', '0009_auto_20170319_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='especialidad',
            name='estado',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]