# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 10:23:47 2019

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
link="https://bangalore.quikr.com/Escrow/post-classifieds-ads/?postadcategoryid=227"
browser.execute_script('''window.open('',"_blank");''')
time.sleep(2)
browser.switch_to.window(browser.window_handles[-1])
browser.get(link)
time.sleep(3)
innerHTML = browser.execute_script("return document.body.innerHTML")
user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'    
soup=bs(innerHTML,"html.parser")
file="C:/Users/yp229/OneDrive/Desktop/scrapped.txt"
file_csv="C:/Users/yp229/OneDrive/Desktop/scrapped.csv"
f=open(file,"w",encoding="utf-8")

company=[]
container=soup.find('ul',{'class':'optionLists'})

for c in container:
    company.append(c.text)

options = {i.get_attribute('textContent'):i.get_attribute('rel') for i in d.find_elements_by_css_selector('#Brand_name_selectWrap .optionLists li:not(.optionHeading) a')}
input_element = d.find_element_by_id('Brand_name')

##################################################STACK---OVER--FLOW--SOULTION########################################################
####LINK:https://stackoverflow.com/questions/57388134/how-to-scrape-li-tag-with-class-like-active-selected

for k,v in options.items():
    input_element.click()  
    input_element.send_keys(k)
    selector = '[rel="' + v + '"]'

    WebDriverWait(d, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector))).click()
    WebDriverWait(d, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#Model_selectWrap.showCustomSelect")))
    time.sleep(4)   
    innerHTML = browser.execute_script("return document.body.innerHTML")
    user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'    
    sup=bs(innerHTML,"html.parser")
    ctnr=sup.findAll('ul',{'class':'optionLists'})
    models=[]
    for c in ctnr[1]:
               models.append( c.text)
    info= str(k) + "|" + str(models) + "\n"
    print(info)
    f.write(info)

f.close()

with open(file, 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split("|") for line in stripped if line)
    with open(file_csv, 'w',newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('company','models'))
        writer.writerows(lines)
        
time.sleep(2)
            

                                     
                                     
                                 
