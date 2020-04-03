# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 23:41:29 2019

@author: yp229
"""



from bs4 import BeautifulSoup as bs
from urllib.request import urlopen,Request
from selenium import webdriver
import numpy as np
import re
import time
import csv

search="band baaja"
search=search.replace(" ","+")

url=  'https://www.imdb.com/find?ref_=nv_sr_fn&q='+search+'&s=all'
user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'
client = urlopen(Request(str(url), data=None, headers={'User-Agent': user_agent}))

#client=req(url)
html=client.read()
client.close()
soup=bs(html,"html.parser")

#print(soup)
#print(soup.prettify())

container=soup.findAll('div',{'class':'findSection'})

for ct in container:    
    name=container[0].find('td',{'class':'result_text'}).a['href']
    link='https://www.imdb.com'+name
    clnt = urlopen(Request(str(link), data=None, headers={'User-Agent': user_agent}))
    html=clnt.read()
    clnt.close()
    sup=bs(html,"html.parser")
    pack=sup.findAll('meta',{'name':'description'})[0]['content']
    arr=pack.split(".")
    actors=arr[1].strip(" With")
    
    
    
