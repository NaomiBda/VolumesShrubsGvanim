# Volumes Shrubs Gvanim
scripts to calculate the volume of shrubs using drone rasters of the area

## Before running the script

You may install the follwing packages : 
* rasterio (reads raster) 
* geopandas (reads shapefiles) 

Run this line in the command prompt: 

```bash
conda install -c conda-forge geopandas rasterio descartes 
```

## Description of the repository 

This repository contains three files : 

* **clip_raster** :  From a polygon shapefile and a raster, clips the raster according to the polygons and put the newly created files in a new folder called "polygons"
* **Volumeshrubs** : From a raster, calculate the volume buy multiplying the surface of a pixel with the pixel value. This only makes sense if the pixel value is the height, elevation . 
* **main** is the file combining the two files. It first clips the raster then calcule each value of volume. It then condense these data on a CSV file which is automaticcaly created. 

## Input 

There are three input to this script. Everything must be written in the **main.py** file. 
```bash
path_raster  ="D:/Gvanim/rasters/" 
raster_name="raster-HEIGHT.tif"
shapefile_path='D:/Gvanim/shapefiles/shrubs-SOUTH5.shp'
```
* **path_raster** is the path where the raster is. It must end with / . It is an str. There mustn't be any \ in the str 
* **raster_name** is the name of the raster. It must be a raster of the height of the shrubs, which can be calculated previouly using GIS (DSM-DTM with the raster calculator).
*  **shapefile_path** is the complete path of the shapefile, including its name. It is the path where the shapefile of th polygons is. 


## Output
