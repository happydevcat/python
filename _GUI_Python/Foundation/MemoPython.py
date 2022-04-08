

# Python으로 메모장 Program 
# 1. title : 고양이 메모장
# 2. 메뉴 : 파일, 편집,서식, 보기, 도움말
# 3. 메뉴 - 파일 :  열기, 저장, 끝내기
#     3-1 열기: pytonMemo.txt 열기
#     3-2 저장: pytonMemo.txt 저장
#     3-2 끝내기 : root.quit
# 4. 본문 우측에 사하 스클로 바 넣기
from tkinter import *

import os
import tkinter
import tkinter.font

root = Tk()
root.title("고양이 메모장")
root.geometry("600x450+1100+200")

ctrFile = "pytonMemo.txt"

# ][Menu Part] ========================================================================
def fnOpenFile():
    print("현재 경로 : " + os.getcwd())
    if os.path.isfile(ctrFile): # 파일 존재 여부 
        with open(ctrFile, "r", encoding="utf8") as file:
            txt.delete("1.0",END)
            txt.insert(END,file.read())


def fnSaveFile():
    with open(ctrFile, "w", encoding="utf8") as file:
        file.write(txt.get("1.0",END)) 



menu = Menu(root)
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=fnOpenFile)
menu_file.add_command(label="저장", command=fnSaveFile)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)

menu.add_cascade(label="파일", menu=menu_file)
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

root.config(menu=menu)

# ][Scroll][ ========================================================================
scrollbar =  Scrollbar(root)
scrollbar.pack(side="right", fill="y")


# ][Memo TextArea] ========================================================================
font=tkinter.font.Font(family="맑은 고딕", size=11)

txt = Text(root, yscrollcommand=scrollbar.set, font=font)
txt.pack(side="left", fill="both", expand=True)
scrollbar.config(command=txt.yview) # txex의 Compenent 기준으로 설정
txt.pack()






root.resizable(True,True)

root.mainloop()