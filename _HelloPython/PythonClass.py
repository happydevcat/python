
## Python Class 
# Python의 Method의 첫번째 parameter는 관례적으로 self를 사용한다. 객체를 호출할때 호출한 객체 자신이 전달되기 때문이다. 



# result = 0 
# def add(num):
#     global result
#     result += num
#     print("IN METHOD  : %s" % result)
#     return result

# print(f"{'':=^100}")
# print(add(7))
# print(add(9))

class FourCal:

    # ][Contructor 생성자 설정 ]
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setData(self, first, second):
        # print(id(self))
        # print("▶ :   %d, %d" % (first, second))
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        print("Method ADD  F: %d, S: %d" % (self.first,self.second))
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    

        

aCalObj = FourCal(9,5)
bCalObj = FourCal(45,11)
cCalObj = FourCal(997,449)

# aCalObj.setData(9,5)
# bCalObj.setData(19,11)
# cCalObj.setData(997,449)

print(f"{'':=^100}")


class Family:
    _NicName ="웃긴사람은 되더라도 웃으은 사람은 되지 말자"


a = Family()    
b = Family()

print(a._NicName)
print(id(a._NicName))
print(id(b._NicName))

