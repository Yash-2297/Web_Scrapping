# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 15:24:28 2019

@author: yp229
"""

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen,Request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import pandas as pd
import csv
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

result=[]
df= pd.read_csv(r'C:\Users\yp229\OneDrive\Desktop\olx_final.csv')
file="C:/Users/yp229/OneDrive/Desktop/longilati.txt"
file_csv="C:/Users/yp229/OneDrive/Desktop/longilati.csv"
f=open(file,"w",encoding="utf-8")
for i in range(len(df)):
    local=[]
    print( df['local'][i])
    city=df['city'][i]
    state=df['state'][i]
    
    if df['local'][i]!="":
        
        local=(str(df['local'][i])).split('*')
        for k in range(1,len(local)):
            res= str(local[k])+","+str(city)+","+str(state)+",IN"
            result.append(res)
    
    elif df['local'][i]=="":
             res= str(city)+","+str(state)+",IN"
             result.append(res)
             
    elif df['city'][i]=="":
            print("DO NOTHING")
     
browser = webdriver.Chrome(r'C:\Users\yp229\.spyder-py3\chromedriver.exe') #replace with .Firefox(), or with the browser of your choice
link="https://www.latlong.net/"
browser.execute_script('''window.open('',"_blank");''')
time.sleep(2)
browser.switch_to.window(browser.window_handles[-1])
browser.get(link)
for i in range(len(result)):
    browser.find_element_by_css_selector("""#place""").clear()
    browser.find_element_by_css_selector("""#place""").send_keys(result[i])
    time.sleep(0.5)
    browser.find_element_by_css_selector("""#btnfind""").click()
    time.sleep(1)
    innerHTML = browser.execute_script("return document.body.innerHTML")
    user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'    
    soup=bs(innerHTML,"html.parser")
    container=soup.find('span',{'class':'coordinatetxt'})
    ans= container.text.strip()
    info=result[i]+"|"+ans+"\n"
    print(info)
    
    f.write(info)
    
f.close()


with open(file, 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split("|") for line in stripped if line)
    with open(file_csv, 'w',newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('Place','Coordinate'))
        writer.writerows(lines)

            

                        
                                      
        
        
            
            
        
        