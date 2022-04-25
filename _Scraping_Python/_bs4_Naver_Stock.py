import csv
import requests
from bs4 import BeautifulSoup

#코스피 시가총액
#https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=1


_csvFileName = "시가총액1-200.csv"
f = open(_csvFileName,"w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

_header ="N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE 토론실".split("\t")
#print(type(_header))
writer.writerow(_header)

uInforHeader = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}

for setPage in range(1,5):
    url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page={}".format(setPage)
    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■    ",url)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_Rows=soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")

#    print(data_Rows)
    for index, row in enumerate(data_Rows):
        if len(row) <= 1:
            continue

        columns = row.find_all("td")
        data = [column.get_text().strip() for column in columns]
#        print(index, data)
        writer.writerow(data)


#        if index < 9 :
#            print(index, data)
#        else : 
#            break    
