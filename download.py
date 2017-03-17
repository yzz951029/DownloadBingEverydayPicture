#coding: utf-8
from time import sleep
import re
import urllib.request as request
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import os
import datetime

def download():
	print("Downloading...")
	bing_url = r"http://cn.bing.com/"
	tURL = r"https://simple.wikipedia.org/wiki/HTML"
	driver = webdriver.PhantomJS()
	driver.get(bing_url)
	sleep(5)
	#temp = driver.find_elements_by_id("bgDiv")
	#print(type(temp))
	#print(temp[0])
	#print(type(driver.page_source))
	soup = bs(driver.page_source,"html.parser")
	#html = driver.page_source.encode('utf-8','ignore')
	#file = open(r"C:\Users\user\Desktop\ForFun\save.html","wb")
	#file.write(html)
	#file.close()
	list = soup.find_all(name='div',id='bgDiv')
	bgDiv = str(list[0])
	#all_the_text = open(r"C:\Users\user\Desktop\ForFun\save.html").read()
	#print(bgDiv)
	pattern = "http://.+\.jpg"
	url = re.search(pattern,bgDiv).group(0)
	#print(pos)
	name = "BingWallpaper-"+datetime.date.today().strftime('%Y-%m-%d')+'.jpg'
	pic  = request.urlopen(url)
	file = open(r"C:\Users\user\Pictures\桌面\\"+name,'wb')
	file.write(pic.read())
	file.close()
	#print(name)
	#list = re.match(pattern,all_the_text)
	#print(list)
	#print(url)
	driver.close()
	print("Successful Download!")
	os.system("Pause")
	

if __name__=="__main__":
		download()