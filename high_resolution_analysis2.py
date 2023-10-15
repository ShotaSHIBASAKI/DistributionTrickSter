#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 08:05:30 2023

@author: shibasakishota
"""
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import sys
import latlon_utils 
#import rioxarray as rxr  we used this function to read tiff, but could cause conflict with plotting hex grids
import h3
from geopy.distance import geodesic
#from geojson import Feature, Point, FeatureCollection, Polygon
import plotly.express as px
import random
import scipy as sp
from scipy.integrate import cumtrapz
import statsmodels
from statsmodels.stats import multitest
import math


Temp=[]
Prec=[]
for i in range(len(df_real)):
        #print(df['hex_index'][i])
        if i %1000000==0:
            print(i)
        x=h3.h3_to_geo_boundary(df_real["hex_index2"].iloc[i], True)
        x=np.mean(x, axis=0)
        d=get_climate(x[1], x[0])
        if np.isnan(d.tavg.ann)==True or np.isnan(sum(d.prec[1:12]))==True:
            # estimate from the data
            d_extract=df_real[df_real['hex_index2']==df_real["hex_index2"].iloc[i]]
            d_extract=d_extract[d_extract['decimalLatitude']<89.5] # unable to get data lat is too close to 90
            d_extract=d_extract[d_extract['decimalLongitude']<179.9] # unable to get data lng is too close to 180
            d=get_climate(d_extract.iloc[:, 1], d_extract.iloc[:, 0]) 
            Temp.append(np.nanmean(d.tavg.ann)) # annual average of temperature 
            Prec.append(np.nanmean(np.sum(d.prec.iloc[:,:12], axis=1))) # annual precipition
        else:
            Temp.append(d.tavg.ann)
            Prec.append(sum(d.prec[1:12]))
df_real['Annu_Mean_Temp']=Temp
df_real['Annu_Prec']=Prec
# drop unnecesary info
df_real=df_real.drop("decimalLongitude", axis=1)
df_real=df_real.drop("decimalLatitude", axis=1)
    
df_real.head()
df_real.to_csv("Real_Biome_distributions2.csv")
df_null=df_real.drop_duplicates("hex_index2") # real animal biome
df_null=df_null.drop("Species", axis=1)
df_real.to_csv("Null_Biome_distributions2.csv") # null biome