from tkinter import *
def doc():
    """
Menu Parameters : 
Activebackground    : Used to set the background colour when mouse hovers over the menu button.
Activeforeground    : Used to set the font colour when the mouse hovers over the menu button.
Bd                  : Used to set the size of the border around the indicator. Default = 2px
Bitmap              : Used to display a bitmap on the menu button. 
Bg                  : Background colour used to display behind the label.
Cursor              : Cursor that appears when the mouse is over a menu button.
Direction           : Used to set direction to set menu to the left or right of a button.
Disabledforeground  : When inaccessible.
Fg                  : Used to specify Foreground colour when mouse is not over the menu button.
Height              : Height of menu buttons.
Highlightcolor      : Colour shown in the focus highlight when widget is on focus
Image               : Used to add image to menu buttons
Justify             : Controls where text is located when text does not fill menu button.(Aligned)
Menu                : To assosiate menu with a set of choices.
Padx                : Specifies how much space to leave to the left and right of the menu button.
Pady                : Specifies how much space to leave to the top and bottom of the menu button.
Relief              : Used to select 3D border shading effect.
State               : Set state=disabled to grey out the menu button to make it unresponsive.
Underline           : Setting a menu button to underline.
Width               : Width of the widget in characters. Default = 20.
Wraplenth           : Used to wrap the line.
    """
print(doc.__doc__)

root = Tk()
root.title("Menus")
root.geometry("300x300")
root.iconbitmap("assets/favicon.ico")

menu_button = Menubutton(root,text="Colours",relief=RAISED)     # Apears raised
menu_button.grid()
menu_button.menu = Menu(menu_button,tearoff=0)                  # If no buttons are added, nothing empty shows up
menu_button["menu"] = menu_button.menu
menu_button.pack()
menu_button.menu.add_checkbutton(label="Blue",variable=IntVar())
menu_button.menu.add_checkbutton(label="Green",variable=IntVar())
root.mainloop()