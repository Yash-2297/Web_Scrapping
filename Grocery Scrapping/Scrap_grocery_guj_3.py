# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 19:34:34 2020

@author: yp229
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 17:12:19 2020

@author: yp229
"""



from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
import csv
import re
    


browser = webdriver.Chrome(r'C:\Users\yp229\.spyder-py3\chromedriver.exe') #replace with .Firefox(), or with the browser of your choice

d=browser

link="https://www.deliveryathome.co.in/"

browser.get(link)
time.sleep(6)
innerHTML = browser.execute_script("return document.body.innerHTML")
user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'    
soup=bs(innerHTML,"html.parser")
file="C:/Users/yp229/OneDrive/Desktop/grocery_scrap_4.txt"
file_csv="C:/Users/yp229/OneDrive/Desktop/grocery_scrap_4.csv"
f=open(file,"w",encoding="utf-8")

container=soup.find('ul',{'class':'hnav main_menu'})

cat_container = container.find_all('ul',{'class':'em-catalog-navigation '})


for i in range(0,len(cat_container)):
    t=i+1
    Main_category =container.find_all('li',{'class':re.compile("^menu-item-link")})[t].find_all('a')[1].text
    in_cat_container= cat_container[1].find_all('li',{'class':re.compile("^level0")})       
    for j in range(0,len(in_cat_container)):
        category = in_cat_container[j].find_all('a')[0].text
        if str(category).strip() == '>':
            category = in_cat_container[j].find_all('a')[1].text
        try:    
            sub_category = in_cat_container[j].find('ul').text
        except:
            sub_category = 'None'
        sub_category = str(sub_category).replace('\n\n\n\n',',').replace('\n\n\n','')
        write_string = str(Main_category).strip() + "||" + str(category).strip()+"||" + sub_category + "\n"
        f.write(write_string)
        print("writing done for : " + write_string)        

f.close()


with open(file, 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split("||") for line in stripped if line)
    with open(file_csv, 'w',newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('Main Category','Sub Category'))
        writer.writerows(lines)
    
    
