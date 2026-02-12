from django.shortcuts import render
import datetime
import requests

def home(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else: 
        city = 'lagos'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=bf7d64842ff40f509e79d234058c593e'

    PARAMS = {'units': 'metric'}

    data = requests.get(url, PARAMS).json()

    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temp = data['main']['temp']

    day = datetime.date.today()

    return render(request, 'weatherapp/home.html',{'description': description, 'icon': icon, 'temp': temp, 'day': day, 'city': city})
