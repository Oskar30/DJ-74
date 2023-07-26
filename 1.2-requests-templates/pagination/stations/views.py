from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))

routs = []
with open('data-398-2018-08-30.csv', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
         routs.append({'Name':row['Name'],
                     'Street':row['Street'],
                     'District':row['District']})
         
def bus_stations(request):
    num_page = int(request.GET.get('page', 1))
    paginator = Paginator(routs, 10)
    page = paginator.get_page(num_page)

    context = {
        'bus_stations': page
    }
    return render(request, 'stations/index.html', context)
