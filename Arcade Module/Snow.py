import arcade
import random
import math

win_width = 800
win_height = 600

class snow():
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def reset_pos(self):
        self.x = random.randrange(win_width)
        self.y = random.randrange(win_height,win_height+100)

class game(arcade.Window):
    def __init__(self,width,height):
        super().__init__(width,height)
        self.stream = None

    def start(self):
        self.stream = []
        snowflake = snow()
        snowflake.x = random.randrange(win_width)
        snow.y = random.randrange(win_height+400)
        
        snowflake.size = random.randrange(2)
        snowflake.speed = random.randrange(20,100)
        snowflake.angle = random.uniform(math.pi, math.pi*2) 
        self.stream.append(snowflake)

        arcade.set_background_color(arcade.color.BLACK)

    def draw(self):
        arcade.start_render()
        for snowflake in self.stream:
            arcade.draw_circle_filled(snowflake.x, snowflake.y, snowflake.size, arcade.color.WHITE)

    def update(self,new_time):
        for snowflake in self.stream:
            snowflake.y = snowflake.y - (snowflake.speed * new_time) 
            if(snowflake.y<0):
                snowflake.reset_pos()

            snowflake.x = snowflake.x + (snowflake.speed * math.cos(snowflake.angle) * new_time)
            snowflake.angle = snowflake.angle + new_time

if __name__=="__main__":
    game = game(win_width,win_height)
    game.start()
    arcade.run()
