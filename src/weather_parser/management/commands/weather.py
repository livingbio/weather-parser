# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from LatLon import Latitude, Longitude
from weather_parser.models import City, AirPort
import requests
import re
import csv
from cStringIO import StringIO
import time
import json


class Command(BaseCommand):
    help = ''

    # def add_arguments(self, parser):
    #     parser.add_argument('id_or_url', nargs='?', type=str)

    def handle(self, *args, **options):
        city_names = City.objects.values('name')
        city_names = [c['name'] for c in city_names]
        airports = AirPort.objects.filter(content=None)
        for airport in airports:
            print airport.name.encode('utf-8')
            try:
                assert airport.iata.strip() 

                print airport.iata, 'iata'
                airport.content = requests.get("http://www.wunderground.com/history/airport/{}/2015/1/1/CustomHistory.html?dayend=30&monthend=1&yearend=2016&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1".format(airport.iata)).content.replace("<br />", "").strip()
            except:
                try:
                    assert airport.icao.strip()
                    print airport.icao, 'icao'
                    airport.content = requests.get("http://www.wunderground.com/history/airport/{}/2015/1/1/CustomHistory.html?dayend=30&monthend=1&yearend=2016&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1".format(airport.icao)).content.replace("<br />", "").strip()
                except Exception as e:
                    pass
            finally:
                airport.save()


