# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 10:05:52 2019

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


def gmail_login(index=0):
    
    userid= 'yp.2297'
    password ='Y@sh.2297'
    browser.get(url_google)
    time.sleep(5)
    browser.find_element_by_xpath("""//*[@id="identifierId"]""").send_keys(userid)
    browser.find_element_by_xpath("""//*[@id="identifierId"]""").send_keys(u'\ue007')
    time.sleep(5)
    browser.find_element_by_xpath("""//*[@id="password"]/div[1]/div/div[1]/input""").send_keys(password)
    browser.find_element_by_xpath("""//*[@id="password"]/div[1]/div/div[1]/input""").send_keys("\ue007'")
    time.sleep(5)
    return


    
op=0
browser = webdriver.Chrome(r'C:\Users\yp229\.spyder-py3\chromedriver.exe')#,options=options) #replace with .Firefox(), or with the browser of your choice
url_google=  'https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
url_olx= 'https://www.olx.in/post/attributes'
gmail_login()
time.sleep(1.5)

browser.execute_script('''window.open('',"_blank");''')
time.sleep(2)
browser.switch_to.window(browser.window_handles[-1])
browser.get(url_olx)
time.sleep(1)
browser.find_element_by_css_selector("""body > div:nth-child(12) > div > div > div > button:nth-child(3)""").click()
time.sleep(6)
browser.get(url_olx)
browser.switch_to.alert.accept()
time.sleep(6)
browser.find_element_by_xpath("""//*[@id="container"]/main/div/div/div/div/div/div/ul/li[2]""").click()
browser.find_element_by_css_selector("""#container > main > div > div > div > div > div > div > ul._2qVdv.rui-2SwH7.rui-2H_4Q.rui-ILj5I.rui-3E1c2.rui-1JF_2._29S32 > li:nth-child(1)""").click()

time.sleep(3)                            
innerHTML = browser.execute_script("return document.body.innerHTML")
soup2=bs(innerHTML,"html.parser")

time.sleep(1.4)                            
f=open("C:/Users/yp229/OneDrive/Desktop/scrapped_olx_final.txt","w",encoding="utf-8")

state=[]
ctnr=soup2.find('select',{'id':'State'})
for c in ctnr:
    state.append(c.text)
for i in range(30,len(state)):
    print(state[i])
    browser.find_element_by_css_selector("""#State""").send_keys(state[i])
    time.sleep(1)
    innerHTML = browser.execute_script("return document.body.innerHTML")
    soup=bs(innerHTML,"html.parser")
    city=[]
    contain2=soup.find('select',{'id':'City'})
    time.sleep(3)
    for c in contain2:
        city.append(c.text)
        
    for j in range(0,len(city)):
        browser.find_element_by_css_selector("""#City""").send_keys(city[j])

        try:
            print(city[j])
            time.sleep(4)
            innerHTML = browser.execute_script("return document.body.innerHTML")
            time.sleep(1)
            sup=bs(innerHTML,"html.parser")
            time.sleep(2)
            p=sup.find('select',{'id':'Locality'})
            local=[]
            time.sleep(2)
            k=type(p)
            try:
                for u in p:
                    local.append(str(u.text))
                print(local)
                locality= " * ".join(local)
                info=state[i]+'|'+city[j]+'|'+locality+'\n'
                print(info)
                f.write(info)
                op=1
            except :
                print('No Locality')
                info=state[i]+'|'+city[j]+'\n'
                print(info)
                f.write(info)
        finally:
            if op==0:
                info=state[i]+'|'+city[j]+'\n'
                print(info)
                f.write(info)
f.close()
        

with open("C:/Users/yp229/OneDrive/Desktop/scrapped_olx_final.txt", 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split("|") for line in stripped if line)
    with open("C:/Users/yp229/OneDrive/Desktop/scrapped_olx_final.csv", 'w',newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('state','city','local'))
        writer.writerows(lines)
        
