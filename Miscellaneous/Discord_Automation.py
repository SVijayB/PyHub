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

def Message():
    while True:
        if keyboard.is_pressed("f2"):
            pyautogui.typewrite("Hey, welcome to TechEden! :partying_face:") 
            pyautogui.hotkey('shift', 'enter')
            pyautogui.typewrite("Thank you for taking part in our event and creating a community of coders and hackers around the world.") 
            pyautogui.hotkey('shift', 'enter')
            pyautogui.typewrite("And just for that, you deserve something special!")
            pyautogui.hotkey('shift', 'enter')
            pyautogui.typewrite("Here is a little something we'd like to offer in return :tada::gift:.")
            pyautogui.hotkey('shift', 'enter')
            pyautogui.hotkey('shift', 'enter')
            pyautogui.typewrite("**Balsamiq cloud**")
            pyautogui.hotkey('shift', 'enter')
            pyautogui.typewrite("Balsamiq Cloud is a web-based user interface design tool for creating wireframes, "+ 
            "You can use it to generate digital sketches of your idea or concept for an application or website, "+
            "to facilitate discussion and understanding before any code is written.")
            pyautogui.hotkey('shift', 'enter')
            pyautogui.hotkey('shift', 'enter')
            pyautogui.typewrite("**Wolfram|One**")
            pyautogui.hotkey('shift', 'enter')
            pyautogui.typewrite("Wolfram|One is the world's first fully-integrated cloud-desktop hybrid, integrated computation platform. "+ 
            "The core of it's technology stack is the Wolfram Language, which builds on three decades of development, " +  
            "and represents a new direction in programming that happens to be absolutely ideal for hackathons.")
            pyautogui.hotkey('shift', 'enter')
            pyautogui.hotkey('shift', 'enter')
            pyautogui.typewrite("Product: Wolfram|One, Wolfram API, and other Wolfram development platform.")
            pyautogui.press('enter')
        if keyboard.is_pressed("esc"):
            break

def paste():
    while True:
        if keyboard.is_pressed("f2"):
            pyautogui.keyDown('ctrl')
            pyautogui.press('v')
            pyautogui.keyUp('ctrl') 
            pyautogui.press('enter')
        if keyboard.is_pressed("esc"):
            break
        
if __name__ == "__main__":
    paste()