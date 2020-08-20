
import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
import csv
import re
import logging


browser = webdriver.Chrome(r'C:\Users\yp229\.spyder-py3\chromedriver.exe') #replace with .Firefox(), or with the browser of your choice

d=browser


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

df = pd.read_csv('F:/Jay bhai/clutch_csv.csv',encoding = "ISO-8859-1")
df.columns

df=pd.DataFrame(df)

name = df[[" Name"]]

linkedin_login()
company =[]
for i in range(0,len(name)):
    company.append(name.loc[i," Name"])

f=open("C:/Users/yp229/OneDrive/Desktop/linkedin.txt","w",encoding="utf-8")
for i in range(0,len(company)):
    w = linkedin_search(company[i].strip())
    print(w + "\n")
    a=str(company[i].strip ) + "|| " + w + "\n"
    f.write(a)

f.close()