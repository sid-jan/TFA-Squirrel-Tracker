from django.shortcuts import render
from django.http import HttpResponse
from .models import Squirrel

def all_sightings(request):
    squirrel = Squirrel.objects.all()
    context = {
            'squirrel':squirrel,
            }
    return render(request,'squirrel_tracker_app/all.html',context)

def get_map(request):
    sight = Squirrel.objects.all()[:100]
    context ={
            'sightings' :sight,
        }
    return render(request, 'squirrel_tracker_app/map.html',context)

# Create your views here.
