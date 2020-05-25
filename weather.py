from pyowm import OWM
from configparser import ConfigParser
import json

class city_weather():
    def __init__(self):
        self.config = ConfigParser()
        self.config.read('config.ini')
        self.weather_key = self.config.get('DEFAULT', 'OPEN_WEATHER_API_KEY')
        self.owm = OWM(self.weather_key)

    def weather_in(self, city):
        observation = self.owm.weather_at_place(city)
        w = observation.get_weather()
        temp_json = w.get_temperature(unit='celsius')
        temp = temp_json.get('temp')

        if temp < 15.0:
            status = ' and it is very cold out there'
        elif (temp > 15.0 and temp < 20.0):
            status = ' and it is cold out there'
        elif temp > 20.0 and temp < 23.0:
            status = ' and it is nice weather out there'
        else:
            status = ''

        respond = 'Temperature in ' + city + ' is ' + str(temp) + ' degree celsius' + status

        return {
            "fulfillmentText": respond
        }