#파일 쓰고 Control

# f = open("D:/_StudyArea/python/nMakeFile.txt","w")

# for iLoop in range(1,20):
#     writeData = "%d번째 줄입니다. \n" % iLoop
#     print(writeData)
#     f.write(writeData)

# f.close()


#파일 읽고 1. 

# f = open("D:/_StudyArea/python/nMakeFile.txt","r")
# while True:
#     rline = f.readline()
#     if not rline : break
#     print(rline)

# f.close()

#파일 읽고 2. 
# f = open("D:/_StudyArea/python/nMakeFile.txt","r")
# rlines = f.readlines()
# for line in rlines:
#     line = line.strip()
#     print(line)
# f.close()


print(f"{'':=^100}")

# #파일 추가 쓰기  
# f = open("D:/_StudyArea/python/nMakeFile.txt","a")
# for iLoop in range(20,41):
#     aData ="★★★ %d번째 추가 줄입니다.\n" % iLoop
#     f.write(aData)
# f.close()

# #파일 읽고 (전체)3 . 
# f = open("D:/_StudyArea/python/nMakeFile.txt","r")
# data = f.read()
# print(data)
# f.close()

import sys
args = sys.argv[1:]
for iLoop in args:
    print(iLoop.upper(), end=' ')

    