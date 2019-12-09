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
 
def sighting_stats(request):
    am_count = 0
    pm_count = 0
    running_count = 0
    foraging_count = 0
    chasing_count = 0
    climbing_count = 0
    eating_count = 0
    approaches_count = 0
    kuks_count = 0
    quaas_count = 0
    flag_count = 0
    twitch_count = 0
    moans_count = 0
    for  s in  Squirrel.objects.all():
       if s.Shift == 'AM':
           am_count += 1
       if s.Shift == 'PM':
            pm_count += 1
       if s.Running == True:
            running_count += 1
       if s.Foraging == True:
            foraging_count += 1
       if s.approaches == True:
            approaches_count += 1
       if s.moans == True:
            moans_count += 1
       if s.kuks == True:
            kuks_count += 1
       if s.quaas == True:
            quaas_count += 1
       if s.tail_flags == True:
            flag_count += 1
       if s.tail_twitches == True:
            twitch_count += 1
       if s.Chasing == True:
            chasing_count += 1
       if s.Climbing == True:
            climbing_count += 1
       if s.Eating == True:
            eating_count += 1
    context ={
             'AM_count' : am_count,
             'PM_count' : pm_count,
             'Running' : running_count,
             'Foraging' : foraging_count,
             'Approaches' : approaches_count,
             'Chasing' : chasing_count,
             'Climbing' : climbing_count,
             'Eating' : eating_count,
             'Kuks' : kuks_count,
             'Quaas' : quaas_count,
             'Flag' : flag_count,
             'Twitch' : twitch_count,
             'Moans' : moans_count,
        }
    return render(request, 'squirrel_tracker_app/stat.html', context)  

def main_page(request):
    squirrel = 'Squirrel Tracker'
    return render(request, 'squirrel_tracker_app/main.html',{'Squirrel': squirrel})
