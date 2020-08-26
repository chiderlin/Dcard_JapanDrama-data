from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time
import os
if os.path.exists("japandrama.csv"):
    os.remove("japandrama.csv")
    
driver = webdriver.Chrome()
driver.get("https://www.dcard.tw/f/jp_drama")
#自動滾輪爬取
s="標題, 網址連結\n"
for i in range(0,4):
    html=driver.page_source
    sp=BeautifulSoup(html,"html.parser")
    data=sp.find("div","sc-1db29sy-0 cVHtOY")
    title=data.find_all("a","tgn9uw-3 bvimNL")
    #爬標題及網址
    for i in range(len(title)):
        print(title[i].text)
        print("dcard.tw{}".format(title[i].get("href")))
        s+=title[i].text+"dcard.tw{}".format(title[i].get("href"))+"\n"
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(10)
#存csv檔   
fw=open("japandrama.csv","w",encoding="utf-8-sig")
fw.write(s)
driver.close()

