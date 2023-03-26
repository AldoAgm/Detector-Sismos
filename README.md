Earthquake Tracker
This script tracks the latest earthquakes with a magnitude of 2.5 or greater that have occurred in the past hour. It uses the USGS Earthquake Hazards Program API to get the earthquake data in GeoJSON format, and then displays the location of the latest earthquake on a map using the Folium library. The location is also printed to the console along with other relevant details.

How to use
Install the required libraries using pip:

Copy code
pip install requests folium termcolor geopy
Run the script in a Python environment.

Copy code
python earthquake_tracker.py
The script will continuously check for new earthquakes every minute and print out the details of the latest one detected. A map of the earthquake location will also be displayed.

Dependencies
requests
time
folium
IPython.display
termcolor
datetime
geopy
License
This project is licensed under the MIT License - see the LICENSE.md file for details.
