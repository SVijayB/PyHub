from tkinter import *
from tkinter import simpledialog

window = Tk()
window.title("Check Boxes")
window.geometry("320x240")
window.iconbitmap("assets/favicon.ico")
colour = simpledialog.askstring(
    "Colour", "Enter A Colour : ", parent=window
)  # First arg = title, second = message
if colour == None:
    print("You did not enter any colour :(")
else:
    print("You have entered", colour)

number = simpledialog.askinteger(
    "Number", "Enter A Number : ", parent=window
)  # askinteger to take only integer type values
if number == None:
    print("You did not enter any number :(")
else:
    print("You have entered", number)

window.mainloop()
