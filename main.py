import pyautogui
import time

import keyboard


pyautogui.FAILSAFE = True

def open_chrome():
    keyboard.press_and_release('win')
    time.sleep(1)
    keyboard.write('chrome')
    time.sleep(1)
    keyboard.press_and_release('enter')
    time.sleep(1)
    keyboard.write('chrome://dino/')
    time.sleep(1)
    keyboard.press_and_release('enter')
    time.sleep(1)
    keyboard.press('space')
    
    for i in range(10):
        time.sleep(1)
        keyboard.press_and_release('space')
        

  
if __name__ == '__main__':
    open_chrome()