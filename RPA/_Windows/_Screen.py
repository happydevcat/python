import pyautogui

# 스크린 샷 찍기
#img = pyautogui.screenshot()
#img.save("screendshot.png")

#pyautogui.mouseInfo()
#19,10 49,131,186 #3183BA
# pixel = pyautogui.pixel(19,10) # RGB 값을 갖고와요
# print(pixel)
# print(pyautogui.pixelMatchesColor(19,10,(49,131,186)))
# print(pyautogui.pixelMatchesColor(19,10,pixel))


# 이미지 recognition 
# pyautogui.sleep(3)
# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)


# trash_icon = pyautogui.locateCenterOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# 속도 개선
# 1. GrayScale : 흑백으로 처리 
# trash_icon = pyautogui.locateCenterOnScreen("trash_icon.png", grayscale=True)
# pyautogui.moveTo(trash_icon)
# 2.범위 지정
# 2076,27 1,14,26 #010E1A
# trash_icon = pyautogui.locateCenterOnScreen("trash_icon.png", region=(2076,27,240,100))
# pyautogui.moveTo(trash_icon)

# 3. 정확도 조정. OpenCV  이미지 정확도 적용. 
pyautogui.sleep(2)
# run_icon = pyautogui.locateCenterOnScreen("run.png", confidence=0.9) #90%
# pyautogui.moveTo(run_icon)


#  다음 자동화 대상이 바로 보여지지 않는 경우. Delay ... Next 
# notepad_file_icon = pyautogui.locateCenterOnScreen("notepad_file_menu.png") 
# if notepad_file_icon:
#     pyautogui.click(notepad_file_icon)
# else :
#     print("발견실패") 

# while notepad_file_icon is None : 
#     notepad_file_icon = pyautogui.locateCenterOnScreen("notepad_file_menu.png") 
#     print("뭐야 없잖아.~~")


#일정시간 동안 기다릴꼐. 

currWon = 120000

print("▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶ : ",500000000/currWon)
# 시간내 5초정도에 5억이상. 

import time
import sys
timeout = 10
frTime = time.time()
print("==== START : ", frTime)

notepad_file_icon = None

while notepad_file_icon is None:
    notepad_file_icon = pyautogui.locateOnScreen("notepad_file_menu.png")
    toTime = time.time() 
    if toTime-frTime > timeout  :
        print("종료") 
        sys.exit()
    else :
        print(">>>>   : ",toTime-frTime)

pyautogui.click(notepad_file_icon)












