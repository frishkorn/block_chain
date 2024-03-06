# ISS Blockchain - frishkorn.com
#### This source code is a Python script that plots the last 100 entries of a blockchain on a world map using the Folium library. It reads data from a JSON file, extracts the latitude and longitude coordinates, calculates the age of each entry, and assigns marker colors based on the age. The resulting map is saved as an HTML file.

## Table of Contents
* Introduction
* Requirements
* Usage Instructions
* Code Comments
* Examples
* Configuration
* Troubleshoot
* Limitations
* Conclusions
* Usage Examples

### Introduction
The script takes the last 100 entries of a blockchain and plots them on a world map. It uses the Folium library to create the map and markers. The marker colors are determined based on the age of each entry, with different colors representing different age ranges. The resulting map is saved as an HTML file.

### Requirements
#### The script requires the following:

* Python 3.x
* Folium library
* JSON file containing blockchain data

### Usage Instructions
To use the script:

Ensure that Python 3.x is installed on your system.
Install the Folium library by running the command pip install folium.
Place the JSON file containing the blockchain data in the same directory as the script and name it blockchain_data.json.
Run the script using the command python script.py.
The resulting map will be saved as iss_locations_map.html.
Code Comments
The code is well-commented to explain its functionality and logic. Here are some important comments:

The script starts by loading the data from the JSON file using the json.load() function.
A Folium map is created with an initial location at coordinates [0, 0] and a zoom level of 4.
The script iterates over the last 100 entries of the data and extracts the latitude and longitude coordinates from each entry.
The timestamp is extracted and converted to a datetime object for calculating the age in minutes.
The marker color is determined based on the age of the entry.
A marker is added to the map for each entry, with a popup displaying the entry index, geographical location, and timestamp.
The resulting map is saved as an HTML file.

### Examples
Here are some examples of how the script can be used:

Visualizing the movement of a cryptocurrency by plotting its blockchain data on a map.
Tracking the location and age of satellite data by plotting it on a map.
Analyzing the distribution of data points in a dataset by plotting them on a world map.
Configuration
The script does not require any specific configuration. However, you can modify the following parameters:

data_file: The name of the JSON file containing the blockchain data.
map_location: The initial location of the map.
marker_colors: The colors assigned to markers based on the age of the entry.
Troubleshoot
If you encounter any issues while running the script, consider the following:

Make sure that the JSON file containing the blockchain data is present in the same directory as the script and named correctly.
Check that you have installed the required dependencies, including Python 3.x and the Folium library.
Verify that the JSON file is in the correct format and contains the necessary data fields.
If the map is not displaying correctly, check your internet connection and ensure that the map tiles are loading properly.
Limitations
The script has the following limitations:

It only plots the last 100 entries of the blockchain. If you have more data, you may need to modify the script to handle larger datasets.
The marker colors are determined based on fixed age ranges. You may need to adjust the color thresholds to better represent the age distribution of your data.
The script assumes that the JSON file contains the necessary data fields in the expected format. If your data is structured differently, you may need to modify the code accordingly.
Conclusions
The script provides a convenient way to visualize blockchain data on a world map. By plotting the data points and assigning marker colors based on age, it allows for easy analysis and interpretation of the data. The resulting map can be saved as an HTML file for further sharing and exploration.
