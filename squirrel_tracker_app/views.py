from django.shortcuts import render
from django.http import HttpResponse
from .models import Squirrel
from .forms import SquirrelForm,SquirrelFormShort

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

def edit_sighting(request,Unique_Squirrel_ID):
    squirrel = Squirrel.objects.get(Unique_Squirrel_ID = Unique_Squirrel_ID)
    if request.method =='POST':
        form = SquirrelForm(request.POST, instance = squirrel)
        if form.is_valid():
            form.save()
            return redirect (f'squirrel_tracker_app/sightings/{Unique_Squirrel_ID}')
    else:
        form = SquirrelForm(instance=squirrel)
    context = {'form':form}
    return render(request,'squirrel_tracker_app/edit.html',context)

def add_sighting(request):
    if request.method =='POST':
        form = SquirrelFormShort(request.POST)
        if form.is_valid():
            form.save()
            return redirect (f'squirrel_tracker_app/sightings/')
    else:
        form = SquirrelFormShort()
    context = {'form':form}
    return render(request,'squirrel_tracker_app/add.html',context)



# Create your views here.
