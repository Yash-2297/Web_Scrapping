# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 12:04:59 2019

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


browser = webdriver.Chrome(r'C:\Users\yp229\.spyder-py3\chromedriver.exe') #replace with .Firefox(), or with the browser of your choice


df= pd.read_csv(r'C:\Users\yp229\OneDrive\Desktop\Link_quicker.csv')

for i in range(0,len(df['URL'])):
    browser.execute_script('''window.open('',"_blank");''')
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[-1])
    link=df['URL'][i]        
    browser.get(link)
    time.sleep(3)
    innerHTML = browser.execute_script("return document.body.innerHTML")
    user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'    
    soup=bs(innerHTML,"html.parser")
    file="C:/Users/yp229/OneDrive/Desktop/scrapped"+str(i)+".txt"
    file_csv="C:/Users/yp229/OneDrive/Desktop/scrapped"+str(i)+".csv"
    f=open(file,"w",encoding="utf-8")

#OPTION SELECT THROUGH BEAUTIFULSOUP .....

    
    com=  [option['value'] for option in soup.select('#brands option[value]')   ]    
    for c in com:
        browser.find_element_by_xpath("""//*[@id="papForm"]/div[1]/div[1]/div/input[1]""").clear()
        browser.find_element_by_xpath("""//*[@id="papForm"]/div[1]/div[1]/div/input[1]""").send_keys(str(c))
        browser.find_element_by_xpath("""//*[@id="papForm"]/div[1]/div[1]/div/input[2]""").click()
        innerHTML = browser.execute_script("return document.body.innerHTML")
        soup2=bs(innerHTML,"html.parser")
        time.sleep(1)
        model=  [option['value'] for option in soup2.select('#models option[value]') ]
        time.sleep(0.5)
        print(len(model))
        info= str(c) + "|" + str(model) + "\n"
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
            
            
            
    
        
           
          

    