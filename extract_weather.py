
from dotenv import load_dotenv
load_dotenv()

import os
token=os.environ.get("api-token")

import requests
import json

def get_current_weather(id):
    """ Returns current weather data by city id (New York by default)
    """
    load_dotenv()
    json_data = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?id="+id+"&appid="+os.environ.get("api-token")).json()

    print("Getting current weather data from OpenWeatherMap.org..........")
    return json_data

  #  {'coord': {'lon': -74.006, 'lat': 40.7143}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 'main': {'temp': 295.71, 'feels_like': 295.01, 'temp_min': 293.56, 'temp_max': 297.17, 'pressure': 1012, 'humidity': 38}, 'visibility': 10000, 'wind': {'speed': 8.49, 'deg': 283, 'gust': 13.41}, 'clouds': {'all': 1}, 'dt': 1632687255, 'sys': {'type': 2, 'id': 2008776, 'country': 'US', 'sunrise': 1632653260, 'sunset': 1632696408}, 'timezone': -14400, 'id': 5128581, 'name': 'New York', 'cod': 200}


def write_weather_data(json_data):
    """ Save current weather data to a json file.
        Name the file by the Unix Timestamp.
    """
    name = 'data' + str(json_data['dt']) #  Each json file is named after the "dt" value which stands for datetime.
    #'data1632687255'
    filename = r"data_cache/%s.json" % name
   # data_cache/data1632687255.json
    with open(filename, 'w') as f:
        json.dump(json_data, f)
    return filename
