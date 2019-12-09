from django.forms import ModelForm

from .models import Squirrel


class SquirrelForm(ModelForm):
    class Meta:
        model = Squirrel
        fields = '__all__'

class SquirrelFormShort(ModelForm):
    class Meta:
        model = Squirrel
        fields = ('Latitude',
'Longitude',
'Unique_Squirrel_ID',
'Shift',
'Date',
'Age',
'Primary_fur_color',
'Location',
'Specific_location',
'Running',
'Chasing',
'Climbing',
'Eating',
'Foraging',
'Other_activities',
'kuks',
'quaas',
'moans',
'tail_flags',
'tail_twitches',
'approaches',
'indifferent',
'runs_from',)
