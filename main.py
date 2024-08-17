import os
import glob
import time
import keyboard
import pyautogui

pyautogui.FAILSAFE = True

current_status = ''
sleep = 1
current_file_name  = 0



def open_chrome():
    global current_status
    keyboard.press_and_release('win')
    time.sleep(sleep)
    keyboard.write('chrome')
    time.sleep(sleep)
    keyboard.press_and_release('enter')
    time.sleep(sleep)
    keyboard.write('chrome://dino/')
    time.sleep(sleep)
    keyboard.press('enter')
    # directory_name  = 'images_screenshot'
    # try:
    #     if os.mkdir(directory_name):
    #         os.mkdir('images_screenshot')
    #     else:
    #         print('Directory already done')
    # except Exception as directory_error:
    #     print(directory_error)
    # current_status = "directory_done"
    # print(current_status)
    # main_manager()
    check_image()
    


# def screenshot():
#     global current_status
#     global current_file_name
#     # current_dir  = os.getcwd()
#     current_dir  = 'images_screenshot'
#     os.chdir(current_dir)
#     print(f'current directory is : {current_dir}')
#     pyautogui.screenshot(str(current_file_name)+ '.png')
#     current_file_name=+1
#     current_status = 'screenshot_done'
#     os.chdir("..")
#     main_manager()
    
    

def check_image():
    global current_status
    directory  = 'resource'
    # os.chdir(directory)
    print(f'current directory is : {directory}')
    image_extensions = "*.png"
    image_files  = []
    for ext in image_extensions:
        image_files.extend(glob.glob(os.path.join(directory , ext)))
    
    for image in image_files:
        keyboard.press_and_release('space')
        try:
            coordinates  = pyautogui.locateOnScreen(image=image)
            print(coordinates)
            print(os.path.basename(image))
        except Exception as error:
            print(error)
            check_image()
    # current_status = 'image_done'   
    # current_dir  =os.chdir("..")
    # print(current_dir)
    # main_manager()
    time.sleep(sleep)
    # print("done hai")
    check_image()
    
    


# def main_manager():
#     pass

# def main_manager():
#     global current_status
#     if current_status == 'chrome_done':
#         make_dir()
#     elif current_status == 'directory_done':
#         time.sleep(sleep)
#         check_image()
#     elif current_status == 'image_done':
#         time.sleep(sleep)
#         screenshot()
#     elif current_status == 'screenshot_done':
#         time.sleep(sleep)
#         check_image()
    
        


if __name__ == '__main__':
    open_chrome()