from django.core.management.base import BaseCommand

import csv
  
from squirrel_tracker_app.models import Squirrel

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')
    def handle(self, *args, **options):
        dict_ = {}
        s = Squirrel.objects.all()
        with open(options['csv_file'],"w") as fp:
            for item in s:
                dict_['X'] = item.Latitude
                dict_['Y'] = item.Longitude
                dict_['Shift'] = item.Shift
                dict_['Date'] = item.Date
                dict_['Unique Squirrel ID'] = item.Unique_Squirrel_ID
                dict_['Age'] = item.Age
                dict_['Primary Fur Color'] = item.Primary_fur_color
                dict_['Location'] = item.Location
                dict_['Specific Location'] = item.Specific_location
                dict_['Running'] = item.Running
                dict_['Chasing'] = item.Chasing
                dict_['Climbing'] = item.Climbing
                dict_['Eating'] = item.Eating
                dict_['Foraging'] = item.Foraging
                dict_['Other Activities'] = item.Other_activities
                dict_['Kuks'] = item.kuks
                dict_['Quaas'] = item.quaas
                dict_['Moans'] = item.moans
                dict_['Tail Flags'] = item.tail_flags
                dict_['Tail Twitches'] = item.tail_twitches
                dict_['Approaches'] = item.approaches
                dict_['Indifferent'] = item.indifferent
                dict_['Runs from'] = item.runs_from
                writer = csv.DictWriter(fp,delimiter=",",fieldnames=dict_.keys())
                writer.writeheader()
                writer.writerow(dict_)
