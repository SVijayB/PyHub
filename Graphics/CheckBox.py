from tkinter import *

window = Tk()
window.title("Check Boxes")
window.geometry("400x400")
window.iconbitmap("assets/favicon.ico")
a = IntVar()
a.set(True)
check_box1 = Checkbutton(window,text="Python is fun?",variable = a)             
check_box1.grid(column=0,row=0)
check_box2 = Checkbutton(window,text="Tkinter is good?",variable = a)    #Both are assigned the same value
check_box2.grid(column=1,row=0)
b = IntVar()
check_box3 = Checkbutton(window,text="This makes sense?",variable = b)   
check_box3.grid(column=2,row=0)
window.mainloop()