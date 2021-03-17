import pyperclip

"""
Program description : 
Takes a string as input and creates an alternating upper and lower case pattern of the string. Eg : Hello becomes hELlO.

Note : The output is copied to clipboard. To do this, first => `pip install pyperclip`
"""


def caseswapper(value, choice):
    if choice == "uppercase" or choice == "upper" or choice == "u":
        j = 0
    else:
        j = 1
    string = ""
    for i in value:
        if j % 2 == 0:
            i = i.upper()
        else:
            i = i.lower()
        j = j + 1
        string = string + i
    print(string)
    pyperclip.copy(string)
    print("The above string has been copied to your clipboard :)")


if __name__ == "__main__":
    value = input("Enter a sentence \n> ")
    choice = input(
        "Do you want the first letter to in uppercase or lowercase? (U/L) \n> "
    ).lower()
    caseswapper(value, choice)
