# Python script to automate deleting Discord DM messages.
import pyautogui
import time


def AutoDelete(msgCount):
    for i in range(msgCount):
        pyautogui.press("up")
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("backspace")
        pyautogui.press("enter")
        pyautogui.press("enter")
        pyautogui.click(500, 976)
        time.sleep(0.1)


def Get_position():
    print(pyautogui.position())


if __name__ == "__main__":
    msgCount = int(input("How many messages would you like to delete? > "))
    # Get_position()
    time.sleep(2)
    AutoDelete(msgCount)
