
from cgitb import text
from tkinter import *
import os

root = Tk()
root.title("고양이 발 버튼")
root.geometry("600x450+1100+200")

# 맨 윗줄
btn_f16 = Button(root, text="F16", padx=10,pady=10)
btn_f17 = Button(root, text="F17", padx=10,pady=10)
btn_f18 = Button(root, text="F18", padx=10,pady=10)
btn_f19 = Button(root, text="F19", padx=10,pady=10)

btn_f16.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_f17.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_f18.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_f19.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)


# Clear
btn_clear = Button(root, text="Clear", padx=10,pady=10)
btn_equal = Button(root, text="=", padx=10,pady=10)
btn_div = Button(root, text="/", padx=10,pady=10)
btn_mul = Button(root, text="+", padx=10,pady=10)

btn_clear.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_equal.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_div.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_mul.grid(row=1, column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3)

# 7 시작
btn_7 = Button(root, text="7", padx=10,pady=10)
btn_8 = Button(root, text="9", padx=10,pady=10)
#btn_9 = Button(root, text="9")
#btn_sub = Button(root, text="-")

btn_7.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_8.grid(row=2, column=1, columnspan=2, sticky=N+E+W+S, padx=3, pady=3)
#btn_9.grid(row=2, column=2)
#btn_sub.grid(row=2, column=3)

root.mainloop()