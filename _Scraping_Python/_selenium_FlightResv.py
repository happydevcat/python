
from time import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyperclip

#로딩정보를 확인해주세요. 

base_url= "https://flight.naver.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(("lang=ko_KR"))
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

srv = Service("D:\\_StudyArea\\python\\chromedriver.exe")

browser = webdriver.Chrome(service=srv, options=chrome_options)
browser.maximize_window() # 창 최대화
browser.get(base_url)



