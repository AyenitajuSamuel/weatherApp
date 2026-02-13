from django.shortcuts import render
from django.contrib import messages
import datetime
import requests

def home(request):

    city = request.POST.get('city', 'lagos')

    url = f'https://api.openweathermap.org/data/2.5/weather'

    params = {
        'q': city,
        'appid': 'bf7d64842ff40f509e79d234058c593e',
        'units': 'metric'
    }

    data = requests.get(url, params=params).json()

    if data.get("cod") != 200:
        messages.error(request, "City not found. Showing Lagos instead.")

        city = "lagos"
        params['q'] = city
        response = requests.get(url, params=params)
        data = response.json()

    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temp = data['main']['temp']
    feel_temp = data['main']['feels_like']
    humidity = data['main']['humidity']
    windspeed = data['wind']['speed']
    pressure = data['main']['pressure']
    day = datetime.date.today()

    context = {'description': description,
            'icon': icon,
            'temp': temp,
            'feel_temp': feel_temp, 
            'day': day, 
            'city': city, 
            'humidity': humidity, 
            'windspeed': windspeed,
            'pressure': pressure,
            }

    return render(request, 'weatherapp/home.html', context)