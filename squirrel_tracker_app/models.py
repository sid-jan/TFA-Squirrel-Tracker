from django.db import models

from django.utils.translation import gettext as _
# Create your models here.
class Squirrel(models.Model):
    
    AM = 'AM'
    PM = 'PM'

    ADULT = 'ADULT'
    JUVENILE = 'JUVENILE'

    Gray = 'GRAY'
    Cinnamon = 'CINAMMON'
    Black = 'BLACK'
    
    GROUND_PLANE = 'GROUND PLANE'
    ABOVE_GROUND = 'ABOVE GROUND'


    age_options = (
            (ADULT, 'ADULT'),
            (JUVENILE, 'JUVENILE'),
        )

    shift_options = (
            (AM, 'AM'),
            (PM, 'PM'),
        )


    color_options = (
            (Gray, 'GRAY'),
            (Cinnamon, 'CINNAMON'),
            (Black, 'BLACK'),
        )
    

    location_options = (
            (GROUND_PLANE, 'GROUND PlANE'),
            (ABOVE_GROUND, 'ABOVE GROUND'),
        )
    
    Latitude = models.DecimalField(
            null=False,
            help_text='Latitude coordinate of sighting',
            max_digits = 20,
            decimal_places = 15
            )
    
    Longitude = models.DecimalField(
            null=False,
            help_text='Longitude coordinate of sighting',
            max_digits = 20,
            decimal_places = 15
            )
    
    Unique_Squirrel_ID = models.CharField(
            null=False,
            help_text = 'Unique ID of squirrel sighting',
            max_length=14)
    
    Hectare = models.CharField(
            null = False,
            max_length=3)
  
    Shift = models.CharField(
            max_length=2,
            null = False,
            help_text = 'Morning/Evening sighting',
            choices=shift_options)
    
    Date = models.DateField(
            null=False,
            help_text = 'Date of sighting')
    
    Hectare_Squirrel_Number = models.IntegerField(
            null=False)
    
    Age = models.CharField(
            max_length=10,
            blank=True,
            null = True,
            choices = age_options,
            help_text='Age of squirrel sighted'
            )
    
    Primary_fur_color = models.CharField(
            max_length = 20,
            help_text = 'Color of the squirrel',
            choices = color_options,
            blank=True
            )
    
    Highlight_fur_color = models.CharField(
            max_length = 50,
            help_text= 'Highlight color of the fur of the squirrel',
            blank=True
            )
    Combination_of_primary_and_highlight_color = models.CharField(max_length=70, blank=True)
    
    Color_notes = models.CharField(max_length = 100,
            blank=True)
    
    Location = models.CharField(max_length = 20,
            blank=True,
            choices = location_options)
    
    Above_ground_sighter_measurement = models.CharField(
            max_length = 10,
            blank= True)
    
    Specific_location = models.CharField(
            help_text=_('Location of sighting'),
            max_length = 40,
            blank=True)
    
    Running = models.BooleanField(
            help_text=_('True if squirrel seen running'),
            default=False,
        )

    Chasing = models.BooleanField(
            help_text=_('True if squirrel was seen chasing'),
            default=False,
         )
    Climbing = models.BooleanField(
            help_text=_('True if Squirrel was seen climbing'),
            default=False,
        )
    Eating = models.BooleanField(
            help_text=_('True if Squirrel is eating'),
            default=False,
        )
     
    Foraging = models.BooleanField(
            help_text=_('True if Squirrel is foraging'),
            default=False,
        )
     
    Other_activities = models.CharField(
            help_text=_('Activity the Squirrel is performing'),
            blank=True,
            max_length = 100,
        )
            
    kuks = models.BooleanField(
            help_text=_('True if the Squirrel is kuking - a chirpy voice communication'),
            default=False,
        )
    

    quaas = models.BooleanField(
            help_text=_('True if the Squirrel is Quaaing - an elongated vocal call'),
            default=False,
        )
     
    moans = models.BooleanField(
            help_text=_('True if the Squirrel is Moaning - a high pitched vocal communication'),
            default=False,
        )
            
    tail_flags = models.BooleanField(
            help_text=_('True if the Squirrel is flagging its tail'),
            default=False,
        )
            
    tail_twitches = models.BooleanField(
            help_text=_('True if the Squirrel is twitching its tail'),
            default=False,
        )
            
    approaches = models.BooleanField(
            help_text=_('True if the Squirrel is seen approaching humans'),
            default=False,
        )
            
    indifferent = models.BooleanField(
            help_text=_('True if squirrel was indifferent to humans'),
            default=False,
        )

    runs_from = models.BooleanField(
            help_text=_('True if Squirrel was seen running from humans'),
            default=False,
        )

    other_interactions = models.CharField(
            null=True,
            blank = True,
            max_length=100
                )

    lat_Long = models.CharField(
            max_length=100,
            null=False
            )
    

    zip_code = models.CharField(
            max_length=6,
            null=True
                )

    community_district = models.IntegerField(
            null=False
                )

    borough_boundaries = models.IntegerField(
            null=False
                )

    city_council_districts = models.IntegerField(
            null=False
                )

    police_precincts = models.IntegerField(
             null=False
                )
    
    def __str__(self):
        return self.Unique_Squirrel_ID


