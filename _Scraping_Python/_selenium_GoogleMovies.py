# -------------------------------------------------------------------------    
from asyncio.windows_events import NULL
import requests
from bs4 import BeautifulSoup


# base_url= "https://play.google.com/store/movies"
# uInforHeader = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36","Accept-Language" :"ko-KR,ko" }

# res= requests.get(base_url, headers=uInforHeader)
# res.raise_for_status()
# soup = BeautifulSoup(res.text , "lxml")

# movies = soup.find_all("div", attrs={"class":"ULeU3b neq64b"})

# print("▶▶▶▶▶▶▶▶▶▶▶▶▶   :  ",len(movies))




# for movie in movies :
#     objType = movie.find("div", attrs={"class":"Epkrse"})
#     if objType == None :
#         continue

#     title = objType.get_text()
#     print(title)


# with open("_google_Movies.html","w",encoding="utf-8") as f:
#     f.write(soup.prettify())
#    f.write(res.text)


# -------------------------------------------------------------------------    

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pyperclip


base_url= "https://play.google.com/store/movies"
uInforHeader = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36","Accept-Language" :"ko-KR,ko" }


chrome_options = webdriver.ChromeOptions()
chrome_options.headless = True
chrome_options.add_argument("window-siz=1920*1000")
chrome_options.add_argument(f"user-agent={uInforHeader}")

chrome_options.add_argument(("lang=ko_KR"))
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

srv = Service("D:\\_StudyArea\\python\\chromedriver.exe")

browser = webdriver.Chrome(service=srv, options=chrome_options)
#browser.maximize_window() # 창 최대화
browser.get(base_url)
time.sleep(2)
#couserPoint = browser.find_element(By.XPATH,"//*[@id='yDmH0d']/c-wiz[2]/div/div/div[1]/c-wiz/div/c-wiz/c-wiz[1]/c-wiz/section/div/div/div/div/div/div[1]/div[3]/div/div/a/div[1]")
couserPoint = browser.find_element(By.CLASS_NAME, "TjRVLb")
print("▶▶▶▶▶▶▶  :   ",couserPoint)
ActionChains(browser).move_to_element(couserPoint).perform()
time.sleep(2)

#nextButton=browser.find_element(By.CLASS_NAME, "VfPpkd-BIzmGd SaBhMc NNFoTc zI3eKe N7pe4e PcY7Ff")
#nextButton=browser.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz[4]/div/div/div[1]/c-wiz/div/c-wiz/c-wiz[1]/c-wiz/section/div/div/div/div/div/div[2]/button")
nextButtons=browser.find_elements(By.TAG_NAME,"button")

objButton = NULL
for btn in nextButtons :
    if btn.get_attribute("aria-label") =="다음으로 스크롤" :
        objButton = btn        
        break


for iLoop in range(1,4) :

    res= requests.get(base_url, headers=uInforHeader)
    res.raise_for_status()
    soup = BeautifulSoup(res.text , "lxml")

    parentDiv = soup.find_all("div", attrs={"class":"ftgkle"})[0]
    movies = parentDiv.find_all("div", attrs={"class": "ULeU3b neq64b"})
#ULeU3b neq64b
    print(iLoop, " : ▶▶▶▶▶▶▶▶▶▶▶▶▶   :  ",len(movies))
# 스크린샷
    browser.get_screenshot_as_file("_google_Movie{}.png".format(iLoop)) 
    time.sleep(2)
    objButton.click()




        

    
    

    
#print("▷▷▷▷▷▷▷ : ",nextButton)
#ActionChains(browser).click(nextButton)

#browser.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz[2]/div/div/div[1]/c-wiz/div/c-wiz/c-wiz[1]/c-wiz/section/div/div/div/div/div/div[2]/button").click()



# # button class="VfPpkd-BIzmGd SaBhMc NNFoTc zI3eKe N7pe4e PcY7Ff"
# # aria-label="이전으로 스크롤"
# # aria-label="다음으로 스크롤"










