# Vancouver Park Biodiversity
A project to explore GBIF species occurrence data in Vancouver parks.

- Author: Lesley Miller 

# Research Question 
Urban parks provide an array of physical and psycholocial benefits to city residents. In addition to providing space for numerous recreational activities as well as natural beauty, urban parks can also provide an interface for residents to interact with wildlife through activities such as bird watching or mushroom picking. But how much of a city's biodiversity is observed in urban parks? More specifically, for residents who will record their sightings of wildlife (plants and animals) on citizen science websites, how much of these observations occur in urban parks? This project will explore the city parks of Vancouver, British Columbia and discover the types of biodiversity that is observed due to citizen science. The project will attemp to answer the following questions: 
1) What proportion of Vancouver's biodiversity data is recorded in an urban park? 
2) Which parks contain the most observations?
3) Which parks contain the largest number of different species?

# Data Sources 

## Global Biodiversity Information Facility 
[GBIF](https://www.gbif.org/) is a massive database that contains geotagged observation data for individual species (e.g. pland and animals). Species occurrence data was obtained from GBIF for City of Vancouver as well as the area of UBC and the Endowment Lands for the years between 2009 and 2019. 

## Local & Regional Greenspaces 
Geospatial data for Vancouver parks was obtained from the [BC Data Catalogue](https://catalogue.data.gov.bc.ca/dataset/local-and-regional-greenspaces)

# Analysis Plan 
1) Geotagged species observations will be spatially clipped to obtain the observations that occur within the spatial bounds of parks. 
2) The spatial distribution of parks will be mapped with an overlay of park species obsevations. 
3) The species counts for each park will be ranked to obtain the top 10 parks with the most observations. 
4) The species richness (count of unique species) will then be calculated for each park to obtain the top 10 parks with the highest species richness. 
