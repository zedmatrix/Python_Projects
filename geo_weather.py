#!/usr/bin/env python3
import requests
import json
import argparse

degree = u'\N{DEGREE SIGN}'
api_key = ## Goto https://openweathermap.org Sign up for free account and get API Key
limit = 5
class City:
    def __init__(self, lat, lon, units="imperial"):
        #self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.url = f"https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&units={self.units}&appid={api_key}"
        self.get_data()

    def get_data(self):
        try:
            response = requests.get(self.url)
        except Exception as e:
            print(f"Error {e}")

        response_json = response.json()
        print(f"\n -- {response_json} --\n")
        self.name = response_json["name"]
        self.main = response_json["main"]
        self.temp = self.main["temp"]
        self.feels = self.main["feels_like"]
        self.temp_min = self.main["temp_min"]
        self.temp_max = self.main["temp_max"]

    def temp_print(self):
        unit_sym = f"{degree}C"
        if self.units == "imperial":
            unit_sym = f"{degree}F"

        print("--------------------------")
        print(f"Temperature in {self.name} is {self.temp}{unit_sym} but Feels Like {self.feels}{unit_sym}")
        print(f"Today's High Temp {self.temp_max}{unit_sym}")
        print(f"Today's Low Temp {self.temp_min}{unit_sym}")

class json_parser:
    def __init__(self, data):
        self.json_data = data
    def getObj(self):
        for index, obj in enumerate(self.json_data):
            for key, value in obj.items():
                if isinstance(obj, dict):
                    #print(f"{index} => {key} => {value}")
                    if 'lat' in key.lower():
                        self.latitude = value
                    if 'lon' in key.lower():
                        self.longitude = value
                else:
                    print(f"unknown object {obj} at {index}")
    def getLat(self):
        return self.latitude
    def getLon(self):
        return self.longitude

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get Weather of City / State / Country.")
    parser.add_argument("city", nargs="?", default="Vancouver", help="Name of the city")
    parser.add_argument("state", nargs="?", default="BC", help="Name of the state")
    parser.add_argument("country", nargs="?", default="CAN", help="Name of the country")
    parser.add_argument("--units", choices=["metric", "imperial"], default="imperial", help="Units for temperature")

    args = parser.parse_args()

    city = args.city
    state = args.state
    country = args.country
    units = args.units

    geocoder_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit={limit}&appid={api_key}"

try:
    response = requests.get(geocoder_url)
    parse = json_parser(response.json())
    parse.getObj()
    lat = parse.getLat()
    lon = parse.getLon()
    print(f"Latitude {lat} and Longitude {lon}")
    weather = City(lat, lon)
    weather.temp_print()

except Exception as e:
    print(f"Error: {e}")
