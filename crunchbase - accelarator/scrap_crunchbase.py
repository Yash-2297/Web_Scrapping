# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:07:54 2020

@author: yp229
"""

from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
import csv




browser = webdriver.Chrome(r'C:\Users\yp229\.spyder-py3\chromedriver.exe') #replace with .Firefox(), or with the browser of your choice

d=browser
link="https://about.crunchbase.com/blog/100-startup-accelerators-around-the-world/"

browser.get(link)
time.sleep(3)
innerHTML = browser.execute_script("return document.body.innerHTML")
user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'    
soup=bs(innerHTML,"html.parser")
file="C:/Users/yp229/OneDrive/Desktop/startup_accelarator.txt"
file_csv="C:/Users/yp229/OneDrive/Desktop/startup_accelarator.csv"
f=open(file,"w",encoding="utf-8")

container=soup.find_all('a',{'rel':'noopener noreferrer'})

for i in range(4,len(container)-2):
    link = container[i]['href']
    browser.execute_script('''window.open('',"_blank");''')

    browser.switch_to.window(browser.window_handles[-1])
    browser.get(link)
    innerHTML = browser.execute_script("return document.body.innerHTML")
    soup=bs(innerHTML,"html.parser")
    name= container[i].text
    print('Scrapping '+name+' '+str(i)+' out of '+ str(len(container)-2))
    short_desc = browser.find_element_by_xpath("""//*[@id="section-overview"]/mat-card/div[2]/image-with-fields-card/image-with-text-card/div/div/div[2]/div[2]/field-formatter/span""").text    
    headquarter = browser.find_element_by_xpath("""//*[@id="section-overview"]/mat-card/div[2]/image-with-fields-card/image-with-text-card/div/div/div[2]/div[3]/field-formatter/identifier-multi-formatter/span""").text
    industries = browser.find_element_by_xpath("""//*[@id="section-overview"]/mat-card/div[2]/fields-card[1]/div/span[2]""").text
    try:
        website = browser.find_element_by_xpath ("""//*[@id="section-overview"]/mat-card/div[2]/fields-card[3]/div/span[2]/field-formatter/link-formatter/a""").text
    except:
        website='None'
    
    try:
        
        linkedin = soup.find('a',{'aria-label':'View on LinkedIn'})['href']
    except:
        linkedin = 'None'
    write_string = name+"||" +short_desc+"||" +headquarter+"||" +industries+"||"+website+"||" +linkedin+"\n"
    print(write_string)
    f.write(write_string)
    browser.close()
    browser.switch_to.window(browser.window_handles[0])
    
f.close()

with open(file, 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split("||") for line in stripped if line)
    with open(file_csv, 'w',newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('Name',' Description' ,'Headquarter','Industries','Website','LinkedIn'))
        writer.writerows(lines)
    
    
