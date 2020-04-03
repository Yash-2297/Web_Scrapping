# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 13:37:49 2020

@author: yp229
"""


from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
import csv


list=[]

browser = webdriver.Chrome(r'C:\Users\yp229\.spyder-py3\chromedriver.exe') #replace with .Firefox(), or with the browser of your choice

d=browser
link=[]


with open(r'C:\Users\yp229\OneDrive\Desktop\link.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ')
    for row in spamreader:
        link.append(', '.join(row))
        
    
user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'    
#
#file="C:/Users/yp229/OneDrive/Desktop/startup_accelarator_new.txt"
file_csv="C:/Users/yp229/OneDrive/Desktop/startup_accelarator_new.csv"
#f=open(file,"w",encoding="utf-8")

k=1
for i in range(2593,len(link)):

    if i%79 == 0: 
        if k==1:
            browser.close()
            time.sleep(20)
            browser = webdriver.Chrome(r'C:\Users\yp229\.spyder-py3\chromedriver.exe') #replace with .Firefox(), or with the browser of your choice
            time.sleep(20)
            k=0
            
            
    browser.get(link[i])
    innerHTML = browser.execute_script("return document.body.innerHTML")
    soup=bs(innerHTML,"html.parser")
    name= browser.find_element_by_xpath("""//*[@id="section-overview"]/mat-card/div[2]/image-with-fields-card/image-with-text-card/div/div/div[2]/div[1]/field-formatter/blob-formatter/span""").text
    print('Scrapping '+name+' '+str(i)+' out of '+ str(len(link)-1))
    short_desc = browser.find_element_by_xpath("""//*[@id="section-overview"]/mat-card/div[2]/image-with-fields-card/image-with-text-card/div/div/div[2]/div[2]/field-formatter/span""").text    
    try:    
        headquarter = browser.find_element_by_xpath("""//*[@id="section-overview"]/mat-card/div[2]/image-with-fields-card/image-with-text-card/div/div/div[2]/div[3]/field-formatter/identifier-multi-formatter/span""").text
    except:
        headquarter = 'Nil'
    try:
        industries = browser.find_element_by_xpath("""//*[@id="section-overview"]/mat-card/div[2]/fields-card[1]/div/span[2]""").text
    except:
        industries='Nil'
    try:
        website = browser.find_element_by_xpath ("""//*[@id="section-overview"]/mat-card/div[2]/fields-card[3]/div/span[2]/field-formatter/link-formatter/a""").text
    except:
        website='None'
    
    try:
        
        linkedin = soup.find('a',{'aria-label':'View on LinkedIn'})['href']
    except:
        linkedin = 'None'
    write_string = name+"||" +short_desc+"||" +headquarter+"||" +industries+"||"+website+"||" +linkedin+"\n"
    f.write(write_string)
    print("Writing Done \n" + write_string)
    k=1

    
    
    
    
    
    
f.close()

with open(file, 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split("||") for line in stripped if line)
    with open(file_csv, 'w',newline='',encoding="utf-8") as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('Name',' Description' ,'Headquarter','Industries','Website','LinkedIn'))
        writer.writerows(lines)
    
    
