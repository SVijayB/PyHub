import arcade
from tkinter import Tk, messagebox
import sys
 
class Timer(arcade.Window):
    def __init__(self,width=300,height=150):
        super().__init__(width,height)
        self.time = 0.0

    def Window(self,time):
        arcade.set_background_color(arcade.color.BLACK)
        self.time = time

    def on_draw(self):
        arcade.start_render()
        min = int(self.time)//60
        sec = int(self.time)%60
        result = f"Time : {min}:{sec}"
        arcade.draw_text(result,60,60,arcade.color.RED,35)
        if(min<0):
            root = Tk()
            root.withdraw()
            messagebox.showinfo("Info Box","Countdown Has Reached Zero")
            sys.exit(0)

    def on_update(self,new_time):
        self.time = self.time - new_time

if __name__=="__main__":
    try:
        time = int(input("Enter how many seconds you want to count : "))
    except:
        print("ERROR : ENTER ONLY INTEGER VALUES")
    else:
        timer = Timer()
        timer.Window(time)
        arcade.run()
