import requests

#res = requests.get("https://google.jp")
res = requests.get("https://nadocoding.tistory.com/")

print("Request State : ", res.status_code) #200 정상
res.raise_for_status()
print("WEB Scraping Start")


#print("Request State : ", res.status_code) #200 정상
#if res.status_code == requests.codes.ok:
#    print("정상")
#else:
#    print("문제가 생긴것 같아요 Error Code: ",res.status_code )


#상단 IF문과 같은 기능입니다. 
#print(len(res.text))
#print(res.text)
#with open("DN_google.html","w", encoding="utf8") as f:
#    f.write(res.text)