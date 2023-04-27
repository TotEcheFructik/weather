from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


def index(req):
    appid = 'e2a0acf58f074fc9679c60d2796fa782'
    url = 'https://api.openweathermap.org/data/2.5/' \
          'weather?q={}&units=metric&appid=' + appid

    if (req.method == 'POST'):
        form = CityForm(req.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:

        res = requests.get(url.format(city.name)).json()

        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon'],
        }

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(req, 'weather/index.html', context)
