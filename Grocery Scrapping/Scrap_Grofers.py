# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 11:01:02 2020

@author: yp229
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 10:29:26 2020

@author: yp229
"""

# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
import csv

    


browser = webdriver.Chrome(r'C:\Users\yp229\.spyder-py3\chromedriver.exe') #replace with .Firefox(), or with the browser of your choice

d=browser
link="https://grofers.com/"

browser.get(link)
time.sleep(3)
innerHTML = browser.execute_script("return document.body.innerHTML")
user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'    
soup=bs(innerHTML,"html.parser")
file="C:/Users/yp229/OneDrive/Desktop/grofers_scrap.txt"
file_csv="C:/Users/yp229/OneDrive/Desktop/grofer_scrap.csv"
time.sleep(4)
browser.find_element_by_xpath("""//*[@id="app"]/div/div[2]/div[2]/header/div[2]/div[2]/div/div/div/div[1]/div[2]""").click()
time.sleep(4)
f=open(file,"w",encoding="utf-8")

container=soup.find('div',{'class':'store-card-categories'})

link_container=container.find_all('a')

for i in range(0,len(link_container)):
    link = "https://grofers.com"+link_container[i]['href']
    browser.execute_script('''window.open('',"_blank");''')
    browser.switch_to.window(browser.window_handles[-1])
    browser.get(link)
    innerHTML = browser.execute_script("return document.body.innerHTML")
    soup=bs(innerHTML,"html.parser")
    main_cat = link_container[i].text
    cat_container = soup.find_all('li',{'class':'category-list__item'})
    for j in range(0,len(cat_container)):
        link= "https://grofers.com"+cat_container[j].find('a')['href']
        browser.get(link)
        category = str(cat_container[j].text)
        if main_cat != category and category != 'New Launches': 
            innerHTML = browser.execute_script("return document.body.innerHTML")
            soup=bs(innerHTML,"html.parser")
            container = soup.find('ul',{'class':'category-sub-list list-unstyled show-el'}) 
        if str(type(container))!="<class 'NoneType'>":
            if str(container) == "":
                print(1)
            sub_cat_link=container.find_all('span')
            sub_cat="" 
            for k in range(0,len(sub_cat_link)):
                if len(sub_cat)==0 and k%2==0:
                    sub_cat = str(sub_cat_link[k].text)
                elif len(sub_cat)!=0 and k%2==0:
                    sub_cat = sub_cat + "," +str(sub_cat_link[k].text)
            print(sub_cat)
            write_string = main_cat+"||" +category+"||" +sub_cat+"\n"
            f.write(write_string)
            print("writing_done: "+ write_string)

    
    browser.close()
    browser.switch_to.window(browser.window_handles[0])
    
f.close()

with open(file, 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split("||") for line in stripped if line)
    with open(file_csv, 'w',newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow('Main Category','Category' ,'Sub Category')
        writer.writerows(lines)
    
    
