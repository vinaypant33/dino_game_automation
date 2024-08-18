from selenium import webdriver
import keyboard
import pyautogui
import time

from selenium.webdriver.chrome.service import Service



def main_manager():
   
    options = webdriver.ChromeOptions()
    # keyboard.press_and_release('ctrl+w')
    options.add_experimental_option('detach' , True)
    
    chrome_driver = webdriver.Chrome(options = options)
    chrome_driver.maximize_window()
    chrome_driver.get(url='chrome://dino/')
    
    
def play_game():
    pyautogui.displayMousePosition()


if __name__ =="__main__":
    main_manager()
    play_game()