import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog
from PIL import Image

import os
import tkinter
import tkinter.font

root = Tk()
root.title("고양이 그림 합치기")
root.geometry("600x450+1100+200")


#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

# 파일 추기
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요", filetypes=(("PNG 파일", "*.png"),("모든 파일","*")), initialdir=r"D:\_StudyArea\python\DN Images")

    for file in files:
        list_file.insert(END,file)


# 파일 삭제
def del_file():
    print(list_file.curselection())
    
    for index in reversed(list_file.curselection()):    # reversed는 기존 데이터가 변하지 않음 , reverse 는 대상 list가 변경됨
        list_file.delete(index)

# 저장경로
def browse_dest_path():
    forlder_selected=filedialog.askdirectory()
    if forlder_selected =='': #is None 아닙니다. 
        print("폴더 선택 취소")
        return
    else:
        #print(forlder_selected)
        txt_dest_path.delete(0,END)
        txt_dest_path.insert(0,forlder_selected)


# 시작 
def start():
    ## 옵션설정 확인
    # print("가로넓이 : ", cmb_width.get())
    # print("간격 : ", cmb_space.get())
    # print("포멧 : ", cmb_format.get())
    
    # 파일 목록 확인. 
    if list_file.size() ==0:
        msgbox.showwarning("경고", "이미지를 선택해주세요. ")
        return

    #저장 경로확인. 
    if len(txt_dest_path.get()) ==0:
        msgbox.showwarning("경고","저장경로를 선택하세요.")
        return

    merge_image()

# 이미지 통합
def merge_image():

    print("가로넓이 : ", cmb_width.get())
    print("간격 : ", cmb_space.get())
    print("포멧 : ", cmb_format.get())

    # 가로넓이 
    img_width = cmb_width.get()
    if img_width =="원본유지":
        img_width = -1
    else:
        img_width = int(img_width)

    # 간격
    img_space = cmb_space.get()
    if img_space =="좁게":
        img_space = 30
    elif img_space =="보통":
        img_space = 60
    elif img_space =="넓게":
        img_space = 90
    else:
        img_space = 0

    #포멧   
    img_format = cmb_format.get().lower() 



    print(list_file.get(0,END))
    images = [Image.open(x) for x in list_file.get(0,END)]
    #size > size[0] : width, size[1]: height
    #ZIP , UNZIP 
    # widths = [x.size[0] for x in images]
    # heights = [x.size[1] for x in images]
    # 이미지 사이즈를 리스트에 넣어서 하나씩 처리 
    image_sizes = []
    if img_width > -1:
        #with가 조정되면 그비율에 맞게 높이도 수정이 되어야 하잖아요. 그쵸?       
        # 100* 60 > 80으로 줄이면 높이는  y(48) =60*80/100
        image_sizes = [(int(img_width), int(x.size[1]*img_width/x.size[0])) for x in images]
    else:
        image_sizes = [(x.size[0],x.size[1]) for x in images]

    
    #widths, heights = zip(*(x.size for x in images))
    widths, heights = zip(*(image_sizes))
    
    #최대 넓이,전체 높이
    #print(widths) 가장 넓은 것을 기준으로 
    #print(heights) 높은값은 더한다
    max_width, total_height = max(widths), sum(heights)
    
    # 스케치북 만들기. 
    ## 이미지 간격 옵션
    if img_space > 0:
        total_height += (img_space * (len(images)- 1))

    result_img = Image.new("RGB",(max_width,total_height),(255,255,255))
    y_offeset=0 # y 위치

#    for img in images:
#        result_img.paste(img,(0,y_offeset))
#        y_offeset += img.size[1] #height값
    
    for idx, img in enumerate(images):
        #width 가 원본유지의 경우  이미지 크기 조정
        if img_width > -1:
            img = img.resize(image_sizes[idx])


        result_img.paste(img,(0,y_offeset))
        y_offeset += (img.size[1] + img_space) # 사용자가 지정한 간격 

        progress = (idx+1)/len(images) *100 
        print("▷▷▷▷▷▷▷▷▷▷▷ ", progress)
        p_var.set(progress)
        progressbar.update()

    # 포맷 옵력 처리 
    try:
        file_name = "happyCat."+img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name)
        result_img.save(dest_path)
        msgbox.showinfo("알림","저장이 완료되었습니다")
    except Exception as err:
        msgbox.showerror("에러",err)




#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■




# 파일 Frame(파일 추가, 선택 삭제) #################################################################
file_frame = Frame(root,padx=5, pady=5)
file_frame.pack(fill="x")

btn_add_file = Button(file_frame, text="파일 추가", padx=5, pady=5, width=10, command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, text="파일 삭제", padx=5, pady=5, width=10, command=del_file)
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

btn_dest_path = Button(path_frame, text="찾아보기", padx=5, pady=5, width=10 ,command=browse_dest_path)
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
lbl_format = Label(frame_option, text="저장옵션", width=8)
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

btn_start = Button(frame_run, padx=5, pady=5, text="시작" ,width="10", command=start)
btn_start.pack(side="right")






root.resizable(False,False)
root.mainloop()