from django.shortcuts import render
import requests
import datetime

# Create your views here.

def index(request):

    # city = request.POST['city']
    # print(request.POST['city'])
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        print('not working')
        city = 'london'

    appid = 'a2872272194807dbb7838b7044e642f8'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': city, 'appid': appid, 'units': 'metric'}
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()
    # print(res)
    desc = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    day = datetime.date.today()

    print(desc)
    print(day)
    print(temp)
    print(icon)


    return render(request, 'weatherapp/index.html', {'desc': desc, 'icon': icon, 'temp': temp, 'day': day, 'city': city})
    