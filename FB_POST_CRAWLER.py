# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 06:44:53 2018

@author: PASTOR DAN
"""

# Write a script that crawls posts of your Facebook friends

from selenium import webdriver
import json
from selenium.webdriver.common.keys import Keys
from time import sleep

def post_scraper(email, password, timeline_url):
    chrome = webdriver.Chrome(r"C:\Users\PASTOR DAN\Documents\DAN THE GURU\PYTHONPROJECTS\chromedriver")
    chrome.get("http://facebook.com")
    chrome.find_element_by_id("email").send_keys(str(email))
    chrome.find_element_by_id("pass").send_keys(str(password))
    chrome.find_element_by_id("pass").send_keys(Keys.ENTER)
    
    # Get login cookies
#    cookie = chrome.get_cookies()
#    with open("cookies.txt", "w") as f:
#        f.write(str(cookie))

    chrome.get("https://web.facebook.com/profile.php?id="+str(timeline_url))
    # Get scroll height
    last_height = chrome.execute_script("return document.body.scrollHeight")
    po = []
    while True:
        # Scroll down to bottom
        chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load
        sleep(15)
        # Calculate new scroll height and compare with last scroll height
        new_height = chrome.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        
    p = chrome.find_elements_by_class_name("_3ccb")
    # Exracting male names
    for i in p:
        name = i.text
        data = {"post": name}
        po.append(data)
    data = {"post": po}
    data = json.dumps(data, indent=4)
    #writing to file
    with open("d.json","w") as f:
        f.write(str(data))
        
        

    
    
    
    
    
    