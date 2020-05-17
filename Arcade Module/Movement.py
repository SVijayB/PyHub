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

    def draw(self):
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

class movement(arcade.Window):
    def __init__(self,width,height):
        super().__init__(width,height,title="MOVEMENT")

    def start(self):
        x = win_width//2
        y = win_height//2
        self.player = Rectangle(x,y,rec_width,rec_width,angle=0,colour=arcade.color.RED)

    def on_update(self, dt):
        self.player.move()

    def on_draw(self):
        arcade.start_render()
        self.player.draw()

    def on_key_press(self, key, modif):
        if (key == arcade.key.UP):
            self.player.new_y = speed
        elif (key == arcade.key.DOWN):
            self.player.new_y = -speed
        elif (key == arcade.key.LEFT):
            self.player.new_x = -speed
        elif (key == arcade.key.RIGHT):
            self.player.new_x = speed
    
    def on_key_release(self, key, modif):
        if (key == arcade.key.UP or key == arcade.key.DOWN):
            self.player.new_y = 0
        if (key == arcade.key.LEFT or key == arcade.key.RIGHT):
            self.player.new_x = 0

if __name__=="__main__":
    print("Use Arrow Keys to move the square")
    move = movement(win_width,win_height)
    move.start()
    arcade.run()