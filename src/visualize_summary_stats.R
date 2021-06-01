# author: Lesley Miller 
# date: 2020/06/08

# The purpose of this script is to generate plots and save them for embedding in the final report. 


# load libraries 
library(tidyverse)
library(sf)
library(knitr)
library(gridExtra)


# load gbif
gbif <- st_read('data/clean_data/vancouver_gbif.shp')

# load clipped_gbif
clipped_gbif <- st_read('data/clean_data/clipped_gbif.shp')

# load outlier parks 
outlier_parks <-  st_read('data/clean_data/park_outliers.shp')

# load parks with no outliers 
parks_with_no_outliers <- st_read('data/clean_data/parks_with_no_outliers.shp')



# Question 1 
observed_in_park <- nrow(clipped_gbif)
outside_park <-  nrow(gbif) - observed_in_park

species_in_out_df <- tibble(count_observed_in_park = c('yes', 'no'),
                            count = c(observed_in_park, outside_park))

#### compare observation count within and outside parks #### 
plot1 <- species_in_out_df %>%  
      ggplot(aes(x = count_observed_in_park, y = count, color = count_observed_in_park)) + 
      geom_col() + 
      labs(title = "Comparison Between Species Observations Found Inside and Outside a Park",
           x = 'Whether Species is Observed in a Park',
           y = 'Count of Species') + 
      theme(legend.position = "none")

# Question 2: What are the top 10 parks with the highest observations?
obs_hotspots_no_outliers <- parks_with_no_outliers %>% 
      arrange(desc(species_co)) %>% 
      head(10) %>% 
      select(park_name, species_co, species_ri)

plot2 <- obs_hotspots_no_outliers %>% 
      ggplot(aes(x = reorder(park_name, species_counts), y = species_counts)) + 
      geom_col() + 
      labs(title = "Top Ten Observation Hotspots",
           x = 'Park Name',
           y = 'Count of Observations') +
      coord_flip()


#### outliers #### 
plot2_1 <- outlier_parks %>% 
      ggplot(aes(x = park_name, species_counts)) +
      geom_col() + 
      labs(title = "Outlier Observation Hotspots",
           x = 'Park Name',
           y = 'Count of Observations') +
      coord_flip()


##### Question 3: which parks have the most species richness? ##### 
top_species_rich <- parks_with_no_outliers %>% 
      arrange(desc(species_ri)) %>% 
      head(10) %>% 
      select(park_name, species_co, species_ri)

plot3 <- top_species_rich %>% 
      ggplot(aes(x = reorder(park_name, species_ri), y = species_ri)) + 
      geom_col() + 
      labs(title = "Top Ten Parks for Species Richness",
           x = 'Park Name',
           y = 'Unique Species Count') +
      coord_flip()

### outliers species richnesss ###
plot3_1 <- outlier_parks %>% 
      ggplot(aes(x = reorder(park_name, species_ri), y = species_ri)) + 
      geom_col() + 
      labs(title = "Outlier Parks for Species Richness",
           x = 'Park Name',
           y = 'Unique Species Count') +
      coord_flip()

plot_grid1 <- grid.arrange(plot2, plot3)
plot_grid2 <- grid.arrange(plot2_1, plot3_1)

#### Save Plots and Tables for final report #### 
ggsave(filename = "no_outliers.png", plot = plot_grid1, path = 'results/')
ggsave(filename = "outliers.png", plot = plot_grid2, path = 'results/')
ggsave(filename = "within_outside_parks.png", plot = plot1, path = 'results/')
ggsave(filename = "obs_hotspots_no_outliers.png", plot = plot2, path = 'results/')
ggsave(filename = "top_species_rich.png", plot = plot3, path = 'results/')

