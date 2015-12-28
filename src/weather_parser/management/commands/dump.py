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
        fields = """WGT,
                    Max TemperatureC,
                    Mean TemperatureC,
                    Min TemperatureC,
                    Dew PointC,
                    MeanDew PointC,
                    Min DewpointC,
                    Max Humidity,
                     Mean Humidity,
                     Min Humidity,
                     Max Sea Level PressurehPa,
                     Mean Sea Level PressurehPa,
                     Min Sea Level PressurehPa,
                     Max VisibilityKm,
                     Mean VisibilityKm,
                     Min VisibilitykM,
                     Max Wind SpeedKm/h,
                     Mean Wind SpeedKm/h,
                     Max Gust SpeedKm/h,
                    Precipitationmm,
                     CloudCover,
                     Events,
                    WindDirDegrees"""
        airports = AirPort.objects.exclude(content=None)
        with open('weather_data', 'w+') as f:
            for airport in airports:
                print airport.name.encode('utf-8')
                reader = csv.DictReader(StringIO(airport.content))

                time_field = re.match("^\w+", airport.content).group()
                data = airport.__dict__
                del data['_state']
                del data['content']
                del data['dst']
                
                for daily_info in reader:
                    data['time'] = daily_info[time_field]
                    data['max_temp'] = daily_info['Max TemperatureC']
                    data['mean_temp'] = daily_info['Mean TemperatureC']
                    data['min_temp'] = daily_info['Min TemperatureC']
                    data['dew'] = daily_info['Dew PointC']
                    data['mean_dew'] = daily_info['MeanDew PointC']
                    data['min_dew'] = daily_info['Min DewpointC']
                    data['max_humidity'] = daily_info['Max Humidity']
                    data['min_humidity'] = daily_info[' Min Humidity']
                    data['mean_humidity'] = daily_info[' Mean Humidity']
                    data['max_sea_hpa'] = daily_info[' Max Sea Level PressurehPa']
                    data['min_sea_hpa'] = daily_info[' Min Sea Level PressurehPa']
                    data['mean_sea_hpa'] = daily_info[' Mean Sea Level PressurehPa']
                    data['max_visiable'] = daily_info[' Max VisibilityKm']
                    data['min_visiable'] = daily_info[' Min VisibilitykM']
                    data['max_wind_speed'] = daily_info[' Max Wind SpeedKm/h']
                    data['min_wind_speed'] = daily_info[' Max Wind SpeedKm/h']
                    data['max_ghost_wind_speed'] = daily_info[' Max Gust SpeedKm/h']
                    data['precipitation'] = daily_info['Precipitationmm']
                    data['cloudiness'] = daily_info[' CloudCover']
                    data['events'] = daily_info[' Events']

                    f.write(json.dumps(data) + "\n")

