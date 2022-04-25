

import requests
from bs4 import BeautifulSoup

#https://comic.naver.com/webtoon/weekday

# BeautifulSoup4 (네이버웹툰)
#- pip install beautifulsoup4
#- pip install lxml
url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)

res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml") #Elements 요소로 변환 
#print(soup.title)
#print(soup.title.get_text())
#print(soup.a.attrs) # 첫번째 a elemnets 요소를 가지고 옵니다. 
#print(soup.a["href"]) # elements의 값을 갖고와요. 

#print(soup.find("a", attrs={"class":"Nbtn_upload"}).get_text())
#rank1 = soup.find("li", attrs={"class":"rank01"})
#print(rank1.a.get_text())
#rank2 = rank1.next_sibling.next_sibling 
#rank2 = rank1.find_next_sibling("li")
#rank3 = rank2.next_sibling.next_sibling
#rank3 = rank2.find_next_sibling("li")

#print(rank2.get_text())
#print(rank3.get_text())

#rank2 = rank3.previous_sibling.previous_sibling
#print("▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶", rank2.get_text())
#print(rank1.parent)

#print(rank1.find_next_siblings("li"))

webtton  = soup.find("a", text="광마회귀-40화")
print(webtton)



#전체 목록 가지고 오기
cartoons = soup.find_all("a", attrs={"class": "title"})
for cartoons in cartoons:
    print(cartoons.get_text())