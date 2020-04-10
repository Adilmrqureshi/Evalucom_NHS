import requests
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpRequest
from django.urls import reverse

from .models import Home, Bed

# Create your views here.
def index(request):
    all_homes = Home.objects.all()
    home_in_question = get_object_or_404(Home, name="The Elms")
    page_number = home_in_question.page_number
    home_list = list()
    for home in all_homes:
        home_id = home.id
        home_name = home.name
        home_beds = home.beds
        home_vacant_beds = home.vacant_beds
        if home.vacant_beds == None or home.vacant_beds == 'null':
            home.vacant_beds = 0
        
        if home_beds.res_beds != None:
            res = home_beds.res_beds
        else: 
            res = None
        if home_beds.res_dem_beds != None:
            res_dem = home_beds.res_dem_beds
        else: 
            res_dem = None
        if home_beds.nus_beds != None:
            nus = home_beds.nus_beds
        else: 
            nus = None
        if home_beds.nus_dem_beds != None:
            nus_dem = home_beds.nus_dem_beds
        else: 
            nus_dem = None
        home_list.append((home_vacant_beds,home_name, home_id,home_beds,res,res_dem,nus,nus_dem, home_id))      
    
    stuff = {
        'home_list': home_list,
        'page_number': page_number
    }
    return render(request, 'beds/stuff.html',stuff)

def voyage(request, offset = 0):
    page_number = offset
    hello = Home.objects.all()
    hello.delete()
    if 'previous' in request.GET:
        print("next")
        page_number = offset-1
    elif 'next' in request.GET:
        print('hello')
        page_number = offset+1
    url = 'https://skills-assessment.herokuapp.com/api/skills_assessment/?limit=10&offset={}0'.format(page_number)
    response = requests.get(url)
    data = response.json()
    results = data['results']
    home_list = list()
    for name in results:
        home_id = int(name['id'].split('-')[1])
        home_name = name['name']
        home_beds = name['beds']
        home_vacant_beds = name['vacant_beds']
        if home_vacant_beds == None or home_vacant_beds == 'null':
            home_vacant_beds = 0
        if 'Residential' in home_beds:
            res_bed = home_beds['Residential']
        else:
            res_bed = None
        if 'Residential dementia' in home_beds:
            res_dem = home_beds['Residential dementia']
        else:
            res_dem = None
        if 'Nursing' in home_beds:
            nus_bed = home_beds['Nursing']
        else:
            nus_bed = None
        if 'Nursing dementia' in home_beds:
            nus_dem = home_beds['Nursing dementia']
        else:
            nus_dem = None
        bed = Bed.objects.create(res_beds = res_bed, res_dem_beds = res_dem,nus_beds = nus_bed, nus_dem_beds = nus_dem )
        home = Home.objects.create(
            name = home_name, vacant_beds = home_vacant_beds, beds = bed, page_number = page_number, id = home_id
        )
        home_list.append((home_vacant_beds,home_name, home_id,home_beds,res_bed,res_dem,nus_bed,nus_dem, home_id))      
        

    stuff = {
        'home_list': home_list,
        'page_number':page_number
    }
    return render(request, 'beds/stuff.html',stuff)

def add_bed(request ,home_id):
    home = get_object_or_404(Home, id=home_id)
    print(home)
    print(home.beds.nus_beds)
    if "remove_res" in request.GET:
        home.beds.res_beds -= 1
        home.vacant_beds += 1
        home.beds.save()
        home.save()
    elif "add_res" in request.GET:
        home.beds.res_beds += 1
        home.vacant_beds -= 1
        home.beds.save()
        home.save()
    elif "remove_res_dem" in request.GET:
        home.beds.res_dem_beds -= 1
        home.vacant_beds += 1
        home.beds.save()
        home.save()
    elif "add_res_dem" in request.GET:
        home.beds.res_dem_beds += 1
        home.vacant_beds -= 1
        home.beds.save()
        home.save()  
    elif "remove_nus" in request.GET:
        home.beds.nus_beds -= 1
        home.vacant_beds += 1
        home.beds.save()
        home.save()
        print(home.beds.nus_beds)
    elif "add_nus" in request.GET:
        home.beds.nus_beds += 1
        home.vacant_beds -= 1
        home.beds.save()
        home.save()  
    elif "remove_nus_dem" in request.GET:
        home.beds.nus_dem_beds -= 1
        home.vacant_beds += 1
        home.beds.save()
        home.save()  
    elif "add_nus_dem" in request.GET:
        home.beds.nus_dem_beds += 1
        home.vacant_beds -= 1
        home.beds.save()
        home.save()  

    return HttpResponseRedirect(reverse('beds:index'))
    