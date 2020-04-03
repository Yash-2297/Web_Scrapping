# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 15:13:39 2020

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



browser = webdriver.Chrome(r'C:\Users\yp229\.spyder-py3\chromedriver.exe') #replace with .Firefox(), or with the browser of your choice

d=browser
link="https://www.mohfw.gov.in/"
#browser.execute_script('''window.open('',"_blank");''')
#time.sleep(2)
#browser.switch_to.window(browser.window_handles[-1])
browser.get(link)
time.sleep(3)
innerHTML = browser.execute_script("return document.body.innerHTML")
user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'    
soup=bs(innerHTML,"html.parser")
file="C:/Users/yp229/OneDrive/Desktop/corona_txt.txt"
file_sum="C:/Users/yp229/OneDrive/Desktop/corona.txt"
f=open(file,"w",encoding="utf-8")

container=soup.find('ol',{'dir':'ltr'})

t= container.text
t=t.replace ('\n\n\n','|||')
k=t.split('||||||',1)[0]
states= k.split('|||',1)[1].split('|||',1)[1]
summary = k.split('|||',1)[0]

k.split('|||',1)[1].split('|||',1)[0]


f.write(states[2:].replace('\n','|').replace('|||','\n'))

f.close()
f=open(file_sum,"w",encoding="utf-8")
f.write(summary)
f.close()

with open("C:/Users/yp229/OneDrive/Desktop/corona.txt", 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split("|") for line in stripped if line)
    with open("C:/Users/yp229/OneDrive/Desktop/scrapped_corona.csv", 'w',newline='') as out_file:
        writer = csv.writer(out_file)
        #writer.writerow(('S. No.','Name of State','Total Confirmed cases (Indian National)','Total Confirmed cases ( Foreign National )','Cured/Discharged','Death'))
        writer.writerows(lines)
        
with open("C:/Users/yp229/OneDrive/Desktop/corona_txt.txt", 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split("|") for line in stripped if line)
    with open("C:/Users/yp229/OneDrive/Desktop/scrapped_corona.csv", 'a',newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('S. No.','Name of State','Total Confirmed cases (Indian National)','Total Confirmed cases ( Foreign National )','Cured/Discharged','Death'))
        writer.writerows(lines)

        