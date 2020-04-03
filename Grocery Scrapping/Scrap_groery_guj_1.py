# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 15:26:02 2020

@author: yp229
"""




from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
import csv
import re

    


browser = webdriver.Chrome(r'C:\Users\yp229\.spyder-py3\chromedriver.exe') #replace with .Firefox(), or with the browser of your choice

d=browser
link="https://farsankart.com/"

browser.get(link)
time.sleep(3)
innerHTML = browser.execute_script("return document.body.innerHTML")
user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'    
soup=bs(innerHTML,"html.parser")
file="C:/Users/yp229/OneDrive/Desktop/grocery_scrap_1.txt"
file_csv="C:/Users/yp229/OneDrive/Desktop/grocery_scrap_1.csv"

f=open(file,"w",encoding="utf-8")


container=soup.find('ul',{'id':'menu-vertical-menu-2'})

category=container.find_all('li',{'class':re.compile("^menu-item menu-item-type" )})



for i in range(0,len(category)):
    Main_cat = category[i].find('a').text
    sub_cat_container = category[i].find_all('a')
    sub_cat=""
    for j in range(1,len(sub_cat_container)):
        if len(sub_cat_container[j].text) != 0:
            sub_cat =sub_cat + ", "+str( sub_cat_container[j].text )
    write_string = Main_cat+"||" +sub_cat+"\n"
    f.write(write_string)
    print("writing_done: "+ write_string)





#-------------------------------second site-------------------------#

link="https://www.laxmidals.com/"
browser.get(link)
innerHTML = browser.execute_script("return document.body.innerHTML")
user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'    
soup=bs(innerHTML,"html.parser")

container=soup.find('ul',{'class':'dropdown-menu level1'})

dal_list=''
for i in range(0,len(container)-1):
    dal = container.find_all('li',{'class':'parent dropdown-submenu '})[i].find('a').text
    dal_list= dal_list + "," + dal
write_string = "Dal/Pulses" + "||" + dal_list
f.write(write_string)
print("writing_done: "+ write_string)

            


          
f.close()

with open(file, 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split("||") for line in stripped if line)
    with open(file_csv, 'w',newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('Main Category','Sub Category'))
        writer.writerows(lines)
    
    
