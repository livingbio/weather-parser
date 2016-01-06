from __future__ import unicode_literals

from django.db import models
from jsonfield import JSONField
from datetime import timedelta
import requests
import csv
from cStringIO import StringIO

# Create your models here.


class AirPort(models.Model):

    airport_id = models.CharField(max_length=1024, null=True)
    city_name = models.CharField(max_length=1024, null=True)
    country_name = models.CharField(max_length=1024, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    timezone = models.FloatField(null=True)
    dst = models.CharField(max_length=1024, null=True)
    name = models.CharField(max_length=1024, null=True)
    altitude = models.FloatField(null=True)
    iata = models.CharField(max_length=1024, null=True)
    icao = models.CharField(max_length=1024, null=True)
    content = models.TextField(null=True)

    def get_weather(self, st, ed):
        """
        Args:
            st: datetime.Date object ## start date
            ed: datetime.Date object ## start date
        """
        start = st.strftime("%Y/%m/%d")
        url = "http://www.wunderground.com/history/airport/{}/{}/CustomHistory.html?".format({}, start)
        url += "dayend={}&monthend={}&yearend={}".format(ed.strftime("%d"), ed.strftime("%m"), ed.strftime("%Y"))
        url += "&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1"
        try:
            url.format(self.iata)
            result = requests.get(url).content.replace("<br />", "").strip()
        except:
            try:
                url.format(self.icao)
                result = requests.get(url).content.replace("<br />", "").strip()
            except:
                pass
        return result

    def get_date_weather(self, date):
        datedelta = timedelta(days=1)
        date2 = date + datedelta
        result = self.get_weather(date, date2)
        read = csv.DictReader(StringIO(result))
        return read[0]


class City(models.Model):

    name = models.TextField(max_length=255)
    population = models.IntegerField(db_index=True)
    altitude = models.IntegerField(null=True, db_index=True)
    country = models.TextField(max_length=255)
    latitude = models.FloatField(max_length=255)
    longitude = models.FloatField(max_length=255)

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
