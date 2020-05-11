import arcade

win_width = 800
win_height = 600

rec_width = 50
rec_height = 50
speed = 5

class Rectangle:
    def __init__(self,x,y,rec_width,rec_height,angle,colour):
        self.x = x
        self.y = y

        self.new_x = 0                     # New position
        self.new_y = 0

        self.angle = angle
        self.rec_width = rec_width
        self.rec_height = rec_height
        self.colour = colour

    def on_draw(self):
        arcade.draw_rectangle_filled(self.x,self.y,self.rec_width,self.rec_height,self.colour,self.angle)

    def move(self):
        self.x = self.x + self.new_x
        if(self.x < (rec_width//2)):
            self.x = rec_width//2       
        if(self.x > win_width - (rec_width // 2)):
            self.x = win_width - (rec_width // 2)

        self.y = self.y + self.new_y
        if(self.y < (rec_height//2)):
            self.y = rec_height//2
        if(self.y > win_height - (rec_height // 2)):
            self.y = win_height - (rec_height // 2)