# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from LatLon import Latitude, Longitude
from weather_parser.models import City, AirPort
import requests
import re
import csv
from cStringIO import StringIO


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

                    # import pdb; pdb.set_trace()
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
        print len(city_list)
        print city_list[734]
        print city_list[142]
        for city in city_list:
            city = City.objects.create(**city)
            city_airports = AirPort.objects.filter(city_name=city.name)
            city.airports = city_airports
            city.save()


        # pp.pprint(len(result_list))
        # for result in result_list:

        #     city, is_create = City.objects.get_or_create(
        #         name=result['name'],
        #         default=result
        #     )

        #     for k in result:
        #         if k == 'comment_list':
        #             continue
        #         if not result[k] is None:
        #             setattr(review, k, result[k])
        #     for cmt in result['comment_list']:
        #         try:
        #             Comment.objects.create(
        #                 review=review,
        #                 commentator=cmt['commentator'],
        #                 like=cmt['like'],
        #                 content=cmt['content'],
        #                 comment_time=cmt['comment_time']
        #             )

        #             #         pass
        #         except Exception as e:
        #             print e, review.id
        #             pass
        #     review.status = "DONE"
        #     review.save()
