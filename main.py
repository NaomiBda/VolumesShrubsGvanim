# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 15:12:54 2022

@author: nao96
"""

import Volumeshrubs as Vs
import clip_raster as cr
import csv
import os
import shutil


def write_volume_results(raster_path,raster_name,shapefile_path):
    cr.clip(shapefile_path,raster_path,raster_name)
    path_shrubs=raster_path+'polygons_'+raster_name[:-4]+'/'
    
    with open(raster_path+'Volumes_'+raster_name[:-4]+'.csv', 'w',newline='') as csvfile:
            fieldnames = ['ID number', 'Volume','Area']
            
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for file in os.listdir(path_shrubs):
                (volume,area)=Vs.calculateVolume(path_shrubs+file, 0)
                shrub_id=file[-8:-4]
                row={'ID number':shrub_id,'Volume':volume,'Area':area}
                writer.writerow(row)
    shutil.rmtree(path_shrubs)

if __name__=='__main__':
    ###enter raster path and raster name here :
    path_raster  ="D:/Gvanim/mosaic/Elevation/SOUTH/"
    raster_name="South5-Height-HEIGHT.tif"
    shapefile_path='E:/Mop Avshalom 2022/shapefiles Gvanim/shrubs/shrubs_BLOCKS/shrubs-SOUTH5.shp'
    write_volume_results(path_raster,raster_name,shapefile_path)
