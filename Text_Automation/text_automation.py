# To Implement this Code You first Need to Install pyautogui Library
#Open Terminal and Type pip install pyautogui
import pyautogui
import time
time.sleep(4)
count = 0
while count<=2:
    pyautogui.typewrite(" Automate Your Everyday Task..... "+str(count))
    pyautogui.press("enter")
    count=count+1
    