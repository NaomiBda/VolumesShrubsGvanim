# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 11:59:44 2022

@author: nao96
"""

import rasterio as rio 
import numpy as np


def calculateVolume(path_raster,minElev):
    '''
    input a clipped raster of the elevation to calculate thevolume of
    the definition of one pixel
    the minimum elevation to consider
    output :the volume of the srub

    '''
    src=rio.open(path_raster)
    (n,m)=np.shape(src.read(1))
    (res_x,res_y)=src.res
    volume=0
    area=0
    for k in range(n):
        for j in range(m):
            value=src.read(1)[k,j]
            if value>0:
                volume+= value*res_x*res_y
                area+=res_x*res_y
                
            
    return(volume,area)


if __name__=='__main__' :
   
    path_raster='E:/test16012022/20m/clippedbush.tif'
    print(calculateVolume(path_raster, 0))
    
    