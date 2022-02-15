import geopandas 
import rasterio
from rasterio.mask import mask
import json
import os

def clip (inShp,path_raster, inRaster):
    newpath = path_raster+'polygons_'+inRaster[:-4]+'/'
        
    if not os.path.exists(newpath):
            os.makedirs(newpath)
            
    df = geopandas.read_file(inShp)
    with rasterio.open(path_raster+inRaster) as ds:
        profile = ds.profile
        for index, row in df.iterrows():
            coords = [json.loads(df.to_json())['features'][index]['geometry']]
            masked, out_transform = mask(dataset=ds, shapes=coords, crop=True)
            profile.update(transform=out_transform,height=masked.shape[1],width=masked.shape[2])
            
            id_shapefile=row.id
            ids=str(id_shapefile)
            ids=(4-len(ids))*'0'+ids #applying extra '0' before the id to be able to find it easily
            outName = inRaster.replace('.tif','_'+ids+'.tif')
                
         
            with rasterio.open(newpath+outName,'w',**profile) as outds :
                for i in range (ds.count):
                    outds.write(masked[i,:,:],i+1)
                    
if __name__=='__main__' :
    #inShp = "/Volumes/My Passport/TempNaomi/Donnees/Shapefiles/2018/Yield9Plots_4326_Full.shp"
    #path_raster  ="/Volumes/My Passport/TempNaomi/Donnees/Drone/2018/Niakhar/2018_10_08/"
    #inRaster="orthoRGB_2018-10-08_georeferenced.tif"
    #annee='2018'
    inShp = "/Volumes/NAOMI/test13012022/cliptovolume.shp"
    path_raster  ="/Volumes/NAOMI/test16012022/20m/"
    inRaster= "height-20mCropped.tif"

    clip(inShp,path_raster,inRaster)