import tkinter as tk
import random
import os

black = "\033[1;0;40m"


def red(message):
    print("\033[1;31;40m" + message + black)


def grey(message):
    print("\033[1;30;40m" + message + black)


def green(message):
    print("\033[1;32;40m" + message + black)


def yellow(message):
    print("\033[1;33;40m" + message + black)


def blue(message):
    print("\033[1;34;40m" + message + black)


def pink(message):
    print("\033[1;35;40m" + message + black)


def cyan(message):
    print("\033[1;36;40m" + message + black)

logo = """
 _____              _      _____      _              
|_   _|            | |    |  ___|    | |             
  | |    ___   ___ | |__  | |__    __| |  ___  _ __  
  | |   / _ \ / __|| '_ \ |  __|  / _` | / _ \| '_ \ 
  | |  |  __/| (__ | | | || |___ | (_| ||  __/| | | |
  \_/   \___| \___||_| |_|\____/  \__,_| \___||_| |_|


"""

def randomiser():
    themes = ["Fintech","Automation Tools","Healthtech","Transport","Cyber Security","Education"]
    random_themes = []
    themes_dict = {}
    for i in range(6):
        x = random.choices(themes)[0]
        random_themes.append(x)
        themes.remove(x)
    num_set = [1,2,3,4,5,6]
    for i in range(6):
        themes_dict[num_set[i]] = random_themes[i]
    return themes_dict

def picker(themes):
    for i in range(6):
        if(i == 0 or i == 3):
            yellow(logo)
        if(i == 1 or i == 4):
            pink(logo)
        if(i == 2 or i == 5):
            red(logo)
        keys = list(themes.keys())
        print("Pick any one of these numbers", end = " ")
        keys_string = ''.join(str(keys))
        cyan(keys_string)
        choice = int(input("> "))
        try:
            print("Your theme is ", end="")
            green(str(themes[choice]) + ".")
            print("Good luck!")
        except:
            print("Pick the correct number!")
            choice = int(input("> "))
            print("Your theme is ", end="")
            green(str(themes[choice]) + ".")
            print("Good luck!")
        del themes[choice]
        input()
        os.system("cls")

if __name__ == "__main__":
    while(True):
        os.system("cls")
        green(logo)
        choice = input("Start assigning themes?(Y/n)\n> ")
        if(choice == "Yes" or choice == "Y" or choice == "y" or choice == "yes"):
            os.system("cls")
            themes = randomiser()
            picker(themes)
        else:
            print("Good luck to all the participants! Thank you for taking part in TechEden.")
            input()
            break

# Future scope: Add in module to directly append team name with theme picked to an excel sheet.
# Build a simple discord bot that takes in the team name -> Checks for the role and then provides them a random theme.