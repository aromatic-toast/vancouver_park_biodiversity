# author: Lesley Miller
# date: 2020/06/08


# The purpose of this script is to read in data for visualization and produce 
# a kepler map with the following data layers: 
# 1) gbif points clipped to inside parks 
# 2) the outlier parks 
# 3) the parks with no outliers 


# import libraries 
import geopandas as gpd
import pandas as pd
import biodiv_functions as bio
from keplergl import KeplerGl

# read in gbif data 
clipped_gbif = gpd.read_file('data/clean_data/clipped_gbif.shp')
clipped_gbif = clipped_gbif.rename(columns={'basis_of_r': 'record_type'})
clipped_gbif = clipped_gbif.drop(labels=['latitude', 'longitude'], axis=1)

# read in park
park_outliers = gpd.read_file('data/clean_data/park_outliers.shp')
park_outliers = park_outliers.rename(columns={'species_co': "observation_count",
                                              'species_ri': "unique_species_count",
                                              'park_prima': 'park_primary_use'})

# read in non outlier park data                                               
parks_with_no_outliers = gpd.read_file('data/clean_data/parks_with_no_outliers.shp')
parks_with_no_outliers = parks_with_no_outliers.rename(columns={'species_co': "observation_count", 
                                                                 'species_ri': "unique_species_count",
                                                                 'park_prima': 'park_primary_use'})

# kepler config dict 
config={
  "version": "v1",
  "config": {
    "visState": {
      "filters": [],
      "layers": [
        {
          "id": "inb6cun",
          "type": "geojson",
          "config": {
            "dataId": "species",
            "label": "species",
            "color": [
              18,
              147,
              154
            ],
            "columns": {
              "geojson": "geometry"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.8,
              "strokeOpacity": 0.8,
              "thickness": 1.5,
              "strokeColor": [
                202,
                242,
                244
              ],
              "colorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radius": 2,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": True,
              "filled": False,
              "enable3d": False,
              "wireframe": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": None,
            "colorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "heightField": None,
            "heightScale": "linear",
            "radiusField": None,
            "radiusScale": "linear"
          }
        },
        {
          "id": "yl5swz",
          "type": "geojson",
          "config": {
            "dataId": "park_outliers",
            "label": "park_outliers",
            "color": [
              221,
              178,
              124
            ],
            "columns": {
              "geojson": "geometry"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.8,
              "strokeOpacity": 0.8,
              "thickness": 0.5,
              "strokeColor": [
                136,
                87,
                44
              ],
              "colorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": False,
              "filled": True,
              "enable3d": False,
              "wireframe": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": {
              "name": "unique_species_count",
              "type": "integer"
            },
            "colorScale": "quantize",
            "sizeField": None,
            "sizeScale": "linear",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "heightField": None,
            "heightScale": "linear",
            "radiusField": None,
            "radiusScale": "linear"
          }
        },
        {
          "id": "csj60fv",
          "type": "geojson",
          "config": {
            "dataId": "parks",
            "label": "parks",
            "color": [
              255,
              153,
              31
            ],
            "columns": {
              "geojson": "geometry"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.8,
              "strokeOpacity": 0.8,
              "thickness": 0.5,
              "strokeColor": [
                241,
                92,
                23
              ],
              "colorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": False,
              "filled": True,
              "enable3d": False,
              "wireframe": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": {
              "name": "unique_species_count",
              "type": "integer"
            },
            "colorScale": "quantize",
            "sizeField": None,
            "sizeScale": "linear",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "heightField": None,
            "heightScale": "linear",
            "radiusField": None,
            "radiusScale": "linear"
          }
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "species": [
              "kingdom",
              "phylum",
              "class",
              "order",
              "family",
              "genus",
              "species",
              "record_type"
            ],
            "park_outliers": [
              "park_name",
              "park_type",
              "park_primary_use",
              "observation_count",
              "unique_species_count"
            ],
            "parks": [
              "park_name",
              "park_type",
              "park_primary_use",
              "observation_count",
              "unique_species_count"
            ]
          },
          "enabled": True
        },
        "brush": {
          "size": 0.5,
          "enabled": False
        },
        "geocoder": {
          "enabled": False
        },
        "coordinate": {
          "enabled": False
        }
      },
      "layerBlending": "normal",
      "splitMaps": [],
      "animationConfig": {
        "currentTime": None,
        "speed": 1
      }
    },
    "mapState": {
      "bearing": 0,
      "dragRotate": False,
      "latitude": 49.25173789017921,
      "longitude": -123.13914153164245,
      "pitch": 0,
      "zoom": 11.780827885859514,
      "isSplit": False
    },
    "mapStyle": {
      "styleType": "dark",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "label": True,
        "road": True,
        "border": False,
        "building": True,
        "water": True,
        "land": True,
        "3d building": False
      },
      "threeDBuildingColor": [
        9.665468314072013,
        17.18305478057247,
        31.1442867897876
      ],
      "mapStyles": {}
    }
  }
}

##### Make kepler map ###### 
plot = bio.plot_kepler(layers=[clipped_gbif, park_outliers, parks_with_no_outliers],
                   names=['species', 'park_outliers','parks'],
                   config=config)
                   
plot.save_to_html(file_name='results/final_report_map.html')                 

