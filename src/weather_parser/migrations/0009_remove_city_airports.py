# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-30 07:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather_parser', '0008_airport_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='airports',
        ),
    ]
