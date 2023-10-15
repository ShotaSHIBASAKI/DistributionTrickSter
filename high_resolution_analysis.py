#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 08:01:54 2023

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
#import statannot
df=pd.read_csv('TrickSter_data4.csv')

# read all real animal distributiosn
df_meta=pd.read_csv('./GBIF/For_gbif_trickstar.xlsx - Sheet1.csv') # meta file
species=np.unique(df_meta['Category'])
for i in range(len(species)):
    target=species[i]
    print(target)
    if target != 'water bird' and target != 'monkey':
        taxa=df_meta[df_meta['Category']==target]['Taxa'].reset_index(drop=True)
        for j in range(len(taxa)):
            if j==0:
                data=pd.read_csv('./GBIF/'+target+'/'+taxa[j]+'_cleaned.csv')
                data["Species"]=target
            else:
                dd=pd.read_csv('./GBIF/'+target+'/'+taxa[j]+'_cleaned.csv')
                dd["Species"]=target
                data=pd.concat([data,dd])
        # drop overlapped index within the same animal category
        data=data.drop_duplicates("hex_index2")
        
    if i !=0:
        df_real=pd.concat([df_real,data])
    else:
        df_real=data
df_real=df_real.drop("hex_index", axis=1)
df_real.head()