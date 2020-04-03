# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 13:18:54 2019

@author: yp229
"""


from bs4 import BeautifulSoup as bs
from urllib.request import urlopen,Request
from selenium import webdriver
import numpy as np
import re
import time
import csv


browser = webdriver.Chrome(r'C:\Users\yp229\.spyder-py3\chromedriver.exe') #replace with .Firefox(), or with the browser of your choice

url=  'https://www.youtube.com/user/ShemarooEnt/search?query=full+movie'
 
browser.get(url) 
#================================================================AUTOAUTO+++++++++++++++++++
height = browser.execute_script("return document.documentElement.scrollHeight")
for y in range(15):
    browser.execute_script("window.scrollTo(0, " + str(height) + ");")
    height = browser.execute_script("return document.documentElement.scrollHeight")
    time.sleep(2)
    
innerHTML = browser.execute_script("return document.body.innerHTML")

user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'    

soup=bs(innerHTML,"html.parser")
 
container=soup.findAll('div',{'id':'contents'})



f=open("C:/Users/yp229/OneDrive/Desktop/movielist.txt","w",encoding="utf-8")

for ct in container:
    p=ct.find('a')
    if str(type(p)) == '<class \'NoneType\'>':
        print("NOT REQ")
    else:    
        part=ct.find('a')['href']
        link="https://www.youtube.com"+part
        name=ct.find('h3').text.strip()
        w= name+",,"+link+"\n"
        f.write(w)

    
 

f.close()
with open('C:/Users/yp229/OneDrive/Desktop/movielist.txt', 'r',encoding="utf-8") as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",,") for line in stripped if line)
    with open('C:/Users/yp229/OneDrive/Desktop/movielist.csv', 'w',encoding="utf-8",newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('name', 'link'))
        writer.writerows(lines)

