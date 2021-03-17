# Adding images as background.
from tkinter import *

root = Tk()
root.title("Images")
root.geometry("350x350")
root.iconbitmap("assets/favicon.ico")
root.configure(bg="black")
img_loc = PhotoImage(file="assets/Random.PNG")
img = Label(root, image=img_loc)
img.pack()
root.mainloop()
