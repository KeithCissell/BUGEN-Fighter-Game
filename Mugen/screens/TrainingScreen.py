class TrainingScreen():
    """ Class to represent a screen state for the game """

    def __init__(self):
        """ Initialize Screen variables """
        pass

    def load(self, arcade, game):
        """
        Description: This function re-initializes and loads up the screen.
        """
        pass

    def update(self, arcade, game, delta_time):
        """
        Description: This function is passed the game itself to modify.
        """
        game.player1.update(game)

    def handleKeyPress(self, arcade, game, key, key_modifiers):
        """
        Description: This function handles key presses.
        """
        if key == arcade.key.UP:
            game.player1.change_y = game.player1.movementSpeed
        elif key == arcade.key.DOWN:
            game.player1.change_y = -game.player1.movementSpeed
        elif key == arcade.key.LEFT:
            game.player1.change_x = -game.player1.movementSpeed
        elif key == arcade.key.RIGHT:
            game.player1.change_x = game.player1.movementSpeed

    def handleKeyRelease(self, arcade, game, key, key_modifiers):
        """
        Description: This function is called whenever the user lets off a previously pressed key.
        """
        if key == arcade.key.UP or key == arcade.key.DOWN:
            game.player1.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            game.player1.change_x = 0

    def handleMousePress(self, arcade, game, x, y, button, modifiers):
        """
        This function is called when the user presses a mouse button.
        """
        pass

    def draw(self, arcade, game):
        """
        Description: The rendering function.
        """
        arcade.set_background_color(arcade.color.YELLOW)
        game.players.draw()
