# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_parser', '0007_auto_20151227_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='airport',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
