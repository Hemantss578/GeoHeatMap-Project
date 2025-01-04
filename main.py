# -----------------------------------------------------------------------------
import os

currentWorkingDirectory = os.path.dirname(os.path.abspath(__file__))
print(f"Current working directory: {currentWorkingDirectory}")

# os.chdir(currentWorkingDirectory)
# print("Current working directory\n" + os.getcwd())

import pandas as pd
import geopandas as gpd
from core import methods as m1
from core import HelperTools as ht

from config import pdict

# -----------------------------------------------------------------------------
@ht.timer
def main():
    """Main: Generation of Streamlit App for visualizing electric charging stations & residents in Berlin"""

    # Load data (replace 'your_file_path' with actual file paths or data sources)
    df_geodat_plz = pd.read_csv('datasets/geodata_berlin_plz.csv', sep=';')  
    df_lstat = pd.read_excel('datasets/Ladesaeulenregister_SEP.xlsx', header=10)
    df_residents = pd.read_csv('datasets/plz_einwohner.csv')

    # Preprocess data
    gdf_lstat = m1.preprop_lstat(df_lstat, df_geodat_plz, pdict)
    gdf_lstat3 = m1.count_plz_occurrences(gdf_lstat)

    gdf_residents2 = m1.preprop_resid(df_residents, df_geodat_plz, pdict)

    # Generate Streamlit app
    m1.make_streamlit_electric_Charging_resid(gdf_lstat3, gdf_residents2)

# -----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
