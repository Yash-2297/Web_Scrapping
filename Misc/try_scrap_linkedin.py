# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 00:50:39 2019

@author: yp229
"""


from bs4 import BeautifulSoup as bs
from urllib.request import urlopen,Request
from selenium import webdriver
import numpy as np
import re
import time
import csv
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

def refresh():
    for y in range(2):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)
        browser.execute_script("window.scrollTo(0, 100)")
        print(y)
    return

browser = webdriver.Chrome(r'C:\Users\yp229\.spyder-py3\chromedriver.exe') #replace with .Firefox(), or with the browser of your choice

url=  'https://www.linkedin.com/groups/10406658/members/'

userid = 'talkwithnirav@gmail.com'
password ='7305662131@Jay'
browser.get('https://www.linkedin.com/login')



browser.find_element_by_xpath("""//*[@id="username"]""").send_keys(userid)
browser.find_element_by_xpath("""//*[@id="password"]""").send_keys(password)
browser.find_element_by_xpath("""//*[@id="app__container"]/main/div/form/div[3]/button""").click()


browser.get(url) 
browser.find_element_by_xpath("""/html[@class='artdeco windows gr__linkedin_com']/body[@class='render-mode-BIGPIPE nav-v2 ember-application boot-complete icons-loaded']/div[@id='ember5']/div[@class='application-outlet ']/div[@class='authentication-outlet']/div[@id='groups']/div[@class='neptune-grid two-column']/div[@class='groups-members-list__core-rail core-rail Elevation-2dp pt5 ph5 pb4']/div[@id='ember48']/artdeco-typeahead[@id='ember49']/div[@class='display-flex justify-space-between mv5']/div[@class='groups-members-list__search flex-grow-0']/div[@id='ember50']/div/input""").send_keys('Nirav')

refresh()

innerHTML = browser.execute_script("return document.body.innerHTML")

user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'    

soup=bs(innerHTML,"html.parser")
 
container=soup.findAll('div',{'class':'groups-members-list__core-rail core-rail Elevation-2dp pt5 ph5 pb4'})

see=soup.findAll('div', {'id':'ember54'})
ctnr=soup.findAll('artdeco-entity-lockup-title',{'id':re.compile("^ember")})
ctnr1=soup.findAll('artdeco-entity-lockup-content',{'id':re.compile("^ember")})
ctnr2=soup.findAll('artdeco-entity-lockup-subtitle',{'id':re.compile("^ember")})
sr=0

f=open("C:/Users/yp229/OneDrive/Desktop/linkedin.txt","w",encoding="utf-8")
count=0
for ct,ct1,ct2 in zip(ctnr,ctnr1,ctnr2) :
    link=ct1.find('a')['href']
    full='https://www.linkedin.com'+str(link)
    name=ct.text.strip()
    sr=sr+1    
    other=ct2.text.strip()
    coct=full+"detail/contact-info/"
    browser.execute_script('''window.open('',"_blank");''')
    browser.switch_to.window(browser.window_handles[-1])
    browser.get(coct)
    innerHTML = browser.execute_script("return document.body.innerHTML")
    user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'    
    sup=bs(innerHTML,"html.parser")
    #ctnr_in=sup.findAll('div',{'class':'pv-contact-info__ci-container'})
    ctnr_in1=sup.findAll('section',{'class':re.compile('^pv-contact-info__contact-type ci-')})
    s=""
    for q in ctnr_in1:
            info= q.text.replace('\n', '').strip()
            s=s+info+" ::: "
            
    browser.close()
    browser.switch_to.window(browser.window_handles[0])
    count=count+1
    print ("done "+ str(count))
    write=str(sr)+"%"+str(name)+"%"+full+"%"+str(other)+"%"+s+"\n"
    f.write(write)
    
f.close()


with open('C:/Users/yp229/OneDrive/Desktop/linkedin.txt', 'r',encoding="utf-8") as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split("%") for line in stripped if line)
    with open('C:/Users/yp229/OneDrive/Desktop/linkedin.csv', 'w',encoding="utf-8",newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('Sr', 'Name','link','overview','info'))
        writer.writerows(lines)






