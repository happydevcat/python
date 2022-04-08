import tkinter.ttk as ttk
from tkinter import *

import os
import tkinter
import tkinter.font

root = Tk()
root.title("고양이 그림 합치기")
root.geometry("600x450+1100+200")

# 파일 Frame(파일 추가, 선택 삭제) #################################################################
file_frame = Frame(root,padx=5, pady=5)
file_frame.pack(fill="x")

btn_add_file = Button(file_frame, text="파일 추가", padx=5, pady=5, width=10)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, text="파일 삭제", padx=5, pady=5, width=10)
btn_del_file.pack(side="right")


# 선택 파일 리스트 Frame(파일 추가, 선택 삭제) #################################################################
list_frame = Frame(root)
list_frame.pack(fill="x")

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y") 

list_file = Listbox(list_frame, selectmode="extended", height=7, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)


# 저장경로 Frame  #################################################################
path_frame = LabelFrame(root, text="저장경로", padx=5,pady=5)
path_frame.pack(fill="x")

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4)

btn_dest_path = Button(path_frame, text="찾아보기", padx=5, pady=5, width=10 )
btn_dest_path.pack(side="right")


# 옵션 프게인 #####################################################################
frame_option = LabelFrame(root,text="저장옵션", padx=5,pady=5)
frame_option.pack(fill="x")

##가로 넓이 옵션
lbl_width = Label(frame_option, text="가로넓이", width=8)
lbl_width.pack(side="left")

opt_width = ["원본유지","1024","800","640","480"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width)
cmb_width.current(0)
cmb_width.pack(side="left")

##간견 옵션
lbl_space = Label(frame_option, text="간격옵션", width=8)
lbl_space.pack(side="left")

opt_space = ["없음","좁게","보통","넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space)
cmb_space.current(0)
cmb_space.pack(side="left")

##저장 Format 옵션
lbl_format = Label(frame_option, text="간격옵션", width=8)
lbl_format.pack(side="left")

opt_format = ["PNG","JPG","BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format)
cmb_format.current(0)
cmb_format.pack(side="left")


# 진행 상호아 Progress Bar ############################################################################
frame_progress = LabelFrame(root, text="진행사항", padx=5,pady=5)
frame_progress.pack(fill="x")

p_var = DoubleVar()
progressbar= ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progressbar.pack(fill="x")

# 시작 /종료 실행 button ############################################################################

frame_run = Frame(root)
frame_run.pack(fill="x")

btn_stop = Button(frame_run, padx=5, pady=5, text="종료" ,width="10", command=root.quit)
btn_stop.pack(side="right")

btn_start = Button(frame_run, padx=5, pady=5, text="시작" ,width="10")
btn_start.pack(side="right")






root.resizable(False,False)
root.mainloop()