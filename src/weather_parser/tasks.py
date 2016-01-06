# -*- encoding=utf8 -*-
from .parser import Parser
from huey.djhuey import crontab, db_periodic_task, db_task  # , periodic_task
from weather_parser.models import City, AirPort
from bs4 import BeautifulSoup
from LatLon import Latitude, Longitude
from cStringIO import StringIO
import re
import csv
import requests


s = Parser()


def _iter(qs, chunk_size=500):
    from django.core.paginator import Paginator

    paginator = Paginator(qs, chunk_size)
    print 'iter', qs, paginator.count, paginator.num_pages

    for page in xrange(1, paginator.num_pages + 1):
        print 'page', page
        for row in paginator.page(page).object_list:
            yield row


@db_periodic_task(crontab(hour='24'))
def scan_airport():
    airport_url = 'https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat'
    content = requests.request('GET', airport_url).content.decode('utf-8', 'ignore')
    fields = "airport_id,name,city_name,country_name,iata,icao,latitude,longitude,altitude,timezone,dst".split(',')

    reader = csv.DictReader(StringIO(content.encode('utf-8')), fieldnames=fields)
    for info in reader:
        del info[None]
        AirPort.objects.get_or_create(**info)


@db_periodic_task(crontab(hour='24'))
def update_city():
    city_list = []
    for x in xrange(0, 10):
        url = 'http://www.tiptopglobe.com/biggest-cities-world?p=' + str(x)
        html = requests.request('GET', url).content.replace('\xb0', 'O')
        html = html.decode('utf-8', 'ignore').replace(u'</h2>', '')
        body = BeautifulSoup(html, "html.parser")
        city_list_from_web = body.select('tr')

        for city in city_list_from_web[1:]:
            try:
                name = city.select('td')[1].select('font')[0].text
                name = re.sub("\s*\(.*\)", "", name).strip()
                population = int(city.select('td')[2].text.replace(' ', ''))
                try:
                    altitude = int(city.select('td')[3].text.split(' ')[0])
                except:
                    altitude = None
                country = city.select('td')[4].select('font')[0].text
                latitude = city.select('td')[5].text
                latitude = re.search(r'(\d+)O(\d+)\'([\d\.]+)"', latitude).groups()
                latitude = float(Latitude(
                    degree=int(latitude[0]),
                    minute=int(latitude[1]),
                    second=float(latitude[2])))
                longitude = city.select('td')[6].text
                longitude = re.search(r'(\d+)O(\d+)\'([\d\.]+)"', longitude).groups()
                longitude = float(Longitude(
                    degree=int(longitude[0]),
                    minute=int(longitude[1]),
                    second=float(longitude[2])))
                city_list.append({
                    'name': name,
                    'population': population,
                    'altitude': altitude,
                    'country': country,
                    'latitude': latitude,
                    'longitude': longitude,
                    })
            except:
                pass
    for city in city_list:
        city = City.objects.get_or_create(**city)
        city.save()