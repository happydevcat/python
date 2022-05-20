import pyautogui
import time

#pyautogui.PAUSE = 3 # sleep(1) 모든 도작에 Dlay를 걸어둡니다.
time.sleep(5)
size = pyautogui.size()
# print(size, "Windows == Auto pyautoGUI")
print("WIDTH" , size[0])
print("HEIGHT" , size[1])

# 원하는 좌표 알아내기
#pyautogui.sleep(3)
# print(pyautogui.position())
#x:57, y:13
#pyautogui.click(57,13, duration=1)
# click == mouseDown() + mouseUp() 드레그 드랍경우. 
#click(clicks=2) = doubleClick()
#pyautogui.click(clicks=300)

# #그림판에 사선을 잇는 예제 입니다. 
# pyautogui.moveTo(300,300)
# pyautogui.mouseDown()
# pyautogui.moveTo(400,400)
# pyautogui.mouseUp()

#pyautogui.rightClick()
#pyautogui.middleClick() # 마우스 볼 클릭


#print(pyautogui.position())
#x:726, y:83
# pyautogui.moveTo(700,400)
# pyautogui.drag(200,0, duration=3) # 현재 좌표 (상대좌표) 으로 이동 설정


# 스크롤 
#pyautogui.scroll(-300) # 양수이면 위, 음수이면 아래 방향으로

# Mouse moveTo(100,100) - 지정한 위치한 마우스로 이동.[절대좌표] 
# pyautogui.moveTo(300,600, duration=5) # 0.25 초 동안 이동 

# pyautogui.moveTo(300,600, duration=1) 
# pyautogui.moveTo(300,300, duration=1) 
# pyautogui.moveTo(300,100, duration=1) 

# # 상대좌표로 마우스 이동 (현재 커서가 기준이됩니다.)
# pyautogui.moveTo(300,300, duration=1)
# pyautogui.move(300,300, duration=1)
# pyautogui.move(300,300, duration=1)

# # 현재 마우스의 좌표 표시 
# p =pyautogui.position()
# print("X", p.x)
# print("Y", p.y)


# pyautogui.position() 정보 
# pyautogui.mouseInfo()

pyautogui.moveTo(700,400)
distance = 200

while distance > 0 :
    pyautogui.drag(distance, 0 ,duration=0.5) #right
    distance -= 5
    pyautogui.drag(0, distance, duration=0.5) #down
    pyautogui.drag(-distance, 0, duration=0.5) #left
    distance -= 5
    pyautogui.drag(0, -distance, duration=0.5) #up
    






