from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    city = request.GET.get('city' , 'lucknow')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=fb1559b93f2f1d556c9ec0d2c0725a55'
    data = requests.get(url).json()
    payload = {
        'city':data['name'],
        'weather':data['weather'][0]['main'],
        'icon':data['weather'][0]['icon'],
        'kelvin_temperature':data['main']['temp'],
        'celcius_temperature':data['main']['temp']-273,
        'pressure':data['main']['pressure'],
        'humidity' :data['main']['humidity'],
        'description': data['weather'][0]['main']

        
        
    } 

    context = {'data' : payload}
    print(context)
    return render(request,'home.html',context)
