# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from weather_parser.models import AirPort
import csv
from cStringIO import StringIO
import requests


class Command(BaseCommand):
    help = ''

    # def add_arguments(self, parser):
    #     parser.add_argument('id_or_url', nargs='?', type=str)

    def handle(self, *args, **options):
        airport_url = 'https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat'
        content = requests.request('GET', airport_url).content.decode('utf-8', 'ignore')
        fields = "airport_id,name,city_name,country_name,iata,icao,latitude,longitude,altitude,timezone,dst".split(',')

        reader = csv.DictReader(StringIO(content.encode('utf-8')), fieldnames=fields)
        for info in reader:
            del info[None]
            AirPort.objects.create(**info)
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
                    airport.content = requests.get("http://www.wunderground.com/history/airport/{}/2015/1/1/CustomHistory.html?dayend=27&monthend=12&yearend=2015&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1".format(airport.icao)).content.replace("<br />", "").strip()
                except:
                    pass
            finally:
                airport.save()
