#import library
from django.shortcuts import render
import json
import urllib.request

# Create your views here.
""" index function recieve the city from the html test box
    request the url(openweathermap) to get the data of particular city in json format .
    display the data in html file.
"""
def index(request):
    if request.method =="POST":
        city=request.POST['city']
        source=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +city + '&units=metric&appid=<Your API Key>').read()
        list_of_data=json.loads(source)
        data={
            "country_code":str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '+ str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],

        }
        print(data)
    else:
        data={}
    return render(request,"index.html",data)

def about(request):
    return render(request,'about.html')