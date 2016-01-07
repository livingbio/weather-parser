# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-07 07:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_parser', '0009_remove_city_airports'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='airport_id',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='airport',
            name='altitude',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='airport',
            name='city_name',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='airport',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='airport',
            name='country_name',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='airport',
            name='dst',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='airport',
            name='iata',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='airport',
            name='icao',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='airport',
            name='latitude',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='airport',
            name='longitude',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='airport',
            name='name',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='airport',
            name='timezone',
            field=models.FloatField(blank=True),
        ),
    ]