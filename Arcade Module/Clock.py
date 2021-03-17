import arcade
import math as m

win_width = 900
win_height = 700

x_axis = win_width // 2  # X-Axis
y_axis = win_height // 2  # Y-Axis
rad = 60 / 360
lenth = 300


def on_draw(new_time):
    on_draw.angle = on_draw.angle + rad
    x = lenth * m.sin(on_draw.angle) + x_axis  # Sin for X axis
    y = lenth * m.cos(on_draw.angle) + y_axis  # Cos for Y axis

    arcade.start_render()
    arcade.draw_line(x_axis, y_axis, x, y, arcade.color.RED, 5)
    arcade.draw_circle_outline(x_axis, y_axis, lenth, arcade.color.BLUE, 10)


on_draw.angle = 0

if __name__ == "__main__":
    arcade.open_window(win_width, win_height, "CLOCK")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_draw, 1)
    arcade.run()
