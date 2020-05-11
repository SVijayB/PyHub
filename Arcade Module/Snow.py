import random
import math
import arcade

class Snow:
    def __init__(self, height, width):
        self.x = 0
        self.y = 0

    def reset_pos(self, height, width):
        self.y = random.randrange(height, height + 100)
        self.x = random.randrange(width)


class MyGame(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)
        self.stream = None

    def start(self, height, width):
        self.stream = []

        for i in range(100):
            snow = Snow(800, 600)
            snow.x = random.randrange(width)
            snow.y = random.randrange(height + 200)
            snow.size = random.randrange(2)
            snow.speed = random.randrange(20, 100)
            snow.angle = random.uniform(math.pi, math.pi * 2)
            self.stream.append(snow)
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):                  # This is a default function.
        arcade.start_render()
        for snow in self.stream:
            arcade.draw_circle_filled(snow.x, snow.y,snow.size, arcade.color.WHITE)

    def on_update(self, delta_time):    # This is a default function.
        for snow in self.stream:
            snow.y = snow.y - snow.speed * delta_time
            if snow.y < 0:
                snow.reset_pos(800, 600)
            snow.x = snow.x + snow.speed * math.cos(snow.angle) * delta_time
            snow.angle = snow.angle + delta_time

if __name__ == "__main__":
    window = MyGame(800, 600)
    window.start(800, 600)
    arcade.run()