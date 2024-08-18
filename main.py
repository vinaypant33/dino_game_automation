from selenium import webdriver
import keyboard
import pyautogui
import time

from selenium.webdriver.chrome.service import Service



def main_manager():
    global chrome_driver
   
    options = webdriver.ChromeOptions()
    # keyboard.press_and_release('ctrl+w')
    options.add_experimental_option('detach' , True)
    
    chrome_driver = webdriver.Chrome(options = options)
    chrome_driver.maximize_window()
    # chrome_driver.get(url='chrome://dino/')
    
    
def play_game():
    global chrome_driver
    # chrome_driver.get(url='chrome://dino/')
    
    keyboard.press_and_release('ctrl+l')
    # keyboard.send('chrome://dino/')
    pyautogui.write('chrome://dino/')
    keyboard.press_and_release('enter')
    # keyboard.press_and_release('space')
    time.sleep(1)
    keyboard.press('space')
    # keyboard.press_and_release('chrome://dino/')
    # pyautogui.displayMousePosition()    
    
    while True:
        im = pyautogui.screenshot()    
        # screen = im.getpixel((214 , 189))
        x1 = im.getpixel((373 , 678))
        x2 = im.getpixel((435 , 678))
        x3 = im.getpixel((437 , 707))
        x4 = im.getpixel((441 , 651))
        x5 = im.getpixel((445 , 550))
        x6 = im.getpixel((446 , 530))
        x7 = im.getpixel((446 , 504))
    
        
        # print(x1[0] , x1)
        if x1[0] != 255:
            # keyboard.press('space')
            # keyboard.release('space')
            keyboard.press_and_release('space')
        if x2[0] != 255:
            keyboard.press_and_release('space')
        if x3[0] != 255:
            keyboard.press_and_release('space')
        if x4[0] != 255:
            keyboard.press_and_release('space')
        if x5[0] != 255:
            keyboard.press_and_release('down')
        if x6[0] != 255:
            keyboard.press_and_release('down')
        if x7[0] != 255:
            keyboard.press_and_release('down')
       
                
        if keyboard.is_pressed('ctrl+q'):
            print('Game Closed')
            break
        



if __name__ =="__main__":
    main_manager()
    play_game()