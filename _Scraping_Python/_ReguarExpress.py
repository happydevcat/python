import re

#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
def fn_GetMatch(m):
    if m:
        print("m.group() : ", m.group())  ## 일치하는 문자열 반환
        print("m.string : ", m.string) # 입력받은 문자열
        print("m.start() : ",m.start()) # 일치하는 문자령의 시작 index
        print("m.end() : ",m.end()) # 일치하는 문자령의 종료 index
        print("m.span() : ",m.span()) # 일치하는 문자령의 시작 / 끝 Index 
    else:
        print("Not Match")
# 정규식 reguarExpress Python 형식 
#. : (ca.e)하나의 문자를 의미
#^ : (^de)문자열시작 의미 >  desk, destisation 
#$ : (se$)문자열 종료 읨 > case , base
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


p= re.compile("ca.e")    


#m= p.match("careless") # match : 주어진 문자열의 처츰부터 일치하는지 확인
#fn_GetMatch(m)

#m= p.search("good cafe") # search : 주어진 문자열 중에 잋이하는게 있는지 확인 
#fn_GetMatch(m)


lst= p.findall("good care cafe")
print(lst)





