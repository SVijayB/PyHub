import pyautogui
import time
from datetime import datetime

#Have to install the Pyautogui Library
#pip3 install pyautogui

str=input('Enter the message: ')
n=int(input("Enter the count: "))
time.sleep(5)
for i in range(n):
    pyautogui.write(str)
    pyautogui.press('enter')
