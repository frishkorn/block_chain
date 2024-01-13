import folium, json

# Load data from the JSON file
with open('blockchain_data.json', 'r') as json_file:
    data = json.load(json_file)

# Create a folium map centered at the initial location
mymap = folium.Map(location=[0, 0], zoom_start=2)

# Plot ISS locations on the map, skipping the first entry
for i, entry in enumerate(data):
    if i == 0:
        continue  # Skip the first entry
    
    lat_str, lon_str = entry["data"].split(":")[1].split(",")
    lat, lon = float(lat_str.split()[1]), float(lon_str.split()[1])
    folium.Marker([lat, lon], popup=f"ISS Location {entry['index']} {entry['timestamp']}").add_to(mymap)

# Save the map to an HTML file
mymap.save('iss_locations_map.html')
