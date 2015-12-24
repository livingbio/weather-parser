# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from LatLon import Latitude, Longitude
from Weather.models import City
import requests
import re


class Command(BaseCommand):
    help = ''

    # def add_arguments(self, parser):
    #     parser.add_argument('id_or_url', nargs='?', type=str)

    def handle(self, *args, **options):
        url2 = 'http://www.airportcodes.org/'
        html2 = requests.request('GET', url2).content.decode('utf-8', 'ignore')
        body2 = BeautifulSoup(html2, "html.parser")

        airport_code_list_from_web = body2.select('.t6')[0].parent.parent.text
        # airport_code_list_from_web = airport_code_list_from_web.text.split(
        #     'International code list')[-1]
        airport_code_list_from_web = airport_code_list_from_web.split('\n')
        airport_code_list = {}
        for x in airport_code_list_from_web:
            if ',' in x:
                y = x.split(',')
                y[0] = y[0].split(' (')[0]
                try:
                    airport_code_list[y[0]].append(re.search(ur'\(?(\w+)\)', y[-1]).group(1))
                except:
                    print y
                    try:
                        airport_code_list[y[0]] = [re.search(ur'\(?(\w+)\)', y[-1]).group(1)]
                    except:
                        pass
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
                    try:
                        airport_code = airport_code_list[name]
                    except:
                        # import pdb; pdb.set_trace()
                        airport_code = None
                    city_list.append({
                        'name': name,
                        'population': population,
                        'altitude': altitude,
                        'country': country,
                        'latitude': latitude,
                        'longitude': longitude,
                        'airport_code': airport_code
                        })
                except:
                    pass
        print len(city_list)
        print city_list[734]
        print city_list[142]
        print len(airport_code_list)
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
