# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 09:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_parser', '0006_auto_20151227_0759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='airport_code',
        ),
        migrations.AddField(
            model_name='city',
            name='airports',
            field=models.ManyToManyField(null=True, to='weather_parser.AirPort'),
        ),
    ]
