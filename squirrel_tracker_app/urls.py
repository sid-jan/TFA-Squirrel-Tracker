
from django.urls import path
 
from . import views

urlpatterns = [
    path('sightings/', views.all_sightings),
    path('map/', views.get_map, name='map'),
    path('sightings/<Unique_Squirrel_ID>/',views.edit_sighting),
    path('add/',views.add_sighting),
    path('',views.main_page, name= 'main'),
    path('stats/',views.sighting_stats),
]
