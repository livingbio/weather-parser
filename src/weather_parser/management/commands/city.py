# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from LatLon import Latitude, Longitude
from weather_parser.models import City
import requests
import re


class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
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
            city = City.objects.create(**city)
            city.save()
