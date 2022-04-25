import requests
import re
from bs4 import BeautifulSoup


uInforHeader = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}

for year in range(2015,2022):
    url="https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)

    res = requests.get(url,headers=uInforHeader)
    res.raise_for_status()

    soup = BeautifulSoup(res.text,"lxml") #Elements 요소로 변환 

    images = soup.find_all("img", attrs={"class":"thumb_img"})

    for idx, image in enumerate(images):
        #print(idx, image["src"] )    
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "https:"+image_url

        print(idx, image_url)
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        with open("_DnDaum_{}Movie_{}.jpg".format(year,idx), "wb") as f:
            f.write(image_res.content)

        if idx >=4 :
            break;