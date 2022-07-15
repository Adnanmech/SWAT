# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 17:11:00 2020

@author: PKSA
"""

import pandas as pd




# Reading Sample file for basin
pcp=pd.read_csv("E:\\Adnan\\GridModel\\CC INPUT SWAT-v2\\CC INPUT SWAT\\Baram\\CCSM4\\4.5\\pcp1.pcp")
tmp=pd.read_csv("E:\\Adnan\\GridModel\\CC INPUT SWAT-v2\\CC INPUT SWAT\\Baram\\CCSM4\\4.5\\Tmp1.Tmp")


date=pcp.iloc[3:,0:1].astype(str)
date=date[date.columns[0]].str.slice(0, 7, 1)
date.index = range(len(date.index))
# Percipitation station uses in the basin
pcpstations=pcp.columns[0:-1]
pcpstations=list(pcpstations)
pcpstations[0]=pcpstations[0].split(" ")[-1]

# Temperture station uses in the basin
tmpstations=tmp.columns[0:-1]
tmpstations=list(tmpstations)
tmpstations[0]=tmpstations[0].split(" ")[-1]

# Building pcp columns and fixing numbers format (111.11) then concatenating together inorder to
#Replace with 
#pcp.iloc[3:,0:1] 
file=pcpstations[0]
pcppath="E:\\CC_DATA\\missvaluecorected_v2\\pcporginal\\pcp\\CCSM4\\CCSM4_RCP4.5\\"


####Function for making in SWAT type
def swattype(x):
    x=round(x,1)
    x="{:.1f}".format(x)
    x=str(x)
    return x.zfill(5)

swattype(12.06)


pcprf=pd.DataFrame()
for file in pcpstations:
    
    rfdf=pd.read_csv(pcppath+file+".txt")
    rfdf=rfdf.iloc[:,0].agg(swattype,axis=0)
    pcprf=pd.concat([pcprf, rfdf], axis=1)


pcprf=pd.concat([date,pcprf], axis=1)
pcprf=pcprf[pcprf.columns].agg(''.join, axis=1)
pcp.iloc[3:,0:1]=pcprf

pcp.to_csv("E:\\Adnan\\GridModel\\CC INPUT SWAT-v2\\CC INPUT SWAT\\Baram\\CCSM4\\4.5\\"+"PCPn.pcp",sep=" ")
