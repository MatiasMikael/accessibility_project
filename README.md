# Accessibility Data Project #

*Introduction*

This project collects wheelchair-accessible locations in Helsinki using the Overpass API (OpenStreetMap data). The data is stored in a MongoDB database and visualized on an interactive map using Folium. The map supports clustering to ensure smooth performance even with large datasets.

*How It Works*

1. **Data Retrieval**:
   - The Overpass API fetches all wheelchair-accessible places in Helsinki, based on OpenStreetMap data.
   - The API query identifies nodes and ways tagged with "wheelchair=yes".

2. **Database Storage**:
   - The fetched data is stored in a MongoDB database.
   - Existing data is cleared before adding new entries to ensure consistency.

3. **Interactive Map**:
   - The map is created using Folium and centers around Helsinki.
   - Markers for accessible locations are added to the map using clustering for better performance.
   - The map is saved as an HTML file, which can be opened in any modern browser.

*Technologies Used*

- *Python*: Handles API calls, database operations, and map generation.
- *MongoDB*: Stores and manages the data.
- *Folium*: Creates the interactive map.
- *Overpass API*: Retrieves wheelchair-accessible location data from OpenStreetMap.

*Setup Instructions*

1. Clone this repository:
   ```
   git clone <repository_url>
   cd accessibility_project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up MongoDB:
   - Ensure MongoDB is installed and running locally.
   - Create a database directory if it doesn’t already exist:
     ```
     mkdir C:\data\db
     ```
   - Start the MongoDB server:
     ```
     mongod --dbpath C:\data\db
     ```

4. Run the project:
   - Execute the main Python script:
     ```
     python main.py
     ```

5. Open the generated map:
   - Find the file `accessible_places_map.html` in the project directory.
   - Open it in your browser to view the interactive map.

*Data License*

The wheelchair-accessibility data is retrieved from OpenStreetMap via the Overpass API. OpenStreetMap data is made available under the *Open Database License (ODbL)*. More details about the license can be found at:
```https://www.openstreetmap.org/copyright```.

*Project License*

This project is licensed under the MIT License.
