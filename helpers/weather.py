'''
    Gets Weather Data from National Weather Service
    API reference : https://www.weather.gov/documentation/services-web-api
    Forecasts are divided into 2.5km grids. Each NWS office is responsible for a section of the grid.
'''

import requests as request
from dotenv import load_dotenv
import os
import json

s = request.session()
s

load_dotenv()

headers = {
    "User-Agent"    : "Camarillo, CA Weather Info",
    "From"          : "camarillionaire@gmail.com",
    "Cache-Control" : "no-cache",
    "Pragma"        : "no-cache"
}

'''
    Gets Grid information based on Lat, Lon
'''
def get_grid_location() :

    # print(f"{os.getenv('WEATHER_END_POINT')}{os.getenv('WEATHER_CAM_LAT')},{os.getenv('WEATHER_CAM_LON')}")

    response = s.get(
        f"{os.getenv('WEATHER_END_POINT')}{os.getenv('WEATHER_CAM_LAT')},{os.getenv('WEATHER_CAM_LON')}",
        headers = headers
    )

    response.raise_for_status()

    # print(response.json())
    return response

'''
    Gets current forecast
'''
def get_forecast() :

    forecast_url = get_grid_location().json()["properties"]["forecast"]

    print(forecast_url)

    response = s.get(
        forecast_url,
        headers = headers
    )

    response.raise_for_status()
    return response.json();

'''
    Gets formated forecast for publishing
'''
def get_formated_forecast() :

    forecast_json     = get_forecast()
    name              = forecast_json['properties']['periods'][0]['name']
    detailed_forecast = forecast_json['properties']['periods'][0]['detailedForecast']
    # short_forecast    = forecast_json['properties']['periods'][0]['shortForecast']
    temperature       = forecast_json['properties']['periods'][0]['temperature']
    temperature_unit  = forecast_json['properties']['periods'][0]['temperatureUnit']

    return f"{name}: {temperature}º{temperature_unit} {detailed_forecast} #{os.getenv('BOT_NAME')} #{os.getenv('BOT_LOCATION')}"