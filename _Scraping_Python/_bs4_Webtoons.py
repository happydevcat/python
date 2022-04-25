

import requests
from bs4 import BeautifulSoup

#https://comic.naver.com/webtoon/weekday

# BeautifulSoup4 (네이버웹툰)
#- pip install beautifulsoup4
#- pip install lxml
url = "https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml") #Elements 요소로 변환 

# 제목과 링크 가지고 오기
#cartoons = soup.find_all("td", attrs={"class": "title"})
#for webtoon in cartoons:
#    title = webtoon.a.get_text()
#    link = "https://comic.naver.com"+webtoon.a["href"]
#    print("▶  ", title, " :  ", link)



# 평점 가지고 오기
total_rates = 0
cartoons = soup.find_all("div", attrs={"class": "rating_type"})
for webtoon in cartoons:
    rate=webtoon.find("strong").get_text()
    total_rates += float(rate)


print("전체 점수 : ", total_rates)    
print("평균 점수 : ", total_rates/ len(cartoons))











