import requests
import time
import folium
from IPython.display import HTML, display
from termcolor import colored
from datetime import datetime
from geopy.geocoders import Nominatim


quake_list = []

while True:
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson"
    response = requests.get(url)
    data = response.json()

    new_quake = None

    for earthquake in data["features"]:
        if earthquake not in quake_list:
            new_quake = earthquake
            quake_list.append(new_quake)
            print(colored("New earthquake detected!", "green"))
            print("Magnitude: ", new_quake["properties"]["mag"])
            print("Location: ", new_quake["properties"]["place"])
            print("Coordinates: ", new_quake["geometry"]["coordinates"])
            print("Depth: ", new_quake["geometry"]["coordinates"][2], "km")
            quake_time = datetime.fromtimestamp(new_quake["properties"]["time"] / 1000)
            quake_time_str = quake_time.strftime("%Y-%m-%d %H:%M:%S")
            print("Time: ", quake_time_str)
            time_diff = round((time.time() - new_quake["properties"]["time"]/1000)/60, 2)
            print("Time elapsed since the earthquake: ", time_diff, "minutes")
            print("URL: ", new_quake["properties"]["url"])
            print("\n")

            # Create a map centered at the earthquake's coordinates
            map_center = [new_quake["geometry"]["coordinates"][1], new_quake["geometry"]["coordinates"][0]]
            earthquake_map = folium.Map(location=map_center, zoom_start=5, width=400)

            # Add a marker for the earthquake
            earthquake_marker = folium.Marker(location=[new_quake["geometry"]["coordinates"][1], new_quake["geometry"]["coordinates"][0]], 
                                               popup=f"Magnitude: {new_quake['properties']['mag']}<br>Depth: {new_quake['geometry']['coordinates'][2]} km",
                                               icon=folium.Icon(color='red'))
            earthquake_marker.add_to(earthquake_map)

            # Display the map
            display(HTML(earthquake_map._repr_html_()))

            break

    quake_list = [quake for quake in quake_list if time.time() - quake["properties"]["time"] / 1000 < 3600]

    time.sleep(60)
