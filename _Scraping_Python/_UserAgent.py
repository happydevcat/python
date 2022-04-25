import requests


headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}
url = "https://nadocoding.tistory.com/"
res = requests.get(url,headers=headers)


print("Request State : ", res.status_code) #200 정상
res.raise_for_status()
print("WEB Scraping Start")



with open("DN_nadocoding.html","w", encoding="utf8") as f:
    f.write(res.text)