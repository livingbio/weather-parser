# -*- coding: utf-8 -*-
from weather_parser.models import AirPort
import re
import csv
from cStringIO import StringIO
import json


def dump_weather(weather_data):
    airports = AirPort.objects.exclude(content=None)
    with open('weather_data', 'w+') as f:
        for airport in airports:
            print airport.name.encode('utf-8')
            reader = csv.DictReader(StringIO(airport.content))
            try:
                time_field = re.match("^\w+", airport.content).group()
            except:
                continue
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
