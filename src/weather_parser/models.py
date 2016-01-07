from __future__ import unicode_literals

from django.db import models
from jsonfield import JSONField
from datetime import datetime
from datetime import timedelta
import requests
import re
import csv
from cStringIO import StringIO

# Create your models here.


class AirPort(models.Model):

    airport_id = models.CharField(max_length=1024, blank=True)
    city_name = models.CharField(max_length=1024, blank=True)
    country_name = models.CharField(max_length=1024, blank=True)
    latitude = models.FloatField(blank=True)
    longitude = models.FloatField(blank=True)
    timezone = models.FloatField(blank=True)
    dst = models.CharField(max_length=1024, blank=True)
    name = models.CharField(max_length=1024, blank=True)
    altitude = models.FloatField(blank=True)
    iata = models.CharField(max_length=1024, blank=True)
    icao = models.CharField(max_length=1024, blank=True)
    content = models.TextField(blank=True)

    def get_weather(self, st, ed):
        """
        Args:
            st: datetime.Date object ## start date
            ed: datetime.Date object ## start date
        """
        if st.strftime("%Y") > ed.strftime("%Y"):
            st, ed = ed, st
        result = ""
        while st.strftime("%Y") <= ed.strftime("%Y"):
            start = st.strftime("%Y/%m/%d")
            url = "http://www.wunderground.com/history/airport/{0}/{1}/CustomHistory.html?".format({}, start)
            if st.strftime("%Y") == ed.strftime("%Y"):
                url += "dayend={0}&monthend={1}&yearend={2}".format(ed.strftime("%d"), ed.strftime("%m"), ed.strftime("%Y"))
            else:
                url += "dayend={0}&monthend={1}&yearend={2}".format("31", "12", st.strftime("%Y"))
            url += "&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1"
            # import pdb; pdb.set_trace()
            try:
                url_try = url.format(self.iata)
                data = requests.get(url_try).content.replace("<br />", "").strip()
            except:
                try:
                    url_try = url.format(self.icao)
                    data = requests.get(url_try).content.replace("<br />", "").strip()
                except:
                    data = ''
            if len(data.split('\n')[1:]) != 0:
                result_head = data.split('\n')[0]
                result += data.replace(result_head,"")
            start = str(int(st.strftime("%Y")) + 1) + "/1/1"
            st = datetime.strptime(start, '%Y/%m/%d')
        result = result_head + result
        return result

    def get_date_weather(self, date):
        datedelta = timedelta(days=1)
        date2 = date + datedelta
        result = self.get_weather(date, date2)
        result = "".join(result.split('\n')[:-1])
        return result


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
