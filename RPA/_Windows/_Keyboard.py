import pyautogui
import time 

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
time.sleep(2)
print(w)
w.activate()

# pyautogui.write("▶12345")
# pyautogui.write("코딩하자규....." , interval=1)
# 방향키 left,right, enter 
# Automate the Boring stuff with Python : Key 참조 
# pyautogui.write(["t","e","s","left","left","left","left","left","v","right","right","right","x","enter"], interval=0.2)

# 특수 문자. 
# shift 4 > $
# pyautogui.keyDown("shift")
# pyautogui.press("4")
# pyautogui.keyUp("shift")

# 조합키 Hot Key
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")
# pyautogui.keyUp("ctrl")

# 조홥키.
# pyautogui.hotkey("ctrl","a")

#한글 
import pyperclip
pyperclip.copy("와우 멋지네")
pyautogui.write(["enter","enter","enter"])
pyautogui.hotkey("ctrl","v")

