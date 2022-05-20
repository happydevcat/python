import pyautogui
import time

# fw = pyautogui.getActiveWindow() # 활성화 된 창 
# print(fw.title) # 창의 제목 정보. 
# print(fw.size) # 창의 크리 정보 (Width,height)
# print(fw.left, fw.top,fw.right,fw.bottom) # 창의 좌표 정보. 
# time.sleep(3)
# pyautogui.click(fw.left+60, fw.top+20)


# 모든 윈도우 가지고 오기
# for w in pyautogui.getAllWindows() :
#     print(w.title)


w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w.title)
if w.isActive == False: # 활성화 여부
    w.activate() 
# for openWin in w :
#     print(openWin.title)


if w.isMaximized ==False: # 최대화 여부
    w.maximize()

time.sleep(3)
w.restore() # 화면 Size 

w.close() # 윈도우즈 닫기