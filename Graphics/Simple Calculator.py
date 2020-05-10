from tkinter import *
from PIL import Image       # pip install Pillow
from PIL import ImageTk

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equal():
    try:
        global expression
        result = str(eval(expression))
        equation.set(result)
        expression = ""
    except:
        equation.set("Invalid Equation")
        expression=""

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    window = Tk()
    window.configure(background="black")
    window.title("Simple Calculator")
    window.iconbitmap("assets\Graphics\Calculator\Logo.ico")
    window.geometry("280x300")
    
    equation = StringVar()
    expression_field = Entry(window,textvariable=equation,font=("Aerial",20),fg="red")
    expression_field.grid(columnspan=10,ipady=10,ipadx=70)

    width=50
    height=50

    img1 = Image.open("assets\Graphics\Calculator\one.PNG")
    img1 = img1.resize((width,height))  
    oneImage = ImageTk.PhotoImage(img1)
    button1 = Button(window, image=oneImage,bg="white",command = lambda:press(1),height=height,width=width)
    button1.grid(row=2,column=0)
    window.mainloop()
