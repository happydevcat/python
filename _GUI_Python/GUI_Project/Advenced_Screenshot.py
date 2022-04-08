
import time
import keyboard
from PIL import ImageGrab

def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    print(curr_time)
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))


def exitScreenshot():
    print("종료하자")


keyboard.add_hotkey("F9", screenshot)
keyboard.add_hotkey("esc", exitScreenshot)

print("이건 뭐냐")
