# author: Lesley Miller 
# date: 2020/06/08

# The  purpose of this script is to read in clean gbif and parks data and write a new parks 
# dataframe that contains total species observations and species richness per park and write 
# clipped_gbif and parks_outliers to new shapefiles for kepler visualization 

import geopandas as gpd
import pandas as pd
import biodiv_functions as bio

# load gbif 
print("Loading species data...")
gbif = gpd.read_file('data/clean_data/vancouver_gbif.shp')

# load parks 
print('Loading parks data...')
parks = gpd.read_file('data/clean_data/vancouver_parks.shp')

# clip the gbif data to inside parks 
print("Clipping species data to inside parks...")
clipped_gbif = gpd.clip(gdf=gbif, mask=parks)


# add species metrics for all parks
print("Calculating species metrics...")
parks_counts_gdf = bio.add_species_metrics(species_gdf=clipped_gbif, parks_gdf=parks)
counts_df = pd.DataFrame(parks_counts_gdf)


##### Prepare dataframes for visualization layers #### 

# get outliers dataframe 
park_outliers = parks_counts_gdf.query('park_name == "Stanley Park" | park_name == "Pacific Spirit"')

# remove outliers from parks data 
parks_with_no_outliers = parks_counts_gdf.drop(labels=park_outliers.index)


# write new shapefiles 
print("Writing new shapefiles for visualization...")
clipped_gbif.to_file('data/clean_data/clipped_gbif.shp')
park_outliers.to_file('data/clean_data/park_outliers.shp')
parks_with_no_outliers.to_file('data/clean_data/parks_with_no_outliers.shp')
counts_df.to_csv('data/clean_data/all_parks_with_metrics.csv', index=False)


