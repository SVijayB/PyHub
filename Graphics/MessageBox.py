from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Buttons")
root.geometry("300x300")
root.iconbitmap("assets/Graphics/favicon.ico")

def info_box():
    messagebox.showinfo("Info Box","This is an Info Box")   # First Arg is title, Second Arg is the info.

def error_box():
    messagebox.showerror("Error Box","This is an Error Box")  #showerror displays error box

def warning_box():
    messagebox.showwarning("Warning Box","This is a Warning Box")  #showwarning displays warning box

info_button = Button(root,text="Info Box",command=info_box)
info_button.grid(column=0,row=0) 

error_button = Button(root,text="Error Box",command=error_box)
error_button.grid(column=1,row=0) 

warning_button = Button(root,text="Warning Box",command=warning_box)
warning_button.grid(column=2,row=0) 

root.mainloop()

# There are other types of message boxes as well.

root = Tk()
root.title("Buttons")
root.geometry("300x300")
root.iconbitmap("assets/Graphics/favicon.ico")
answer = messagebox.askyesno("Yes or No Box","Do you like Blue?")
if(answer):
    print("\nYou like blue!!")
else:
    print("\nOh, guess not everyone likes blue.")

temp = messagebox.askokcancel("Okay,Cancel Box","This is another message box!")
temp = messagebox.askretrycancel("Retry, Cancel Box","What do you want to do?")
temp = messagebox.askyesnocancel("Yes,No,Cancel Box","Do you like PYTHON!????")
if(temp):
    print("\nNice")
else:
    print("\nOh, guess not everyone likes Python xD")
