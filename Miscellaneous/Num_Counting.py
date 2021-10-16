# Simple script to cheat counting bot on discord xD

import pyautogui
import time


def counter(num, end):
    time.sleep(5)
    for i in range(num, end):
        pyautogui.typewrite(str(i))
        pyautogui.press("enter")
        pyautogui.hotkey("alt", "tab")
        i += 1
        time.sleep(1)


if __name__ == "__main__":
    num = int(input("Enter current number: ")) + 1
    end = int(input("Enter final number: "))
    counter(num, end)
    print("Done!")
