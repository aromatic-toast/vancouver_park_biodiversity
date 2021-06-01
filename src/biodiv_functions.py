import geopandas as gpd
import pandas as pd
from keplergl import KeplerGl

def add_species_metrics(species_gdf, parks_gdf):
    """
    Add total observation count and species richness metrics to each park in parks_gdf.
    
    Arguments
    ---------
    species_gdf (GeoDataFrame) : a dataframe of species occurrence data from GBIF. 
    parks_gdf  (GeoDataFrame)  : a dataframe of parks polygons. 
    
    Returns 
    -------
    GeoDataFrame
        Produces the parks_gdf with total observations and unique species counts for each park polygon. 
        
    Examples
    --------
    TODO 
    
    """
    parks = parks_gdf.copy()
    
    # initalize species counts 
    num_species = []
    
    # initialize species richness 
    species_richness = []
    
    for park in parks.geometry:
        
        # clip points to park
        clip = gpd.clip(species_gdf, mask=park)
        
        # check if species have been observed in park 
        if clip.notnull().sum()[0] == 0:
            num_species.append(0)
            species_richness.append(0)
            
        else:
            # add species count 
            count = len(clip)
            unique_species_count = clip.species.nunique()
            num_species.append(count)
            species_richness.append(unique_species_count)
                
    # add species count list to parks_gdf
    parks['species_count'] = num_species
    parks['species_richness'] = species_richness
    
    return parks

def plot_kepler(layers, names, config=None):
    """
    Produces a kepler plot with data specified in layers. 
    
    Arguments
    ---------
    layers (list): a list of geodataframes to add as kepler data in order of top to bottom layers.
    names (list) : a list of strings specifyig names of data layers in kepler. 
    config (dict) : A kepler config dictionary. 
    
    Returns 
    -------
    keplergl.keplergl.KeplerGl 
        A kepler plot with data layers. 
        
    Examples
    --------
    TODO
    """
    # intialize a base kepler plot 
    plot = KeplerGl(height=500)
    
    index = 0
    for layer in layers:
        # add data layer to kepler plot 
        plot.add_data(data=layer, name=names[index])
        
        # increment index 
        index += 1
        
    # check if a config is provided
    if config != None:
        plot.config = config
        
    return plot 