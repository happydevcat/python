import requests
import re
from bs4 import BeautifulSoup


uInforHeader = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}

for pLoop in range(1,6):
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=5&backgroundColor=".format(pLoop)

    res = requests.get(url,headers=uInforHeader)
    res.raise_for_status()


    soup = BeautifulSoup(res.text,"lxml") #Elements 요소로 변환 

    items = soup.find_all("li", attrs={"class" : re.compile("^search-product")})

    for idx, item in enumerate(items):
        # span ad-badge-text AD 제외처리 해아합니다.
        ad_badge = item.find("span", attrs={"class": "ad-badge-text"})
        if ad_badge:
            print("▶▶▶▶▶▶▶▶▶▶▶▶▶  건너자")
            continue

        name = item.find("div", attrs={"class": "name"}).get_text()
        price = item.find("strong", attrs={"class": "price-value"}).get_text()
        rate = item.find("em", attrs={"class": "rating"})
        if rate:
            rate= rate.get_text()
        else:
            rate = -1
            continue

        if float(rate) > 4.5:
            print(idx," : ", name , "(",price,") 평점: [",rate,"]" )