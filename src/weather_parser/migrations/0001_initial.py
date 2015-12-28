# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-25 06:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255)),
                ('population', models.IntegerField(db_index=True)),
                ('altitude', models.IntegerField(db_index=True, null=True)),
                ('country', models.TextField(max_length=255)),
                ('latitude', models.FloatField(max_length=255)),
                ('longitude', models.FloatField(max_length=255)),
                ('airport_code', models.TextField(max_length=255, null=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weather_stats', jsonfield.fields.JSONField()),
                ('updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather_parser.City')),
            ],
        ),
    ]
