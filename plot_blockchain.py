#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
[Blockchain Plotting Script]

This script takes the last 100 entries of the blockchain and plots them to a world map.
"""

import folium, json, time
from datetime import datetime
from geopy.geocoders import Nominatim

if __name__ == "__main__":

    # Load data from the JSON file
    with open('blockchain_data.json', 'r') as json_file:
        data = json.load(json_file)

    # Create a folium map centered at the initial location
    map = folium.Map(location=[0, 0], tiles="CartoDB_Positron", attr="OpenStreetMap", zoom_start=2)

    # Plot only the last 100 ISS locations on the map
    for i, entry in enumerate(data[-100:]):  # Iterate over the last 100 entries (~1-1/2 hr).
        lat_str, lon_str = entry["data"].split(":")[1].split(",")
        lat, lon = float(lat_str.split()[1]), float(lon_str.split()[1])

        # Extract timestamp and calculate age in minutes
        timestamp_str = entry['timestamp']
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S.%f")
        current_time = datetime.utcnow()
        age_in_minutes = (current_time - timestamp).total_seconds() / 60

        geolocator = Nominatim(user_agent="block_iss")  # Replace "your_app_name" with a unique identifier

        # Reverse geocode to get the city name from coordinates
        location = geolocator.reverse([lat, lon], language='en')

        # Check if the location is found
        if location and location.address and len(location.address.split(",")) >= 3:
            city_name = location.address.split(",")[-3]  # Extracting the city name from the address
        else:
            city_name = "Unknown"
        time.sleep(0.5)

        # Set marker color based on age
        if age_in_minutes > 60:
            marker_color = 'red'
        elif age_in_minutes > 30:
            marker_color = 'orange'
        elif age_in_minutes > 1:
            marker_color = 'green'
        else:
            marker_color = 'blue'

        # Add marker to the map
        folium.Marker(
            [lat, lon],
            popup=f"ISS Location {entry['index']} - {city_name} - {entry['timestamp']}",
            icon=folium.Icon(color=marker_color, prefix="fa", icon="satellite")
        ).add_to(map)

    # Save the map to an HTML file
    map.save('iss_locations_map.html')

