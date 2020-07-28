import pyperclip
"""
Program description : 
Adds a '#' to all the words in the sentence you provide and then copies it to your clipboard.
Can be used for insta and other social media platforms.

Note : To run this program -> `pip install paperclip` first.
"""
def hastags(value):
    value = value.split()
    string = ""
    for i in value:
        i = "#" + i
        string = string + i + " "
    print(string)
    pyperclip.copy(string)
    print("The above string has been copied to your clipboard :)")

if __name__ == "__main__":
    value = input("Enter the words you want to add hashtag(#) to \n> ")
    hastags(value)