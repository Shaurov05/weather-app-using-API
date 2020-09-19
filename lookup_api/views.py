from django.shortcuts import render
from django.views.generic import (TemplateView,ListView,View,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

import json
import requests
# Create your views here.

# http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=FB06F6F7-42D5-430D-9836-BF36EE03CFCF

def index(request):

    if request.method == "POST":
        zipcode = request.POST["zipcode"]
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=15&API_KEY=FB06F6F7-42D5-430D-9836-BF36EE03CFCF")
    else:
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=FB06F6F7-42D5-430D-9836-BF36EE03CFCF")


    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = 'Error....'

    if not api:
        return render(request, 'index.html', {'api':api})

    if api[0]['Category']['Name'] == "Good":
        category_description = "(0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk."
        category_color = api[0]['Category']['Name']

    elif api[0]['Category']['Name'] == "Moderate":
        category_description = "(51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution. "
        category_color = api[0]['Category']['Name']

    elif api[0]['Category']['Name'] == "USG" :
        category_description = "Unhealthy for Sensitive Groups (101 - 150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."
        category_color = api[0]['Category']['Name']

    elif api[0]['Category']['Name'] == "Unhealthy":
        category_description = "Unhealthy (151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
        category_color = api[0]['Category']['Name']

    elif api[0]['Category']['Name'] == "Very Unhealthy" :
        category_description = "Very Unhealthy (201 - 300) Health alert: everyone may experience more serious health effects."
        category_color = "Very-Unhealthy"

    elif api[0]['Category']['Name'] == "Hazardous" :
        category_description = "Hazardous (301 - 500) Health warnings of emergency conditions. The entire population is more likely to be affected."
        category_color = api[0]['Category']['Name']

    return render(request, 'index.html', {'api':api,
            'category_description':category_description,
            'category_color':category_color,
        })



def about(request):
    return render(request, 'about.html', {})
