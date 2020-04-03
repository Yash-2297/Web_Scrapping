# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 20:52:45 2019

@author: yp229
"""

import pandas as pd
import numpy as np
from sklearn import svm
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder as le

df= pd.read_csv('C:/Users/yp229/OneDrive/Desktop/ios_all.csv')


l=[]
for t in df.Price:
    l.append(t.strip('$'))
    
sale=[]
for t in df.sales:
    sale.append(t)
    
print(len(df))
l=pd.to_numeric(l)
sale=pd.to_numeric(sale)

size=len(df)
total=[]
for i in range(size):
    total.append(l[i]*sale[i])
    
    
cd=df.create_Date
cd=cd.tolist()
usd=[]
    #2019=70 #2018=67 $2017=64 #2016=66 #2015=64 #2014=61 #2013=58 #2012=53 #2011=47 #2010=46

for i in range(len(df)):
        check=cd[i][-2:]
        if(check=='19'):
            usd.append(70)
        if(check=='18'):
            usd.append(67)     
        if(check=='17'):
            usd.append(64)
        if(check=='16'):
            usd.append(66)             
        if(check=='15'):
            usd.append(64)
        if(check=='14'):
            usd.append(61)   
        if(check=='13'):
            usd.append(58)
        if(check=='12'):
            usd.append(53)   
        if(check=='11'):
            usd.append(47)  
        if(check=='10'):
            usd.append(46)   
         
    

df['usd']=usd
df['total']=total

inr_tot=[]
for i in range(len(df)):
    inr_tot.append(total[i]*usd[i])
    
df['inr-tot']=inr_tot

sum(inr_tot)

df['Grand_total_INR']=sum(inr_tot)
df.to_csv('C:/Users/yp229/OneDrive/Desktop/analyzed_ios.csv')
