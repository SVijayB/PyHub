# Events in python are events that occur when a button is pressed
from tkinter import *
import sys

def click(event):       # event has to be mentioned to let the function know that it is being used in a button
    print("Single Click")       

def DoubleClick(event):
    print("Double Click")

window = Tk()
window.title("Check Boxes")
window.geometry("200x200")
window.iconbitmap("assets/Graphics/favicon.ico")
button = Button(window,text="Click on this button!")
button.pack()
button.bind("<Button-1>",click)             # Used for single click, built in function.
button.bind("<Double-1>",DoubleClick)       # Used for double click, built in function.
window.mainloop()


##


window = Tk()
window.title("Submit Boxes")
window.geometry("200x200")
window.iconbitmap("assets/Graphics/favicon.ico")

frame = Frame(window)
frame.pack()

label1 = Label(frame,text="First Name : ")
label1.pack()
first_name = StringVar()
first_name = Entry(textvariable=first_name)
first_name.pack()

label2 = Label(frame,text="Last Name : ")
label2.pack()
last_name = StringVar()
last_name = Entry(textvariable=last_name)
last_name.pack()

def Submit_button(event):
    print("Hey, "+first_name.get()+" "+last_name.get()+".")

button = Button(frame,text="SUBMIT")
button.bind("<Button-1>",Submit_button)
button.pack()
window.mainloop()