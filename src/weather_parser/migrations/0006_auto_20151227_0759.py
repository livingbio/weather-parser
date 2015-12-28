# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_parser', '0005_airport_icao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='altitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='airport',
            name='timezone',
            field=models.FloatField(null=True),
        ),
    ]
