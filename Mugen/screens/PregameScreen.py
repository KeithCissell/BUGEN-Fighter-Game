class PregameScreen():
    """ Class to represent a screen state for the game """

    def __init__(self):
        """ Initialize Screen variables """
        pass

    def update(self, arcade, game, delta_time):
        """
        Description: This function is passed the game itself to modify.
        """
        pass

    def handleKeyPress(self, arcade, game, key, key_modifiers):
        """
        Description: This function handles key presses.
        """
        if key == arcade.key.ENTER:
            game.player1 = game.testChar
            game.currentView = game.trainingScreen

    def handleKeyRelease(self, arcade, game, key, key_modifiers):
        """
        Description: This function is called whenever the user lets off a previously pressed key.
        """
        pass

    def handleMousePress(self, arcade, game, x, y, button, modifiers):
        """
        This function is called when the user presses a mouse button.
        """
        pass

    def draw(self, arcade, game):
        """
        Description: The rendering function.
        """
        #STEP-01: load the game logo
        box_width = 500
        box_height = 60
        font_size = 30
        x = (game.gameOptions['window']['width'] // 2) - (box_width//2)
        y = (game.gameOptions['window']['height'] / 2) - (box_height//2)
        arcade.draw_lrtb_rectangle_outline(x, x + box_width, y + box_height, y, arcade.color.BLUE, 1)
        arcade.draw_text(game.gameOptions['window']['name'], x, y + (box_height//4), arcade.color.BLACK, font_size, width=box_width, align="center")
