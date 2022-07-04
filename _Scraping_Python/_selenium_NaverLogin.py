
from time import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyperclip


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


## ID/Password 로그인 정보입력
naverId = "rurounix"
naverPw = "@7798ss$"

pyperclip.copy(naverId)
browser.find_element(By.ID, "id").send_keys(Keys.CONTROL, 'v')

pyperclip.copy(naverPw)
browser.find_element(By.ID, "pw").send_keys(Keys.CONTROL, 'v')
time.sleep(2)
browser.find_element(By.ID, "log.login").click()
#browser.find_element(By.ID, "id").clear()

#print(browser.page_source)

#browser.close() # tab 현재 탭종료
#browser.quit() # 전제 종료


