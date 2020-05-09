from tkinter import *

window = Tk()
window.geometry("480x240")
text = Entry(window,width=20,font=("Arial",20),fg="red")   # We can choose only the width and not the height
text.grid(column=0,row=0,ipady=10)      # To increase verically, we use Ipady. Value given are in px
window.mainloop()

window = Tk()
window.geometry("480x240")
text = Text(window,width=30,height=1,font=("Arial",25),fg="red") # Text lets you modify height.
text.focus()                   # Used to make sure the cursor is already focused at the textbox
text.grid(column=0,row=0)      # To increase verically, we use Ipady. Value given are in px
window.mainloop()