# WEB Scraping 
  - XPath 개념 정리
    HTML-elements (구조 형식)통한 특정경로
                               /학교/학년/반/학생[2]
                               //*[@학번="1-1-5"] unique* 
                               
                               * naver Login Button 화면
                               //*[@id="account"]/a 
                               /html/body/div[2]/div[3]/div[3]/div/div[2]/a

  - Request [pip install requests]

# 정규식 reguarExpress Python 형식 
    -m.group() : 일치하는 문자열 반환
    -m.string : 입력받은 문자열
    -m.start() : 일치하는 문자령의 시작 index
    -m.end() : 일치하는 문자령의 종료 index
    -m.span() : 일치하는 문자령의 시작 / 끝 Index 

# User Agent
- 현재 User Agent 접속 정보를 알고 싶다면. : https://www.whatismybrowser.com/detect/what-is-my-user-agent/ 
- (Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36)

# BeautifulSoup4 (네이버웹툰)
- pip install beautifulsoup4
- pip install lxml


# Selenium 설치
- pip install selenium
- chrome Driver 설치
- pip install webdriver-manager(webdriver-manager 패키지 설치)
- pip install pyperclip (Naver 자동 로그인 감지기 우회하기 )

- https://selenium-python.readthedocs.io/
