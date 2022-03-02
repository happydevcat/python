# PythonLibrary.py

# import sys


# import pickle
# f = open("D:/_StudyArea/python/nMakeFile.txt","wb")
# data = {1:'Python', 2:"JAVA", 3:"C#"}
# pickle.dump(data,f)
# f.close()

# f = open("D:/_StudyArea/python/nMakeFile.txt","rb")
# data = pickle.load(f)
# print(data)

import time
import threading

def long_task():
    for iLoop in range(2):
        time.sleep(1)
        print("Working : %s\n" % iLoop)

print(f"{'START':=^80}")
threads = []

for tLooop in range(100):
    t = threading.Thread(target=long_task)
    threads.append(t)

for sLoop in threads :
    print("▶ START Thread Nm : %s" % sLoop)
    sLoop.start()

for eLoop in threads:
    eLoop.join()
    print("▷ END Thread Nm : %s" % eLoop)


print(f"{'END':=^80}")
    