# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from weather_parser.models import AirPort
from datetime import datetime


class Command(BaseCommand):
    help = ''

    def add_arguments(self, parser):
        parser.add_argument('city_name', nargs='?', type=str)
        parser.add_argument('start_date', nargs='?', type=str)
        parser.add_argument('end_date', nargs='?', type=str)

    def handle(self, *args, **options):
        name = options['city_name']
        airports = AirPort.objects.filter(city_name=name)
        start_date = datetime.strptime(options['start_date'], '%Y/%m/%d')
        start_date = datetime.date(start_date)
        end_date = datetime.strptime(options['end_date'], '%Y/%m/%d')
        end_date = datetime.date(end_date)
        for airport in airports:
            if start_date == end_date:
                result = airport.get_date_weather(start_date)
            else:
                result = airport.get_weather(start_date, end_date)
            if len(result) == 0:
                continue
            else:
                break
        print result
