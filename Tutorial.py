#!/usr/bin/env python3
import arcade
arcade.open_window(800,600,"Drawing Example")
arcade.set_background_color(arcade.color.RED)
arcade.start_render()

# All the drawing commands go here
my_text = arcade.create_text("Text Example", arcade.color.BLACK, 10)
arcade.render_text(my_text, 250, 300, 45)

arcade.finish_render()
arcade.quick_run(2.5)
