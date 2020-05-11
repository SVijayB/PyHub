import arcade                       # pip install arcade

# Setting size for main window
Window_width = 700
Window_height = 700

# Creating and opening the window
arcade.open_window(Window_width,Window_height,"Smiley") 
arcade.set_background_color(arcade.color.BLACK)

# Base Structure
arcade.start_render()               # Always use this before starting
x = 350; y = 350; radius = 200
arcade.draw_circle_filled(x,y,radius,arcade.color.YELLOW)

arcade.finish_render()              # Ends the arcade
arcade.run()                        # Keeps the window running until closed