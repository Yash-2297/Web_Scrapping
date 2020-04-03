# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 21:26:27 2019

@author: yp2297
"""


from bs4 import BeautifulSoup as bs
from urllib.request import urlopen,Request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import pandas as pd

def refresh():
    for y in range(180):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)
        browser.execute_script("window.scrollTo(0, 100)")
        print(y)
    return


def gmail_login(index=0):
    df= pd.read_csv(r'C:\Users\yp229\OneDrive\Desktop\id.csv')
    userid=df['id'][index]
    password =df['pass'][index]
    browser.get(url_google)
    time.sleep(1.5)
    browser.find_element_by_xpath("""//*[@id="identifierId"]""").send_keys(userid)
    browser.find_element_by_xpath("""//*[@id="identifierId"]""").send_keys(u'\ue007')
    time.sleep(1.5)
    browser.find_element_by_xpath("""//*[@id="password"]/div[1]/div/div[1]/input""").send_keys(password)
    browser.find_element_by_xpath("""//*[@id="password"]/div[1]/div/div[1]/input""").send_keys("\ue007'")
    time.sleep(5)
    return

def gmail_logout():
    browser.execute_script("""window.open('',"_blank");""")
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[-1])
    browser.get('https://mail.google.com/mail/')
    innerHTML = browser.execute_script("return document.body.innerHTML")
    soup=bs(innerHTML,"html.parser")
    link=soup.find('a',{'class':'gb_3 gb_6f gb_eg gb_Ne gb_pb'})['href']
    browser.get(link)
    time.sleep(2)
    return    

def uplab_login():
    browser.execute_script("""window.open('',"_blank");""")
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[-1])
    browser.get(url_auth)
    time.sleep(2)
    try:
        browser.find_element_by_css_selector("""#view_container > div > div > div.pwWryf.bxPAYd > div > div > div > form > span > section > div > span > div > div > ul > li.M8HEDc.ibdqA.W7Aapd.bxPAYd.SmR8.znIWoc > div""").send_keys("\ue007'")
        time.sleep(3)
        browser.find_element_by_css_selector("""#edit_user_602651 > div.narrow__form-fields > div:nth-child(3) > input""").send_keys("\ue007'")                                 
    except:
        print("not found uplab login must be authorized by now")                                         
 #          browser.switch_to.window(browser.window_handles[0])
        
    return
'''
def extension():
    #extension_try
    browser.execute_script("""window.open('',"_blank");""")
    browser.switch_to.window(browser.window_handles[-1])
    browser.get('chrome-extension://ogojkdkkcopeepagdlddbninobfhfbcb/popup.html')
    #set-on-connect    
    elem=driver.find_element_by_css_selector("body")
    driver.execute_script("arguments[0].setAttribute('class','on')", elem)
    browser.find_element_by_xpath("""//*[@id="country-select"]/div[1]""").click()
    browser.find_element_by_xpath("""//*[@id="search_country"]""").send_keys('India')
    driver.find_element_by_css_selector("""#country-select > div.x-select-dropdown > div.countries > div""").click()
    time.sleep(5)
    browser.find_element_by_css_selector("""body > div > main > div.connect_btn_holder > label""").click()
    
    browser.close()
#    browser.switch_to.window(browser.window_handles[-1])
    return
'''    
def scrap_main():
    index=0
    gmail_login(index)
    time.sleep(2)
    index+=1
    uplab_login()
    time.sleep(2)

    #uplab scrap
    browser.execute_script('''window.open('',"_blank");''')
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[-1])
    time.sleep(3)
    browser.get(url_main)
    time.sleep(2)
    refresh()
    innerHTML = browser.execute_script("return document.body.innerHTML")
    soup=bs(innerHTML,"html.parser")
    
    #free - non premium
    container_freenp=soup.findAll('div',{'class':'card__footer-price card__footer-price--free clearfix'})
    
    #driver.execute_script("arguments[0].setAttribute('class','on')", elem)
    #free- premium
    #container_freep=soup.findAll('div',{'class':'card__footer-price card__footer-price--premium clearfix'})
    #PAID
    #container_paid=soup.findAll('div',{'class':'card__footer-price card__footer-price--paid clearfix'})
    p=0
    success=0
    for c in container_freenp:
        if success<=2:
            print(p)
            each_link=c.find('a')['href'].strip()
            browser.execute_script('''window.open('',"_blank");''')
            browser.switch_to.window(browser.window_handles[-1])
            browser.get(each_link)
            try:
                time.sleep(3)
                browser.find_element_by_css_selector("""#sidebar > div.post__sidebar-cta > div > div > div:nth-child(3) > div:nth-child(1) > a""").send_keys("\ue007'") #downloadnow_1st
                time.sleep(5)
                innerHTML2 = browser.execute_script("return document.body.innerHTML")
                soup2=bs(innerHTML2,"html.parser")
                href=soup2.find('a',{'class':'btn btn--green block'})['href']
                stri="https://www.uplabs.com"+href
                browser.get(stri)
                
                time.sleep(3)
                success+=1
            except:
                success-=1
                print("no download option found in ",each_link)
            finally:
                browser.close()
                browser.switch_to.window(browser.window_handles[-1])
                p+=1
        else:
            browser.close()
            time.sleep(6)
            browser.switch_to.window(browser.window_handles[-1])
            gmail_logout()
            gmail_login(index)
            index+=1
            uplab_login()
            success=0
    
    return    

#web-driver-setup 
df= pd.read_csv(r'C:\Users\yp229\OneDrive\Desktop\id.csv')

path='C:/Users/yp229/.spyder-py3/freevpn.crx'
options = Options()
options.add_extension(path)
browser = webdriver.Chrome(r'C:\Users\yp229\.spyder-py3\chromedriver.exe')#,options=options) #replace with .Firefox(), or with the browser of your choice
time.sleep(2)


driver=browser


url_google=  'https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
url_auth="http://www.uplabs.com/auth/google/"
url_main="https://www.uplabs.com/posts/tool/photoshop"
url_plugin="chrome-extension://ogojkdkkcopeepagdlddbninobfhfbcb/popup.html"


scrap_main()
