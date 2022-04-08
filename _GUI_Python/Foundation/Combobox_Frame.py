import time
import tkinter.ttk as ttk
from tkinter import *
import os 

root = Tk()
root.title("고양이 발 버튼")
root.geometry("600x450+1100+200")


# -------------- ComboBox ----------------------------------------------------
def fnCombobox():
    print(combobox.get());


values = [ str(iLoop)+"일" for iLoop in range(1,32)]
combobox = ttk.Combobox(root, height=10,values=values ,state="readonly")

#combobox.set("날짜를 선택해주세요.")
combobox.current(2) # 2번째 Index값 -- 3일
combobox.pack()

btnCombo = Button(root,text="ComboBox", command=fnCombobox)
btnCombo.pack()


# -------------- Prograssbar ----------------------------------------------------

#progressbar  = ttk.Progressbar(root, maximum=100, mode="indeterminate")
p_var2 = DoubleVar()
progressbar  = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2, mode="determinate")
#progressbar.start(10) # 10 ms 마다 움직임 (언제 끝날지 모를때)
progressbar.pack()

def fnProgressbar():
    for iLoop in range(1,101):
        time.sleep(0.01)
        p_var2.set(iLoop)
        progressbar.update()
 #   progressbar.stop()


btnProgress = Button(root,text="Progresbar Start", command=fnProgressbar)
btnProgress.pack()








root.mainloop()