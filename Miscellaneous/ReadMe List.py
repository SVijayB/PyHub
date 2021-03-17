import pyperclip

"""
Program description : 
Helps you in creating an easy README interface with list of data and programs linked to each other.

Note : To run this program -> `pip install pyperclip` first.
"""


def Concat(n, base_url):
    para = ""
    base_url_length = len(base_url)
    for i in range(n):
        url = input("Enter the URL of the program \n> ")
        url_length = len(url)
        name = ""
        j = base_url_length + 1
        while j < url_length:
            name = name + url[j]
            j = j + 1
        name = name.replace("%20", " ")

        point = "• "
        start_tag = '<a href="' + url + '">'
        end_tag = "</a>"
        link = start_tag + name + end_tag
        space_length = 30 - len(name)
        space = ""

        for x in range(space_length):
            space = space + " "

        message = input("Enter Your message here \n> ")
        message = "| " + message
        end = "."
        final_result = point + link + space + message + end

        print(final_result)

        para = "\n" + para + final_result + "\n"

    print(para)
    pyperclip.copy(para)
    print("The final result has been copied to your clipboard :)")


if __name__ == "__main__":
    n = int(input(("Enter number of entries \n> ")))
    base_url = input("Enter Base URL \n> ")
    Concat(n, base_url)
