# PythonException

try:
    a = [1,2,3]
    4/0
    print(a[4])
    
except (ZeroDivisionError, IndexError) as e :
    print("Excepton 발생 : %s" % e)    

 

# # try else 절 사용하기  
# try : 
#     age = int(input('나이를 입력해봐 : '))
# except:
#     print('입력이 정확하지 않잖아 다시 입력해봐 : ')
# else : 
#     if age <= 18:
#         print('미성년자 입니다. ')
#     else:
#         print('환영합니다. ')

# Exception pass
try:
    #f = open("너는 누구냐","r")
    raise NotImplementedError
except FileNotFoundError:
    print('Exception 발생 했는데.. 그냥 pass할거야 ~')
    pass
except NotImplementedError:
    print('강제 Exception 발생')
else :
    print('pass이후 구문이 실행 되는지 확인해봅시다.')

# 예외 만들기.파이선 내장 클래서 Exception 
class MyError(Exception) : 
    def __str__(self) :
        return "허용되지 않는 별명입니다."
    pass

def say_nick(nick) :
    if nick =='바보':
        raise MyError()
    print(nick)

try:
    say_nick("천사")    
    say_nick("바보2")    
except MyError as e: 
    print("%s" % e)    

