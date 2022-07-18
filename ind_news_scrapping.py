# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 
from nltk import wordpunct_tokenize
import nltk
# create webdriver object
driver = webdriver.Chrome(executable_path=r"C:\Users\anura\chromedriver\chromedriver.exe")
# get google.co.in
driver.get("https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRE55YXpBU0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen&v2prv=1")

e=driver.find_element(By.CLASS_NAME,"D9SJMe")
c=e.text.lower().split("\n")
c=[i for i in c if len(i)>25]
print(c)
c=[wordpunct_tokenize(i) for i in c ]
un=['to','s','in','from','for','too','all','At','at','of','on','In','as','t','the','with','and',
    'after','be','is','a','p','will','by']
print(c)
d={}
for j in c:
    for i in j:
        if i in d.keys() and i.isalnum() and i not in un:
            d[i]+=1
        else:
            d[i]=1
z=[i for i in d if d[i]>=max(d.values())-7]       
print(z)
file =open(r'C:\Users\anura\python\news.txt',"a")
for i in z:
    file.write(i+"\n")
 
"""
e.send_keys("sun")
e.send_keys(Keys.ENTER)
e=driver.find_element(By.CLASS_NAME,"hdtb-mitem")

a=ActionChains(driver)
a.click(e)
a.perform()
"""