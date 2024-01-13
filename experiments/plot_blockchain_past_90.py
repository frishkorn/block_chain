import folium, json
from datetime import datetime

# Load data from the JSON file
with open('blockchain_data.json', 'r') as json_file:
    data = json.load(json_file)

# Create a folium map centered at the initial location
mymap = folium.Map(location=[0, 0], zoom_start=2)

# Plot only the last 100 ISS locations on the map
for i, entry in enumerate(data[-90:]):  # Iterate over the last 28 entries.
    lat_str, lon_str = entry["data"].split(":")[1].split(",")
    lat, lon = float(lat_str.split()[1]), float(lon_str.split()[1])

    # Extract timestamp and calculate age in minutes
    timestamp_str = entry['timestamp']
    timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S.%f")
    current_time = datetime.utcnow()
    age_in_minutes = (current_time - timestamp).total_seconds() / 60

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
        popup=f"ISS Location {entry['index']} {entry['timestamp']}",
        icon=folium.Icon(color=marker_color, prefix="fa", icon="satellite")
    ).add_to(mymap)

# Save the map to an HTML file
mymap.save('iss_locations_map.html')

