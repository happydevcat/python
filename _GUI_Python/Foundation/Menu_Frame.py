import tkinter.messagebox as msgbox
from tkinter import *
import os
from urllib import response 

root = Tk()
root.title("고양이 발 버튼")
root.geometry("600x450+1100+200")

def fnCreateFile():
    pass

menu = Menu(root)

menu_file = Menu(menu,tearoff=0)
menu_file.add_command(label="New File", command=fnCreateFile)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)

menu.add_cascade(label="File", menu=menu_file)

root.config(menu=menu)

#---Message Box ----------------------------
def fnInfo():
    msgbox.showinfo("알림", "Message Box ... Open")

def fnWarn():
    msgbox.showwarning("경고", "Message Box Warn... Open")

def fnConfirm():
   response = msgbox.askyesnocancel("확인","엄마가 좋습니까? 아빠는?, 고양이는?")
   print("선택에 따른 결과 내용 : ", response, " / Type : " , type(response))
   # true, false, None > 1,0 , 그외


Button(root, command=fnInfo, text="알림").pack()
Button(root, command=fnWarn, text="경고").pack()
Button(root, command=fnConfirm, text="Comfirm").pack()





root.mainloop()