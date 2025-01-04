# Advanced Software Engineering

## Heatmaps: Electric Charging Stations and Residents in Berlin

**Project done by group 15:**
- **Shaheen Tasneem,** 
- **Remezova Nataliia,** 
- **Pandey Navnish Suryaprakash,** 
- **Rohrscheidt Sebastian**         
   
### Project Overview  
This project aims to visualise the spatial distribution of residents and electric charging 

stations using heatmaps. It offers an interactive platform for analysing geospatial and 

demographic data, utilising Streamlit for an intuitive interface. By providing heatmaps 

that highlight population density and charging station distribution, this project enables 

users to identify infrastructure gaps and make data-driven decisions.


### Purpose
The significant purpose of heatmaps: electric charging station project is to provide a user-friendly tool for visualising and analysing the spatial distribution of residents. 

1. By leveraging geospatial and demographic data, the project helps assess the adequacy of electric vehicle infrastructure.
    
2. Using Streamlit, the interface simplifies complex data analysis tasks, enabling insights into population density and charging station allocation. 

### Scope
1. Data Visualization 
1. Heatmaps showcasing the density of residents and electric charging stations across the region.
2. Residents: Heatmap showing population distribution by postal code
3. Charging_Stations:  Heatmap displaying the density of charging stations and their nominal power
2. Interactive Features
1. Navigate through Berlin's map with pan and zoom functionality.
2. Dynamic legends to show density scales.
3. Heatmaps feature a colour gradient for better visual interpretation.

## Setup and Prerequisites
### Installation Requirements 

1. Install the required libraries listed in the “requirement.txt” file.
    
2. The following datasets are downloaded and placed in the datasets folder:  

1. Ladesaeulenregister_SEP.xlsx
    
2. Ladesaeulenregister.csv
    
3. plz_einwohner.csv
    

### Technologies Used
1. Programming Language: Python 3.12

2. Libraries:
    

1. Data Processing: pandas, geopandas .
    
2. Visualisation: folium, streamlit, streamlit-folium, branca . 

## Program Structure

1. Data Input and Preprocessing

1. Datasets Used:
- geodata_berlin_plz.csv: Contains geospatial data for Berlin postal codes.
    
- Ladesaeulenregister_SEP.xlsx: Includes details about electric vehicle charging stations in Germany.
    
- plz_einwohner.csv: Contains data on resident populations by postal code in Berlin.
    

3. Preprocessing Steps:
    

- Residents Data:
    

1. Population data is filtered for Berlin postal codes.
    
2. Data is cleaned to remove invalid or missing entries.
    
3. Merged with geospatial data to create a GeoDataFrame.
    

- Charging Station Data:
    

4. Charging station details (postal code, coordinates, and nominal power) are filtered for Berlin.
    
5. Latitude and longitude values are standardised for accuracy.
    
6. Data is aggregated by postal code to count the number of charging stations.
    

2. Geospatial Processing
    

- Residents Data: Geospatial boundaries (postal code areas) are merged with population data to map the density of residents.
    
- Charging Stations Data: Charging station locations are matched with geospatial boundaries, and counts are aggregated by postal code.
    
- Geometry Validation: All datasets are checked for valid spatial geometries to ensure accurate rendering on maps.
     

3. Visualisation Generation
    
- Residents Heatmap:  
    A choropleth map displaying population density across Berlin postal codes, using a gradient colour scheme from yellow (low density) to red (high density).
    
- Charging Stations Heatmap:  
    A heatmap visualising the density of EV charging stations by location, with darker colours representing higher densities.
    
- Additional Layered Heatmaps:  

- Charging stations visualised by their nominal power (KW) in separate layers.
    
- Dynamic legends and tooltips provide on-demand details for each postal code. 

4. Streamlit Application
- Layer Selection: Users can toggle between visualisations of residents, charging stations, and additional layers based on nominal power.
    
- Pan and Zoom: Allows for detailed exploration of Berlin's regions.
    
- Tooltips: Display postal code and relevant metrics (e.g., number of residents or charging stations) when hovered over.
    
- Dynamic Legends: Updated in real-time to reflect the selected layer's density scales.
