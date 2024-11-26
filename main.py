import requests
import json
from pymongo import MongoClient
import folium
from folium.plugins import MarkerCluster  # Import the MarkerCluster plugin

# Overpass API endpoint and query to retrieve wheelchair-accessible places in Helsinki
url = "https://overpass-api.de/api/interpreter"
query = """
[out:json];
(
  node["wheelchair"="yes"](60.10,24.80,60.30,25.10);
  way["wheelchair"="yes"](60.10,24.80,60.30,25.10);
);
out body;
>;
out skel qt;
"""

# Step 1: Fetch data from Overpass API
response = requests.post(url, data=query)

if response.status_code == 200:
    data = response.json()
    print(f"Found {len(data['elements'])} accessible places in Helsinki.")
else:
    print(f"API request failed with status code: {response.status_code}")
    print(f"Response text: {response.text}")
    exit()

# Step 2: Save the data to MongoDB
# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["accessibility_data"]
collection = db["places"]

# Clear the existing collection and insert new data
collection.delete_many({})  # Delete all existing documents
if 'elements' in data:
    collection.insert_many(data['elements'])  # Insert new data into MongoDB
    print(f"Saved {len(data['elements'])} accessible places to MongoDB.")
else:
    print("No elements found in the API response.")

# Step 3: Create a map with clustering
print("Retrieving data from MongoDB...")
places = collection.find()  # Fetch all documents from the collection

# Create a map centered in Helsinki
map = folium.Map(location=[60.1695, 24.9354], zoom_start=12)

# Create a MarkerCluster object
marker_cluster = MarkerCluster().add_to(map)

# Add markers for accessible places to the cluster
for place in places:
    if "lat" in place and "lon" in place:
        folium.Marker(
            location=[place["lat"], place["lon"]],
            popup=place.get("tags", {}).get("name", "Accessible place")
        ).add_to(marker_cluster)

# Save the map as an HTML file
map.save("accessible_places_map.html")
print("Map saved as accessible_places_map.html.")