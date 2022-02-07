# Python Module 

_PI = 3.141592

class Math:
    def solv(self,r):
        return _PI*(r**2)


def add(a,b):
    return a+b

def sub(a,b):
    return a-b 


# Module로 import 설정시에는 해당 내용는 실행되지 않음. 
if __name__ =="__main__":
    print(add(99,88))
    print(sub(99,88))