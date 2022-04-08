# pi install Pillow
import time
from PIL import ImageGrab

time.sleep(5) #  사용자가 준비하는 시간 

# 2초 간격으로 10개의 스크린 샷이 생성 되게 합니다. 
for iLoop in range(1,11):
    img = ImageGrab.grab() # 현재 스크린 이미지를 가져옴
    img.save("image_{}.png".format(iLoop))
    time.sleep(2) # 2초 쉬고
    

