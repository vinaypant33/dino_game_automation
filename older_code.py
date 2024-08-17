import pyautogui
import time
import keyboard

import os
import glob

pyautogui.FAILSAFE = True


current_file_name = 0


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
    current_time  = 1
    
    # for i in range(100):
    #     time.sleep(current_time)
    #     if current_time <= 0:
    #         current_time==1
    #     else:
    #         current_time-=.1
        
    #     keyboard.press_and_release('space')
    
    # print(pyautogui.position())
    make_dir()
    save_image()


def make_dir():
    directory_name  = 'images_screenshot'
    try:    
        if os.mkdir('images_screenshot'):
            os.mkdir('images_screenshot')
        else:
            print("I am already available")
    except Exception as drive_error:
        print(drive_error)
    os.chdir(directory_name)
    print(os.getcwd())

def save_image():
    global current_file_name
    pyautogui.screenshot(str(current_file_name) + '.png')
    current_file_name=+1
    check_image()
    save_image()
    
def check_image():
    directory  = 'resource'
    print(directory)
    image_extension  = "*.png"
    image_files = []
    for ext in image_extension:
        image_files.extend(glob.glob(os.path.join(directory, ext)))
    
    for image in image_files:
        print(os.path.basename(image))
    


if __name__ == '__main__':
    check_image()
    