# Python Input Output 2022/02/07

from tkinter import W


def jAdd(a,b):
    return a+b

# *args Parameter에 "*" 붙이면 입력값을 전부 모아 튜프롤 만든다. 
def arrayAdd(*args):    
    result = 0
    for iLoop in args:
        result = result+iLoop

    return result


# **키워드 파라미터 kwargs "**"  딕셔너리에 저장 됩니다. 
def rstKwargs(**kwargs):
    print(kwargs)
    

# lambda는 보통 def 함수를 한줄로 간결하게 만들때 사용한다. 
fn_lambdaName = lambda a,b:a+b

print(f"{'':=^100}")
# print(jAdd(3,6))
# print(arrayAdd(1,2,3,4,5,6,7,8,9,0))
print(fn_lambdaName(8888,221))
print(rstKwargs(a=9,name='rurouni',school='dragon Hischool'))



# 명령 프롬폼트입력 Form 설정 
# _tempInputNum = input('숫자를 입력해주세요 : ')

# while True : 
#     if _tempInputNum.isdigit() :
#         print("gogog")
#         break
#     else:
#         print("▶▶▶ ][숫자형이 아닙니다.다시 입력해주세요.][ ◀◀◀ ")
#         _tempInputNum = input('숫자를 입력해주세요 : ')



# if _tempInputNum.isdigit():
#     print("숫자형")
# else : 
#     print("▶▶▶ ][숫자형이 아닙니다.다시 입력해주세요.][ ◀◀◀ ")
#     _tempInputNum = input('숫자를 입력해주세요 : ')
    





