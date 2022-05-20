# 1. 그림판 실행. 
# 2. 상단의 텍스트 기능을 이용해어서 희 영역 아무 곳에다가 글자 입력. 
#       "잘했어요"
# 3. 그림판 종료. 

from http.client import PAYMENT_REQUIRED
import sys
import pyautogui
import time
import pyperclip

def fnDrawing() :
    pyautogui.moveTo(700,400)
    distance = 200

    while distance > 0 :
        pyautogui.drag(distance, 0 ,duration=0.5) #right
        distance -= 5
        pyautogui.drag(0, distance, duration=0.5) #down
        pyautogui.drag(-distance, 0, duration=0.5) #left
        distance -= 5
        pyautogui.drag(0, -distance, duration=0.5) #up


pyautogui.hotkey("win","r")
pyautogui.write("mspaint")
pyautogui.press("enter")

pyautogui.sleep(2)

window = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0] 
if window.isMaximized == False:
    window.maximize()

pyautogui.sleep(2)
fnDrawing()
pyautogui.sleep(2)

# 글자버튼 클릭
btn_text = pyautogui.locateOnScreen("open_Text.png")
if btn_text : 
    pyautogui.click(btn_text, duration=0.2)
    pyautogui.click(200,200, duration=0.3)

    pyperclip.copy("이 멍충이........")
    pyautogui.hotkey("ctrl","v")

    

else : 
    print("====== 찾기 실패")    
    sys.exit()

# 5초 대기. 
pyautogui.sleep(5)    
window.close()
pyautogui.sleep(1)
pyautogui.press("n") # 단축키
