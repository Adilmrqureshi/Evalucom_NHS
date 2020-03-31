import requests
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'beds/base.html')

def new_search(request):
    return render(request, 'beds/new_search.html')