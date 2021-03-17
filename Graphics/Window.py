# Creating a window using Tkinter Module.
from tkinter import *

window = Tk()
window.title("Hello World!")  # Setting title of the window.
window.geometry("350x350")  # Setting the size of the window.
window.iconbitmap("assets/favicon.ico")  # Setting the icon for the window.
window.configure(bg="blue")  # Added Background of the window as blue.
image = PhotoImage(file="assets/Random.PNG")  # Gets Image from location.
button = Button(window, image=image)  # Inserts Image as a button in the window.
button.pack()
window.mainloop()  # Makes sure the window does not autoclose.
