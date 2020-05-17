from tkinter import *

window = Tk()
window.title("Check Boxes")
window.geometry("320x240")
window.iconbitmap("assets/favicon.ico")
radio_state = IntVar()
male = Radiobutton(window,text="Male",variable=radio_state,value=1)     #Every radio button in a group must have unique value.
male.grid(column=0,row=0)
woman = Radiobutton(window,text="Female",variable=radio_state,value=2)  #Same type radio buttons are assigned to same vairable.
woman.grid(column=1,row=0)
radio_state1 = IntVar()
black = Radiobutton(window,text="Black",variable=radio_state1,value=1)  #Different group.
black.grid(column=0,row=1)
white = Radiobutton(window,text="White",variable=radio_state1,value=2)
white.grid(column=1,row=1)
window.mainloop()