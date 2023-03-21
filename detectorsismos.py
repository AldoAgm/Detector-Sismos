

import requests
import time
import folium
from termcolor import colored

last_quake = None

while True:
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    response = requests.get(url)
    data = response.json()

    new_quake = None

    for earthquake in data["features"]:
        if last_quake is None or earthquake["properties"]["time"] > last_quake["properties"]["time"]:
            new_quake = earthquake
            print(colored("New earthquake detected!", "green"))
            print("Magnitude: ", earthquake["properties"]["mag"])
            print("Location: ", earthquake["properties"]["place"])
            print("Coordinates: ", earthquake["geometry"]["coordinates"])
            print("Time: ", earthquake["properties"]["time"])
            print("URL: ", earthquake["properties"]["url"])
            print("\n")
           

    last_quake = new_quake

  

    time.sleep(60)