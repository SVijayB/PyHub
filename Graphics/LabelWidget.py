# Using the Label Widget to display text on the window.
from tkinter import *
tk = Tk()

tk.title("Hello World!")
tk.geometry("500x500")
tk.iconbitmap("assets/Graphics/favicon.ico")
label = Label(tk,text="I am 1StranGe",font=("Arial Bold",18))      
label.grid(column=0,row=0)              # Setting the string to print at pos (0,0)
tk.mainloop()
