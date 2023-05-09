# pip install selenium
# download chrome driver

import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


from selenium.webdriver.common.keys import Keys

def mysearch() :

	driver = webdriver.Chrome('chromedriver_110.exe')
	driver.get("https://www.google.com/finance/quote/KOSPI:KRX")

	htmlstr = driver.page_source

	soup = BeautifulSoup(htmlstr, features="html.parser") #selenium을 통해 긁어온 정보를 파싱하기

	div_list = soup.select("#yDmH0d > c-wiz > div > div.e1AOyf > div > main > div.VfPpkd-WsjYwc.VfPpkd-WsjYwc-OWXEXe-INsAgc.KC1dQ.Usd1Ac.AaN0Dd.QZMA8b > c-wiz > div > div:nth-child(1) > div > div.rPF6Lc")
	print('sadjlfjadsklfjklsd')
	print(div_list)
	return div_list


mysearch()