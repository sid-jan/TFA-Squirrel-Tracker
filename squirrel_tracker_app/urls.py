
from django.urls import path
 
from . import views

urlpatterns = [
    path('sightings/', views.all_sightings),
    path('map/', views.get_map, name='map'),
]
