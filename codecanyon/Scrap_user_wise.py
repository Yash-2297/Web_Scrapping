# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 23:02:21 2019

@author: yp229
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen,Request
import numpy as np

f=open("C:/Users/yp229/OneDrive/Desktop/vivi.csv","w",encoding="utf-8")
header="create_Date,last_update,Price,sales,app_name,Created_by\n"
f.write(header)

for i in range (1,10):    
    url=  'https://codecanyon.net/user/viaviwebtech/portfolio?page='+str(i)
    user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'
    client = urlopen(Request(str(url), data=None, headers={'User-Agent': user_agent}))
    
    #client=req(url)
    html=client.read()
    client.close()
    soup=bs(html,"html.parser")
    #print(soup)
    #print(soup.prettify())
    
    container=soup.findAll("li",{"class":"js-google-analytics__list-event-container"})
    print(i)    
    if container:
        for ct in container:
                        
            app_name=ct.h3.text.strip()            
            created_by=ct.find("div",{"class":"product-list__info-author"}).text.strip()
            
            #result= ct.find("span",{"class":"_3B04h"})
            #if result:
               # Software=result.text.strip()
                
            sales=ct.find("div",{"class":"product-list__info-sale"}).text.strip()
            
            price=ct.find("div",{"class":"product-list__price"}).text.strip()
            
            tmp= ct.a['href']
            link="https://codecanyon.net"+tmp
            
            co = urlopen(Request(str(link), data=None, headers={'User-Agent': user_agent})).read()
            sup=bs(co,"html.parser")
            
            ctr=sup.findAll("time",{"class":"updated"})
            
            last_update=ctr[0].text.strip()
                 
            ctr=sup.findAll("td",{"class":"meta-attributes__attr-detail"})
            create_date=ctr[1].span.text.strip()

            empty=""   
            k= create_date+","+last_update+ "," + price + "," + sales +","+app_name+","+ created_by+ "\n"
            f.write(k)  
    else:
        break

f.close()
