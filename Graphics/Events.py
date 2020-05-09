# Events in python are events that occur when a button is pressed
from tkinter import *

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