import arcade

arcade.open_window(600, 600, "My Guitar")
arcade.set_background_color(arcade.color.BLACK)

arcade.start_render()


#guitar neck
arcade.draw_rectangle_filled(350, 300, 250, 20, arcade.color.GHOST_WHITE)

#guitar body
arcade.draw_triangle_filled(300, 300, 100, 400, 150, 300, arcade.color.ALLOY_ORANGE)
arcade.draw_triangle_filled(300, 300, 100, 200, 150, 300, arcade.color.ALLOY_ORANGE)

#guitar head
arcade.draw_triangle_filled(450, 300, 475, 320, 475, 280, arcade.color.ALLOY_ORANGE )
arcade.draw_triangle_filled(550, 300, 475, 320, 475, 280, arcade.color.ALLOY_ORANGE )

#guitar strings
arcade.draw_line(250,300, 520, 300, arcade.color.BLACK)

arcade.finish_render()
arcade.run()
