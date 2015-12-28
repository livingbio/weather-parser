from __future__ import unicode_literals

from django.db import models
from jsonfield import JSONField

# Create your models here.


class AirPort(models.Model):    
    airport_id = models.CharField(max_length=1024, null=True)
    city_name = models.CharField(max_length=1024, null=True)
    country_name = models.CharField(max_length=1024, null=True)
    airport_id = models.CharField(max_length=1024, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    timezone = models.FloatField(null=True)
    dst = models.CharField(max_length=1024, null=True)
    name = models.CharField(max_length=1024, null=True)
    altitude = models.FloatField(null=True)
    iata = models.CharField(max_length=1024, null=True)
    icao = models.CharField(max_length=1024, null=True)
    content = models.TextField(null=True)

class City(models.Model):

    name = models.TextField(max_length=255)
    population = models.IntegerField(db_index=True)
    altitude = models.IntegerField(null=True, db_index=True)
    country = models.TextField(max_length=255)
    latitude = models.FloatField(max_length=255)
    longitude = models.FloatField(max_length=255)
    airports = models.ManyToManyField(AirPort, null=True)

    updated = models.DateTimeField(auto_now=True, db_index=True)
    created = models.DateTimeField(auto_now_add=True)

    # @property
    def __unicode__(self):
        return self.name


class Weather(models.Model):

    city = models.ForeignKey(City)
    weather_stats = JSONField()

    updated = models.DateTimeField(auto_now=True, db_index=True)
    created = models.DateTimeField(auto_now_add=True)

    # @property
    def __unicode__(self):
        return self.title
