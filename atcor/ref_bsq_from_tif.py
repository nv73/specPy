# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 10:10:55 2020

@author: nick.viner
"""

import exifread
import pandas as pd
from pyproj import Proj
import numpy as np
from math import floor

def exif_coordinate_convert(coordList):
    
    c = str(coordList)
    c = c.replace("[", "")
    c = c.replace("]", "")
    c = c.split(",")
    
    deg = float(c[0])
    
    minute = c[1]
    minute = c[1].split(r"/")
    minute = (float(minute[0]) / float(minute[1])) / 60.0
    
    sec = round((minute - floor(minute)) *  60.0, 3)
    
    deg = deg + minute

    return(deg)



projection = Proj(proj='utm',zone=10,ellps='WGS84', preserve_units=False)

filepath = r"D:\Hyperspectral\Phase1_tests\raw\16-57-37.046_RGB_35297_38715_rgbi.tif"

file = open(filepath, 'rb')

tags = exifread.process_file(file)

file.close()

lat = exif_coordinate_convert(tags["GPS GPSLatitude"])
long = exif_coordinate_convert(tags["GPS GPSLongitude"]) * -1

x,y = projection(long, lat)
res = 1
zone = 10
mapInfo = "{UTM, 1, 1, %f, %f, %f, %f, %i, North}" % (x, y, res, res, zone)

headerfile = filepath[:-4] + "_img.hdr"

hdr = pd.read_csv(headerfile, header=None, sep="^")

newRow = pd.Series(data = "map info = {UTM, 1, 1, %f, %f, %f, %f, %i, North}" % (x, y, res, res, zone), name='15')
hdr = hdr.append(newRow)

print(hdr.iloc[15][0])

file = open(headerfile, 'a')

file.write(hdr.iloc[15][0])

file.close()


    

