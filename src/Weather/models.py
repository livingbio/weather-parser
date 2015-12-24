from __future__ import unicode_literals

from django.db import models
from jsonfield import JSONField

# Create your models here.


class City(models.Model):

    name = models.TextField(max_length=255)
    population = models.IntegerField(db_index=True)
    altitude = models.IntegerField(null=True, db_index=True)
    country = models.TextField(max_length=255)
    latitude = models.FloatField(max_length=255)
    longitude = models.FloatField(max_length=255)
    airport_code = models.TextField(null=True, max_length=255)

    updated = models.DateTimeField(auto_now=True, db_index=True)
    created = models.DateTimeField(auto_now_add=True)

    # @property
    def __unicode__(self):
        return self.title


class Weather(models.Model):

    city = models.ForeignKey(City)
    weather_stats = JSONField()

    updated = models.DateTimeField(auto_now=True, db_index=True)
    created = models.DateTimeField(auto_now_add=True)

    # @property
    def __unicode__(self):
        return self.title
