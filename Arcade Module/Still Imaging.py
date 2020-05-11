import arcade 
import random

win_width = 800
win_height = 600 

# Drawing the background Screen :
def screen():
    arcade.draw_rectangle_filled(win_width/2, win_height*2/3, win_width-1, win_height*2/3, arcade.color.SKY_BLUE)
    arcade.draw_rectangle_filled(win_width/2, win_height/6, win_width-1, win_height/3, arcade.color.LIGHT_GREEN)

def birds(x,y):
    arcade.draw_arc_outline(x, y, 40, 40, arcade.color.BLACK, 0, 90,3)
    arcade.draw_arc_outline(x+40, y, 40, 40, arcade.color.BLACK, 90, 180,3)   

if __name__=="__main__":
    arcade.open_window(win_width,win_height,"Still Imaging")
    arcade.start_render()
    screen()
    for i in range (10):
        x = random.randrange(0,win_width)
        y = random.randrange(win_height/2,win_height-20)
        birds(x,y)
    arcade.finish_render()
    arcade.run()

