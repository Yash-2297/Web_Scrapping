# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 13:18:15 2020

@author: yp229
"""

from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
import csv
    

def scrap():
    w_str = ""
    main_str = ""
    time.sleep(5)
    innerHTML = browser.execute_script("return document.body.innerHTML")
    user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'    
    soup=bs(innerHTML,"html.parser")
    container=soup.find_all('div',{'class':'col-12 c-ad-carousel__content c-ad-carousel__content'})
    
    for i in range(0,len(container)):
    
        course_name=container[i].find('span',{'class':'js-course-title d-sm-none'}).text.strip()
        uni_name=container[i].find('span',{'class':'c-ad-carousel__subtitle c-ad-carousel__subtitle--small js-course-academy'}).text.strip()
        daad_link = "https://www2.daad.de" + container[i].find('a',{'class':'list-inline-item mr-0 js-course-detail-link'})['href'].strip()
    
        sub_container=container[i].find_all('span',{'class':'c-ad-carousel__data-item c-ad-carousel__data-item--single-line'})
        l = len(sub_container)
    
        if l==4:
           tution_fees = sub_container[0].text.strip()
           start = sub_container[2].text.strip()
           duration = sub_container[3].text.strip()
        
        elif l==3:
            tution_fees = "none"
            start = sub_container[1].text.strip()
            duration = sub_container[2].text.strip()
        
        try:
            city=container[i].find('span',{'class':'c-ad-carousel__subtitle c-ad-carousel__subtitle--location c-ad-carousel__subtitle--small'}).text.strip()
        except:
            city = "Not There"
            
        w_str = city + "||" + uni_name + "||" + course_name + "||" + tution_fees + "||" + start + "||" + duration + "||" + daad_link + "\n"
        main_str = main_str + w_str
        print(w_str)
    return main_str
        


browser = webdriver.Chrome(r'C:\Users\yp229\.spyder-py3\chromedriver.exe') 

d=browser


# Open the link, Choose filters you want and also update the TOTAL NUMBER OF PAGE (which you can find at the end of page)
link="https://www2.daad.de/deutschland/studienangebote/international-programmes/en/result/?cert=&admReq=&scholarshipLC=&scholarshipSC=&degree%5B%5D=2&fos=&langDeAvailable=&langEnAvailable=&lang%5B%5D=2&cit%5B%5D=&tyi%5B%5D=&ins%5B%5D=&dur%5B%5D=&prep_subj%5B%5D=&prep_degree%5B%5D=&sort=4&subjects%5B%5D=&q=&limit=10&offset=&display=list&dat%5B%5D=&fee=&bgn%5B%5D=&lvlEn%5B%5D="
page = 107
browser.get(link)
time.sleep(6)

file="C:/Users/yp229/OneDrive/Desktop/daad.txt"
file_csv="C:/Users/yp229/OneDrive/Desktop/DAAD.csv"
f=open(file,"w",encoding="utf-8")
k=0
last_run = 0

while k>=0 and last_run < page+1:
    try:
        st = scrap()
        f.write(st)
        ele= browser.find_element_by_xpath("""/html/body/div[2]/main/div[2]/div[1]/div/div[2]/div/div/div[2]/a[2]""")
        time.sleep(4)
        browser.execute_script("arguments[0].click();", ele)
        last_run=k+1
        k=k+1
    except:
        k=-1
 
f.close()       

    
with open(file, 'r',encoding="utf-8") as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split("||") for line in stripped if line)
    with open(file_csv, 'w',newline='',encoding="utf-8") as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('City',' University Name','Course Name','Tution Fees','Start','Duration' ,'DAAD Link'))
        writer.writerows(lines)
    