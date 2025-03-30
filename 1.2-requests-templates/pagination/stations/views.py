from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    csv_file_path = 'C:/Users/HONOR/Desktop/DJ homeworks/dj-homeworks/1.2-requests-templates/pagination/data-398-2018-08-30.csv'

    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        stations_list = list(reader)

    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(stations_list, 10)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/data.html', context)
