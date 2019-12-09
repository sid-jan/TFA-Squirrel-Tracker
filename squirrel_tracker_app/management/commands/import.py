from django.core.management.base import BaseCommand
from squirrel_tracker_app.models import Squirrel
import csv

class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('csv_file')
    def handle(self,*args,**options):
        with open(options['csv_file']) as fp:
            Reader = csv.DictReader(fp)
            Data = list(Reader)
            for item in Data:
                form_date= item['Date'][4:] + "-" + item['Date'][:2] + "-" + item['Date'][2:4]
                s=Squirrel(
                Latitude=item['X'],
                Longitude=item['Y'],
                Unique_Squirrel_ID=item['Unique Squirrel ID'],
                Hectare=item['Hectare'],
                Shift=item['Shift'],
                Date=form_date,
                Hectare_Squirrel_Number=item['Hectare Squirrel Number'],
                Age=item['Age'],
                Primary_fur_color=item['Primary Fur Color'],
                Highlight_fur_color=item['Highlight Fur Color'],
                Combination_of_primary_and_highlight_color=item['Combination of Primary and Highlight Color'],
                Location=item['Color notes'],
                Above_ground_sighter_measurement=item['Above Ground Sighter Measurement'],
                Specific_location=item['Specific Location'],
                Running=item['Running'].lower().capitalize(),
                Chasing=item['Chasing'].lower().capitalize(),
                Climbing=item['Climbing'].lower().capitalize(),
                Eating=item['Eating'].lower().capitalize(),
                Foraging=item['Foraging'].lower().capitalize(),
                Other_activities=item['Other Activities'],
                kuks=item['Kuks'].lower().capitalize(),
                quaas = item['Quaas'].lower().capitalize(),
                moans  = item['Moans'].lower().capitalize(),
                tail_flags = item['Tail flags'].lower().capitalize(),
                tail_twitches = item['Tail twitches'].lower().capitalize(),
                approaches = item['Approaches'].lower().capitalize(),
                indifferent = item['Indifferent'].lower().capitalize(),
                runs_from = item['Runs from'].lower().capitalize(),
                other_interactions = item['Other Interactions'],
                lat_Long = item['Lat/Long'],
                zip_code = item['Zip Codes'],
                community_district = item['Community Districts'],
                borough_boundaries = item['Borough Boundaries'],
                city_council_districts = item['City Council Districts'],
                police_precincts = item['Police Precincts']
                )
                s.save()

