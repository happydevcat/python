import os
import pyautogui
import time
import datetime
import fnmatch


# print(os.getcwd()) # current Working Directory 현재 작업공간
# os.chdir("_HelloPython")
# print("1 : ", os.getcwd()) # current Working Directory 현재 작업공간
# os.chdir("..")  #부모 폴더 이동
# print("2 : ", os.getcwd()) # current Working Directory 현재 작업공간


# 파일 경로 
# 1. 절대경로 폴더 정보 가지고 오기
# file_path = os.path.join(os.getcwd(), "CreateMyFile.txt")
# print(file_path)

# 파일 경로에서 폴더 정보 가지고 오기. 
# print(os.path.dirname(r"D:\_StudyArea\python\copyData.txt"))

file_path=os.path.join(os.getcwd(), "RPA/_Windows/_FileSys.py") 

#파일 정보 가지고 오기 - 파일 생성날짜
ctime=os.path.getctime(file_path)
print(ctime)
print(datetime.datetime.fromtimestamp(ctime).strftime("%Y/%m/%d %H:%M:%S"))

#파일 정보 가지고 오기 - 파일 수정날짜
mtime = os.path.getmtime(file_path)
print(datetime.datetime.fromtimestamp(mtime).strftime("%Y/%m/%d %H:%M:%S"))

#파일 정보 가지고 오기 - 파일 마지막 접근 날짜
atime = os.path.getmtime(file_path)
print(datetime.datetime.fromtimestamp(atime).strftime("%Y/%m/%d %H:%M:%S"))

# 파일 크기 
# size = os.path.getsize(file_path)
# print(size) # 바이트 단위로 갖고 오기. 

# 파일 목록 가지고 오기. 자신
# print(os.listdir("RPA"))

# 파일 목록 가지고 하위 폴더 모두 
# result = os.walk("RPA") # . 현재 작업공간

# for root, dirs, files in result:
#     print(root, dirs, files)
#     print()


# 특정파일을 찾는 경우 
# fileName = "_FileSys.py"
# result = []

# for root, dirs, files in os.walk("."):
#     if fileName in files :
#         result.append(os.path.join(root,fileName))

# print(result)


# 확장자 / 파일 이름 찾기 
# pattern = "file*.png"
# result = []


# for root, dirs, files in os.walk("."):
#     for name in files:
#         if fnmatch.fnmatch(name,pattern) : #이름과 패턴이 일치한다면. 
#             result.append(name)
#             print(name)


# 주어진 경로가 파일 인가 폴더인가?

# print(os.path.isdir("RPA"))
# print(os.path.isfile("RPA"))

# print(os.path.isdir("copyData.txt"))
# print(os.path.isfile("copyData.txt"))

# 지정된 경로가 파일/ 파일이 없을 경우 > False 처리. 

# if os.path.exists("RPA"):
#     print("======= 존재=========")
# else :     
#     print("======= 존재하지 않네요=========")

# 파일 만들기. 
# open("NEW_Create.txt", "a").close()

# 파일명 변경. 
# os.rename("NEW_Create.txt","_New_Create.txt")

# 파일 삭제
# os.remove("_New_Create.txt")

import shutil # shell utilities 
# shutil.rmtree("_RPA") #폴더 안이 비어 있지 않아도 모두 삭제 위험. ㅎㅎ

# 파일 복사. 
# shutil.copy("run.png","_TEST_FOLDER")
# shutil.copy("run.png","_TEST_FOLDER/Copy_run.png") # 새로운 이름으로 복사 
# shutil.copyfile("run.png","_TEST_FOLDER/Copy_run2.png") 
# shutil.copy2("run.png","_TEST_FOLDER/Copy2_run.png") # copy2 : 메타정보를 복사 O [있는 그대로 Create/Modify]

# 폴더 복사. 
# shutil.copytree("_TEST_FOLDER", "_TEST_FOLDER2")

# 폴더 이동

# shutil.move("_TEST_FOLDER", "_TEST_FOLDER2") # _TEST_FOLDER > _TEST_FOLDER2 로이동. 
# shutil.move("_TEST_FOLDER2", "_TEST_FOLDER") # 폴더명 변경되는 효과 (폴더명이 존재하지 않는 다면 폴더명을 변경처리 하네요)



















