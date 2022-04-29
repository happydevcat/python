#101.0.4951.41(공식 빌드) (64비트)
#ChromeDriver 101.0.4951.15
#https://velog.io/@sangyeon217/deprecation-warning-executablepath-has-been-deprecated
#webdriver-manager 패키지 설치
#pip install webdriver-manager

from time import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

base_url= "http://naver.com"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(("lang=ko_KR"))
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

srv = Service("D:\\_StudyArea\\python\\chromedriver.exe")

browser = webdriver.Chrome(service=srv, options=chrome_options)
browser.get(base_url)
#elem = browser.find_element_by_class_name("link_login")
elem = browser.find_element(By.CLASS_NAME,"link_login")
elem.click()

#browser.back()
#browser.forward()
browser.refresh()
browser.back()

#elem = browser.find_element_by_id("query")
elem = browser.find_element(By.ID,"query")
elem.send_keys("윤석렬 개시끼")
elem.send_keys(Keys.ENTER)

#elem =browser.find_elements_by_tag_name("a")
elem =browser.find_elements(By.TAG_NAME,"a")

#print("▶▶▶▶▶", elem)

for idx, e in enumerate(elem):
    print(e.get_attribute("href"))
    if idx == 10 :
        break



#browser = webdriver.Chrome("D:\_StudyArea\python\chromedriver.exe")
#browser.get("http://naver.com")
#elem = browser.find_element_by_class_name("link_login")


