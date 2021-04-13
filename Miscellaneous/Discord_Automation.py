import pyautogui
import time
import keyboard


def Create_categories():
    i = 54
    while i < 100:
        time.sleep(1)
        pyautogui.click(216, 67)
        time.sleep(1)
        pyautogui.click(306, 299)
        time.sleep(1)
        pyautogui.typewrite("WEB HUNT TEAM " + str(i))
        time.sleep(1)
        pyautogui.click(1183, 522)
        time.sleep(1)
        pyautogui.click(1136, 688)
        time.sleep(1)
        pyautogui.click(1143, 818)
        i = i + 1


def Get_position():
    print(pyautogui.position())


def Delete_category():
    i = 0
    while i < 20:
        pyautogui.click(185, 222, button="right")
        time.sleep(0.5)
        pyautogui.click(322, 460)
        time.sleep(1)
        pyautogui.click(1153, 578)
        i = i + 1


def Assign_roles():
    i = 69
    while True:
        if keyboard.is_pressed("p"):
            pyautogui.click(500, 500)
            pyautogui.click(422, 190)
            time.sleep(1)
            pyautogui.click(1320, 347)
            time.sleep(1)
            pyautogui.typewrite(str(i))
            time.sleep(1)
            pyautogui.click(859, 482)
            time.sleep(1)
            pyautogui.click(1169, 768)
            time.sleep(1)
            pyautogui.click(1539, 123)
            time.sleep(1)
            i = i + 1
        if keyboard.is_pressed("esc"):
            break


def Create_channels():
    while True:
        if keyboard.is_pressed("o"):
            pyautogui.click()
            pyautogui.typewrite("text-room")
            pyautogui.click(1107, 770)
            pyautogui.moveTo(500, 500)
        if keyboard.is_pressed("p"):
            pyautogui.click()
            pyautogui.click(830, 461)
            keyboard.press("tab")
            pyautogui.typewrite("VC")
            pyautogui.click(1107, 770)
            pyautogui.moveTo(500, 500)
        if keyboard.is_pressed("esc"):
            break

def rename():
    i = 12
    while True:
        if keyboard.is_pressed("q"):
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('backspace')
            time.sleep(0.5)
            pyautogui.typewrite("TEAM " + str(i))
            pyautogui.click(1410, 965)
            time.sleep(0.5)
            pyautogui.hotkey('esc')
            i = i + 1
            pyautogui.moveTo(283, 471)
        if keyboard.is_pressed("w"):
            break


if __name__ == "__main__":
    rename()
