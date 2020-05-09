# Adding images as background.
from tkinter import *

root = Tk()
root.title("Images")
root.geometry("350x350")
root.iconbitmap("assets/Graphics/favicon.ico")
root.configure(bg="black")
img_loc = PhotoImage(file="assets/Graphics/Random.PNG")
img = Label(root,image=img_loc)
img.pack()
root.mainloop()