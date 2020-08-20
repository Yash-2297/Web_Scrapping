# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 15:32:37 2020

@author: yp229
""" 

from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
import csv
import re
import logging

logging.basicConfig(filename='culthrub.log',level=logging.DEBUG)

browser = webdriver.Chrome(r'C:\Users\yp229\.spyder-py3\chromedriver.exe') #replace with .Firefox(), or with the browser of your choice

d=browser
link="https://clutch.co/web-developers"

# browser.get(link)

def linkedin_login():
    
    userid = 'linkedin.meka@gmail.com'
    password ='Y@sh.2297'
    browser.get('https://www.linkedin.com/login')
    browser.find_element_by_xpath("""//*[@id="username"]""").send_keys(userid)
    browser.find_element_by_xpath("""//*[@id="password"]""").send_keys(password)
    browser.find_element_by_xpath("""//*[@id="app__container"]/main/div/form/div[3]/button""").click()
    browser.get("https://www.linkedin.com/search/results/companies/")
    time.sleep(5)
    
def linkedin_search(value):
    browser.switch_to.window(browser.window_handles[0])
    browser.find_element_by_xpath("""/html/body/div[7]/header/div[2]/div/div/div[1]/div/input""").clear()
    
    time.sleep(3)
    browser.find_element_by_xpath("""/html/body/div[7]/header/div[2]/div/div/div[1]/div/input""").send_keys(value)
    browser.find_element_by_xpath("""/html/body/div[7]/header/div[2]/div/div/div[2]/button""").click()
    time.sleep(3)                  
    innerHTML = browser.execute_script("return document.body.innerHTML")
    user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'    
    soup=bs(innerHTML,"html.parser")
    container=soup.find_all('div',{'class':'entity-result__item'})
    try:
        linkedin_link = str(container[0].find('a')['href'])
        # browser.get(linkedin_link)
        # time.sleep(3)
        # try:
        #     linkedin_country = browser.find_element_by_xpath("""/html/body/div[7]/div[3]/div/div[3]/div[1]/section/div/div/div[2]/div[1]/div[1]/div/div[2]/div/div/div[2]/div[1]""").text
        # except:
        #     linkedin_country = "NA"
    except:
        linkedin_link = "NA"
    print ('linkedin = ' + str(linkedin_link)+"\n")
    # write = str(linkedin_link)+"|"+str(linkedin_country)
    write =  str(linkedin_link)
    
    return write
       
    

user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'    

file="F:/Jay bhai/clutch_txt.txt"
file_csv="F:/Jay bhai/clutch_csv.csv"
f=open(file,"w",encoding="utf-8")

browser.get(link)
browser.find_element_by_xpath("""/html/body/section/div[2]/section/div/section/div/div/div/div/div[2]/form/div/div[2]/div/a""").click()
time.sleep(5)
browser.find_element_by_xpath("""/html/body/section/div[2]/section/div/section/div/div/div/div/div[2]/form/div/div[3]/div/div/div/div[6]/button""").click()
time.sleep(5)
browser.find_element_by_xpath("""/html/body/section/div[2]/section/div/section/div/div/div/div/div[2]/form/div/div[3]/div/div/div/div[6]/div/div/div/div/div/div""").click()

innerHTML = browser.execute_script("return document.body.innerHTML")
soup=bs(innerHTML,"html.parser")
location=soup.find_all('select',{'class':'form-control chosen-select-deselect form-select ajax-processed clutch-chosen-processed'})
c=location[0].find_all('option')
country = []

# linkedin_login()

time.sleep(1)

for i in range(1,len(c)):
    country.append(c[i]['value'])
   
"""
# find country index for testing:
# refer : https://www.iban.com/country-codes FOR COUNTRY CODE USING NAME
for i in range(0,len(country)):
    if country[i] == "DK":
        print (i)
"""
#going inside one country    
for i in  range(0,len(country)):
    loc_link = "https://clutch.co/web-developers?page=0&sort_by=&min_project_size=&avg_hrly_rate=&employees=&client_focus=&industry_focus=&location%5Bcountry%5D="+str(country[i])+"&op=Apply&form_id=spm_exposed_form&form_token=X3qF80w6sO85xpCKEkcFlAFQOyURK57er2pZKt3pQYw&form_build_id=form-gf8vtXsIgCuoFLesFAfn3jzU79eKzkwnQ5pEN15FkLk"
    browser.execute_script('''window.open('',"_blank");''')
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[-1])
    w_cnt = str(country[i])
    print('i value in I->' ,i)
    try:
        browser.get(loc_link)
    except:
        logging.debug("location link k first bad")
        pass

    time.sleep(2)
    
    try:
       last = browser.find_element_by_link_text("last").get_attribute('href') 
       l = (re.search('page=(.*)&sort', last)).group(1)
       page_range = int(l)
       
    except:
        page_range = 0
    time.sleep(60)    
    #going inside each page of one country
    for j in range(0,page_range+1):
        p = 'page='+str(j)
        print('i value in J->' ,i)
        page_link = re.sub(r'page=0',p,loc_link)
        try:
           browser.get(page_link)
        except:
            logging.debug("3 Excep inside page")

        time.sleep(2)
        innerHTML = browser.execute_script("return document.body.innerHTML")
        pg=bs(innerHTML,"html.parser")
        names = pg.find_all('h3',{'class':'company-name'})
        website = pg.find_all('li',{'class':'website-link website-link-a'})
        
        #going inside each tab to find name and link for one page for one country
        for k in range(0,len(names)):
            comp = str(names[k].text.strip())
            print(comp + "  ")
            print('i value in K->' ,i)
            # try:
            #     link_write = linkedin_search(comp)
            # except:
            #     # link_write = "Not Found" + "|"+"Not Found"
            #     link_write = "Not Found" 
                
            # browser.switch_to.window(browser.window_handles[-1])
            # write = str(country[i])+"|"+str(comp) + "|"+str(website[k].find('a')['href'])+" |" + str(link_write) + "\n"
            write = w_cnt+"|"+str(comp) + "|"+str(website[k].find('a')['href']+" ")+"\n"
            f.write(write)
            
f.close()

    
with open(file, 'r',encoding="utf8") as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split("|") for line in stripped if line)
    with open(file_csv, 'w',newline='',encoding="utf8") as out_file:
        writer = csv.writer(out_file)
        # writer.writerow(('Country',' Name' ,'Website','LinkedIn','LinkedIn_Country'))
        writer.writerow(('Country',' Name' ,'Website'))
        writer.writerows(lines)
    

#file="C:/Users/yp229/OneDrive/Desktop/startup_accelarator.txt"
#file_csv="C:/Users/yp229/OneDrive/Desktop/startup_accelarator.csv"
#f=open(file,"w",encoding="utf-8")
