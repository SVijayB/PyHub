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

    img1 = Image.open("assets/Graphics/Calculator/one.PNG")
    img1 = img1.resize((width,height))  
    oneImage = ImageTk.PhotoImage(img1)
    button1 = Button(window, image=oneImage,bg="white",command = lambda:press(1),height=height,width=width)
    button1.grid(row=2,column=0)

    img2 = Image.open("assets/Graphics/Calculator/two.PNG")
    img2 = img2.resize((width,height))  
    twoImage = ImageTk.PhotoImage(img2)
    button2 = Button(window, image=twoImage,bg="white",command = lambda:press(2),height=height,width=width)
    button2.grid(row=2,column=1)

    img3 = Image.open("assets/Graphics/Calculator/three.PNG")
    img3 = img3.resize((width,height))  
    threeImage = ImageTk.PhotoImage(img3)
    button3 = Button(window, image=threeImage,bg="white",command = lambda:press(3),height=height,width=width)
    button3.grid(row=2,column=2)

    img4 = Image.open("assets/Graphics/Calculator/four.PNG")
    img4 = img4.resize((width,height))  
    fourImage = ImageTk.PhotoImage(img4)
    button4 = Button(window, image=fourImage,bg="white",command = lambda:press(4),height=height,width=width)
    button4.grid(row=3,column=0)

    img5 = Image.open("assets/Graphics/Calculator/five.PNG")
    img5 = img5.resize((width,height))  
    fiveImage = ImageTk.PhotoImage(img5)
    button5 = Button(window, image=fiveImage,bg="white",command = lambda:press(5),height=height,width=width)
    button5.grid(row=3,column=1)

    img6 = Image.open("assets/Graphics/Calculator/six.PNG")
    img6 = img6.resize((width,height))  
    sixImage = ImageTk.PhotoImage(img6)
    button6 = Button(window, image=sixImage,bg="white",command = lambda:press(6),height=height,width=width)
    button6.grid(row=3,column=2)

    img7 = Image.open("assets/Graphics/Calculator/seven.PNG")
    img7 = img7.resize((width,height))  
    sevenImage = ImageTk.PhotoImage(img7)
    button7 = Button(window, image=sevenImage,bg="white",command = lambda:press(7),height=height,width=width)
    button7.grid(row=4,column=0)

    img8 = Image.open("assets/Graphics/Calculator/eight.PNG")
    img8 = img8.resize((width,height))  
    eightImage = ImageTk.PhotoImage(img8)
    button8 = Button(window, image=eightImage,bg="white",command = lambda:press(8),height=height,width=width)
    button8.grid(row=4,column=1)

    img9 = Image.open("assets/Graphics/Calculator/nine.PNG")
    img9 = img9.resize((width,height))  
    nineImage = ImageTk.PhotoImage(img9)
    button8 = Button(window, image=nineImage,bg="white",command = lambda:press(9),height=height,width=width)
    button8.grid(row=4,column=2)



    window.mainloop()
