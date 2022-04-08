from tkinter import *
import os 

root = Tk()
root.title("고양이 발 버튼")
root.geometry("600x450+1100+200")

lable1 = Label(root,text="안녕하세요")
lable1.pack()

def fnLabelChange():
    lable1.config(text="불꽃 고양이 덕배에요")

btn= Button(root, text="Event발생", command=fnLabelChange)
btn.pack()

## HTML TEXTAREA 
txt = Text(root, width=30, height=5)
txt.pack()

## HTML TEXT
txt.insert(END, "입력부분이에요")
e = Entry(root,width=30)
e.pack()

def fnBtnCmd():
    print(txt.get("1.0", END)) # 1: 라인 0: Column 부터 가지고 오기  END / 마지막까지 
    print(e.get())

    txt.delete("1.0", END)
    e.delete(0,END)

btn1= Button(root, text="Input 초기화", command=fnBtnCmd)
btn1.pack()


# extended 복수 선택 가능 / single 단일 선택 , height 0 모두 
listbox = Listbox(root,selectmode="extended", height=0)
listbox.insert(0,"사과")
listbox.insert(1,"딸기")
listbox.insert(2,"바나나")
listbox.insert(END,"수박")
listbox.insert(END,"포도")

listbox.pack()


def fnListSelect():
    #삭제
    #listbox.delete(END) # END 마지막 항목 삭제 / 0 첫번째 항목
    #항목 갯수 확인
    #print("리스트에는 ",listbox.size(),"개의 항목이 존재합니다")
    #print("첫번째 항목에서 3번째 항목 확인 ",listbox.get(0,2)) #시작,종료 인덱스

    #선택 항목 확인
    print("선택항목 : ",listbox.curselection(), "Type : ",type(listbox.curselection()) ) #인덱스 값으로 반환 
    


btn2 = Button(root, text="리스트 선택", command=fnListSelect)
btn2.pack()

chkvar = IntVar()
checkbox = Checkbutton(root, text="오늘 하루 보이지 않기", variable=chkvar)
checkbox.select() # 자동 선택처리
checkbox.deselect() #자동 선택해제  
checkbox.pack()

# --------------------------------------------------------------------------------------------------------------------------
#   RADIO Button

burger_var = IntVar()
def fnRadioSelect():
    print("선택메뉴 : ", burger_var.get())

Label(root, text="메뉴를 선택해보세요").pack()

rdnBtn1 = Radiobutton(root, text="그냥 햄버거", value=1, variable=burger_var)
rdnBtn2 = Radiobutton(root, text="치즈 햄버거", value=2, variable=burger_var)
rdnBtn3 = Radiobutton(root, text="치킨 햄버거", value=3, variable=burger_var)


rdnBtn1.select()
rdnBtn1.pack()
rdnBtn2.pack()
rdnBtn3.pack()

btn3 = Button(root, text="리스트 선택", command=fnRadioSelect)
btn3.pack()



root.mainloop()