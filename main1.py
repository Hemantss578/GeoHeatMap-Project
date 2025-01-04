
import os
import streamlit as st
from config import pdict
from core.data_loader import DataLoader
from core.preprocessor import Preprocessor
from core.map_visualizer import MapVisualizer, MapLayer, MapRenderer


# Global variable to store ratings and reviews
ratings_db = {}  # Structure: {pincode: {"ratings": [list of ratings], "reviews": [list of reviews]}}


def main():
    # Display current working directory for debugging
    current_working_directory = os.path.dirname(os.path.abspath(__file__))
    print(f"Current working directory: {current_working_directory}")

    # Initialize required classes
    data_loader = DataLoader()
    preprocessor = Preprocessor(pdict)
    map_visualizer = MapVisualizer()

    # Load datasets
    df_lstat = data_loader.load_lstat_data('datasets/Ladesaeulenregister_SEP.xlsx')
    df_geo = data_loader.load_geodata('datasets/geodata_berlin_plz.csv')
    df_residents = data_loader.load_residents_data('datasets/plz_einwohner.csv')

    # Preprocess datasets
    gdf_lstat = preprocessor.preprocess_lstat(df_lstat, df_geo)
    gdf_residents = preprocessor.preprocess_residents(df_residents, df_geo)
    gdf_lstat_summary = preprocessor.count_plz_occurrences(gdf_lstat)

    # Add postal code filter
    search_pincode = st.text_input("Enter Pincode to Filter Data")
    if search_pincode:
        filtered_residents, residents_message = filter_by_pincode(gdf_residents, search_pincode, "PLZ")
        filtered_charging_stations, stations_message = filter_by_pincode(gdf_lstat_summary, search_pincode, "PLZ")

        # Display relevant messages based on the filter
        if residents_message:
            st.success(residents_message)
        elif stations_message:
            st.warning(stations_message)

        # Add rating and review feature in the sidebar
        add_rating_and_review_sidebar(int(search_pincode))

        # Create layers with filtered data
        residents_layer = MapLayer(
            data=filtered_residents,
            value_column="Einwohner",
            color_range=["yellow", "red"],
            tooltip_template="PLZ: {PLZ}, Einwohner: {Einwohner}"
        )
        charging_stations_layer = MapLayer(
            data=filtered_charging_stations,
            value_column="Number",
            color_range=["yellow", "blue"],
            tooltip_template="PLZ: {PLZ}, Number: {Number}"
        )

        # Add layers to the map visualizer
        map_visualizer.add_layer("Residents", residents_layer)
        map_visualizer.add_layer("Charging Stations", charging_stations_layer)

        # Render the map in Streamlit
        MapRenderer.render(map_visualizer, ["Residents", "Charging Stations"])


def filter_by_pincode(data, search_pincode, pincode_column):
    """
    Filters GeoDataFrame by pincode.
    :param data: GeoDataFrame to filter.
    :param search_pincode: Pincode entered by the user.
    :param pincode_column: Column name for pincodes.
    :return: Filtered GeoDataFrame and a message to display.
    """
    if search_pincode:
        try:
            search_pincode = int(search_pincode)  # Ensure valid integer input.
            filtered_data = data[data[pincode_column] == search_pincode]
            if filtered_data.empty:
                return data, f"No data found for Pincode: {search_pincode}"
            else:
                return filtered_data, f"Showing data for Pincode: {search_pincode}"
        except ValueError:
            return data, "Please enter a valid numeric pincode."
    return data, None  # Return unfiltered data and no message if no input.


def add_rating_and_review_sidebar(pincode):
    """
    Adds a rating and review feature for a specific pincode in the sidebar.
    :param pincode: The pincode to rate and review.
    """
    global ratings_db

    with st.sidebar:
        st.subheader(f"Rate Charging Stations in Pincode: {pincode}")
        
        # Input rating and review
        rating = st.slider("Rate the charging station (1-5 Stars)", 1, 5)
        review = st.text_area("Write your review")
        
        if st.button("Submit Rating and Review", key="submit_review"):
            if pincode not in ratings_db:
                ratings_db[pincode] = {"ratings": [], "reviews": []}
            ratings_db[pincode]["ratings"].append(rating)
            ratings_db[pincode]["reviews"].append(review)
            st.success("Thank you for your feedback!")

        # Display existing ratings and reviews
        if pincode in ratings_db:
            st.subheader(f"Ratings and Reviews for Pincode: {pincode}")
            average_rating = sum(ratings_db[pincode]["ratings"]) / len(ratings_db[pincode]["ratings"])
            st.write(f"Average Rating: {average_rating:.2f} Stars")

            st.write("Reviews:")
            for idx, review_text in enumerate(ratings_db[pincode]["reviews"], start=1):
                st.write(f"{idx}. {review_text}")


if __name__ == "__main__":
    main()
