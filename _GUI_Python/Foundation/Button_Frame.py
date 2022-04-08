from tkinter import *
import os 

root = Tk()
root.title("고양이 발 버튼")
root.geometry("600x450+1100+200")

btn1 = Button(root, text="버튼1")
btn1.pack()
# padx, pady 글자의 여백 - 가변적 크기
btn2 = Button(root, padx=5, pady=10, text="버튼2222222222222222")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

# width,height 고정된 크기를 설정
btn4 = Button(root, width=10, height=5, text="버튼43333333333333333333333333333333")
btn4.pack()

btn5 = Button(root , fg='red', bg='yellow', text='버튼5')
btn5.pack()

photo = PhotoImage(file="_GUI_Python\Foundation\img.png")
# photo = PhotoImage(file="D:/_StudyArea/python/_GUI_Python/Foundation/img_Check.png")
btn6 = Button(root,image=photo)
btn6.pack()


def btncmd():
    print("버튼7 Click Event 발생 ")

btn7 = Button(root, text="Event" , command=btncmd)
btn7.pack()


print("현재 경로 : " + os.getcwd())

root.mainloop()