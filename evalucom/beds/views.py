import requests
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpRequest
from django.urls import reverse

from .models import Home

# Create your views here.
def index(request):
    page_number = 0
    response = requests.get('https://skills-assessment.herokuapp.com/api/skills_assessment/?limit=10{}')
    data = response.json()
    results = data['results']
    home_list = list()
    for name in results:
        home_id = name['id']
        home_name = name['name']
        home_beds = name['beds']
        home_vacant_beds = name['vacant_beds']
        if 'Residential' in home_beds:
            res_bed = home_beds['Residential']
        else:
            res_bed = 0
        if 'Residential dementia' in home_beds:
            res_dem = home_beds['Residential dementia']
        else:
            res_dem = 0
        if 'Nursing' in home_beds:
            nus_bed = home_beds['Nursing']
        else:
            nus_bed = 0
        if 'Nursing dementia' in home_beds:
            nus_dem = home_beds['Nursing dementia']
        else:
            nus_dem = 0
        home_list.append((home_vacant_beds,home_name, home_id,home_beds,res_bed,res_dem,nus_bed,nus_dem))        

    stuff = {
        'home_list': home_list,
        'page_number': page_number
    }
    return render(request, 'beds/stuff.html',stuff)

def voyage(request, offset):
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
        home_id = name['id']
        home_name = name['name']
        home_beds = name['beds']
        home_vacant_beds = name['vacant_beds']
        if 'Residential' in home_beds:
            res_bed = home_beds['Residential']
        else:
            res_bed = 0
        if 'Residential dementia' in home_beds:
            res_dem = home_beds['Residential dementia']
        else:
            res_dem = 0
        if 'Nursing' in home_beds:
            nus_bed = home_beds['Nursing']
        else:
            nus_bed = 0
        if 'Nursing dementia' in home_beds:
            nus_dem = home_beds['Nursing dementia']
        else:
            nus_dem = 0
        home_list.append((home_vacant_beds,home_name, home_id,home_beds,res_bed,res_dem,nus_bed,nus_dem))        

    stuff = {
        'home_list': home_list,
        'page_number':page_number
    }
    return render(request, 'beds/stuff.html',stuff)

def add_bed(request, home_id):
    pass