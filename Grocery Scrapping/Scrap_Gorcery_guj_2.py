# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 17:12:19 2020

@author: yp229
"""



from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
import csv

    


browser = webdriver.Chrome(r'C:\Users\yp229\.spyder-py3\chromedriver.exe') #replace with .Firefox(), or with the browser of your choice

d=browser

link="https://www.homebethe.com/"

browser.get(link)
time.sleep(6)
innerHTML = browser.execute_script("return document.body.innerHTML")
user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'    
soup=bs(innerHTML,"html.parser")
file="C:/Users/yp229/OneDrive/Desktop/grocery_scrap_3.txt"
file_csv="C:/Users/yp229/OneDrive/Desktop/grocery_scrap_3.csv"
f=open(file,"w",encoding="utf-8")

container=soup.find('ul',{'class':'sub-menu-1'})

cat_container = container.find_all('ul',{'class':'sub-menu-2'})

main_cat =container.find_all('a',{'class':'menu-iteam-link w-inline-block'})

for i in range(0,len(main_cat)):
    Main_Category = main_cat[i].text
    
    
    for j in range(0,len(cat_container)-1):
        cat  = cat_container[j].find_all('h5')
        for t in range(0,len(cat)-1):
            category = cat[t].text
            try:
                range_k = cat_container[j].find_all('ul')[t].find_all('a') #sub category list
            except:
               range_k = cat_container[j].find_all('ul')[t-1].find_all('a') 
            sub_category = "" 
            for k in range(0,len(range_k)-1):
                sub_cat=range_k[k].text
                
                if len(sub_category)==0:
                    sub_category = str(sub_cat).strip()
                else:
                    sub_category = sub_category + ", "+str(sub_cat).strip()
           
                
            write_string = str(Main_Category).strip()+" || "+str(category).strip()+" || "+sub_category.strip()+"\n"
            f.write(write_string)
            print('writing done for: '+write_string)
    
f.close()

with open(file, 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split("||") for line in stripped if line)
    with open(file_csv, 'w',newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('Main Category','Sub Category'))
        writer.writerows(lines)
    
    
