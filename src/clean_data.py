# author: Lesley Miller 
# date: 2020/06/08

# the purpose of this script is to read in raw gbif and parks data files and produce cleaned 
# shapefile for analysis 

import pandas as pd
import geopandas as gpd

###### Clean GBIF shapefile ##### 

# load raw gbif 
gbif = gpd.read_file('data/raw_data/vancouver_gbif.shp')

# remove columns 
gbif = gbif[['kingdom', 'phylum', 'class','order','family', 'genus', 
      'species','decimalLat','decimalLon', 'eventDate','day','month', 'year', 
      'basisOfRec','geometry']]
      
# rename the columns
gbif = gbif.rename(columns={'decimalLat': 'latitude','decimalLon': 'longitude',
      'eventDate': 'timestamp','basisOfRec': 'basis_of_record'})

# save clean shapefile                                 
gbif.to_file('data/clean_data/gbif.shp')                                


##### Clean Parks shapefile ######
# load raw parks data 
parks = gpd.read_file('data/raw_data/vancouver_parks.shp')

# remove columns 
parks = parks[['PARK_NAME', 'PARK_TYPE', 'PARK_PRIMA', 'geometry']]

# rename columns 
parks = parks.rename(columns={'PARK_NAME':'park_name', 'PARK_TYPE': 'park_type', 'PARK_PRIMA':'park_primary_use'})
 
# save clean parks file 
parks.to_file('data/clean_data/vancouver_parks.shp')


                      
