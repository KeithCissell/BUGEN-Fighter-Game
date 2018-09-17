class ExampleScreen():
    """ Class to represent a screen state for the arcade, game """

    def __init__(self):
        """ Initialize Screen variables """
        pass

    def update(self, arcade, game, delta_time):
        """
        Description: This function is passed the arcade and game itself to modify.
        """
        pass

    def handleKeyPress(self, arcade, game, key, key_modifiers):
        """
        Description: This function handles key presses.
        """
        pass

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
        pass
