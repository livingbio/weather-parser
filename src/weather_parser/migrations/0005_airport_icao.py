# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_parser', '0004_airport_iata'),
    ]

    operations = [
        migrations.AddField(
            model_name='airport',
            name='icao',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]