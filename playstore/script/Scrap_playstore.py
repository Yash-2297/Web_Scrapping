# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 13:18:54 2019

@author: yp229
"""


from bs4 import BeautifulSoup as bs
from urllib.request import urlopen,Request
from selenium import webdriver
import numpy as np
import re
import time
import csv

browser = webdriver.Chrome(r'C:\Users\yp229\.spyder-py3\chromedriver.exe') #replace with .Firefox(), or with the browser of your choice

cats=['AUTO_AND_VEHICLES','BEAUTY','BOOKS_AND_REFERENCE','BUSINESS','COMICS','COMMUNICATION','DATING','EDUCATION','ENTERTAINMENT','EVENTS','FINANCE','FOOD_AND_DRINK','HEALTH_AND_FITNESS','HOUSE_AND_HOME','LIBRARIES_AND_DEMO','LIFESTYLE','MAPS_AND_NAVIGATION','MEDICAL','MUSIC_AND_AUDIO','NEWS_AND_MEGAZINES','PARENTING','PERSONALIZATION','PHOTOGRAPHY','PRODUCTIVITY','SHOPPING','SOCIAL','SPORTS','TOOLS','TRAVEL_AND_LOCAL','VIDEO_PLAYERS','ANDROID_WEAR','WEATHER','GAME_ACTION','GAME_ADVENTURE','GAME_ARCADE','GAME_BOARD','GAME_CARD','GAME_CASINO','GAME_CASUAL','GAME_EDUCATIONAL','GAME_MUSIC','GAME_PUZZLE','GAME_RACING','GAME_ROLE_PLAYING','GAME_SIMULATION','GAME_SPORTS','GAME_STRATAGY','GAME_TRIVIA','GAME_WORD','FAMILY?age=AGE_RANGE1','FAMILY?age=AGE_RANGE2','FAMILY?age=AGE_RANGE3','FAMILY_ACTION','FAMILY_BRAINGAMES','FAMILY_CREATE','FAMILY_EDUCATION','FAMILY_MUSICVIDEO','FAMILY_PRETEND']

for i in cats:
    print(i)
    url=  'https://play.google.com/store/apps/category/'+str(i)
    browser.get(url) 
    for y in range(6):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(0.5)

    innerHTML = browser.execute_script("return document.body.innerHTML")
    
    user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'    
    
    soup=bs(innerHTML,"html.parser")
 
    container=soup.findAll('div',{'class':'Ktdaqe '})
    
    f=open("C:/Users/yp229/OneDrive/Desktop/playstore/"+str(i)+".txt","w",encoding="utf-8")

    for ct in container:
        link=ct.find('div',{'class':'g4kCYe'})
        if link:
            link=ct.find('div',{'class':'g4kCYe'}).a['href']
            browser.get(link)
            innerHTML_more= browser.execute_script("return document.body.innerHTML")
            soup_more=bs(innerHTML_more,"html.parser")
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            num=soup.findAll('div',{'class':'wXUyZd'})
            for n in num:
                print(n)
                temp=n.find('a')['href']
                inlink="https://play.google.com"+temp
                c= urlopen(Request(str(inlink), data=None, headers={'User-Agent': user_agent}))
                html=c.read()
                c.close()
                sup=bs(html,"html.parser")
                name=sup.find('h1',{'class':'AHFaub'}).text
                publisher=sup.findAll('span',{'class':'T32cc UAO9ie'})[0].text
                tmp=sup.find('div',{'class':'BHMmbe'})
                if tmp:
                    review_rate=sup.find('div',{'class':'BHMmbe'}).text
                else:
                    review_rate="NA"
                tmp=sup.find('span',{'class':'EymY4b'})
                if tmp:
                    review_total=sup.find('span',{'class':'EymY4b'}).text.strip(' total')
                else:
                    review_total="NA"
                updated_on=sup.findAll('div',{'class':'JHTxhe IQ1z0d'})[1].findAll('div',{'class':'IQ1z0d'})[0].text.strip()
                downloads=sup.findAll('div',{'class':'JHTxhe IQ1z0d'})[1].findAll('div',{'class':'IQ1z0d'})[2].text.strip()
                require_android=sup.findAll('div',{'class':'JHTxhe IQ1z0d'})[1].findAll('div',{'class':'IQ1z0d'})[4].text.strip()
                current_version=sup.findAll('div',{'class':'JHTxhe IQ1z0d'})[1].findAll('div',{'class':'IQ1z0d'})[3].text.strip()
                size=sup.findAll('div',{'class':'JHTxhe IQ1z0d'})[1].findAll('div',{'class':'IQ1z0d'})[1].text.strip()
                write=name+"|"+publisher+"|"+review_rate+"|"+review_total+"|"+updated_on+"|"+downloads+"|"+require_android+"|"+current_version+"|"+size+"\n"
                f.write(write)
        else:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            num=soup.findAll('div',{'class':'wXUyZd'})
            for n in num:
                print(n)
                temp=n.find('a')['href']
                inlink="https://play.google.com"+temp
                c= urlopen(Request(str(inlink), data=None, headers={'User-Agent': user_agent}))
                html=c.read()
                c.close()
                sup=bs(html,"html.parser")
                name=sup.find('h1',{'class':'AHFaub'}).text
                publisher=sup.findAll('span',{'class':'T32cc UAO9ie'})[0].text
                tmp=sup.find('div',{'class':'BHMmbe'})
                if tmp:
                    review_rate=sup.find('div',{'class':'BHMmbe'}).text
                else:
                    review_rate="NA"
                tmp=sup.find('span',{'class':'EymY4b'})
                if tmp:
                    review_total=sup.find('span',{'class':'EymY4b'}).text.strip(' total')
                else:
                    review_total="NA"
                updated_on=sup.findAll('div',{'class':'JHTxhe IQ1z0d'})[1].findAll('div',{'class':'IQ1z0d'})[0].text.strip()
                downloads=sup.findAll('div',{'class':'JHTxhe IQ1z0d'})[1].findAll('div',{'class':'IQ1z0d'})[2].text.strip()
                require_android=sup.findAll('div',{'class':'JHTxhe IQ1z0d'})[1].findAll('div',{'class':'IQ1z0d'})[4].text.strip()
                current_version=sup.findAll('div',{'class':'JHTxhe IQ1z0d'})[1].findAll('div',{'class':'IQ1z0d'})[3].text.strip()
                size=sup.findAll('div',{'class':'JHTxhe IQ1z0d'})[1].findAll('div',{'class':'IQ1z0d'})[1].text.strip()
                write=name+"|"+publisher+"|"+review_rate+"|"+review_total+"|"+updated_on+"|"+downloads+"|"+require_android+"|"+current_version+"|"+size+"\n"
                f.write(write)
        
    f.close()
    with open('C:/Users/yp229/OneDrive/Desktop/playstore/'+str(i)+'.txt', 'r',encoding="utf-8") as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line.split("|") for line in stripped if line)
        with open('C:/Users/yp229/OneDrive/Desktop/playstore/'+str(i)+'.csv', 'w',encoding="utf-8",newline='') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(('app_name', 'publisher','reviwe_rate','review_total','updated_on','downloads','require_android','current_version','size'))
            writer.writerows(lines)
    
