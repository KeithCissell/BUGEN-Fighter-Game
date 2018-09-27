import arcade

class TestChar(arcade.Sprite):
    """ Class to represent a character on the screen """

    def __init__(self, center_x = 0):
        """ Initialize our character variables """
        super().__init__("characters/test/img/gandalf.png", scale = 0.25, center_x = center_x)
        self.movementSpeed = 5

    def update(self, game):
        """
        Description: This function updates the char for the game canvas.
        """
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > game.gameOptions['window']['width'] - 1:
            self.right = game.gameOptions['window']['width'] - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > game.gameOptions['window']['height'] - 1:
            self.top = game.gameOptions['window']['height'] - 1

    def draw(self):
        """
        Description: This function draws the character.
        """
        super().draw()

    def move(self):
        """
        Description: This function gets called whenever a directional button was pushed.
        """
        pass

    def action(self):
        """
        Description: This function is called whenever an action button was pressed.
        """
        pass

    def collision(self):
        """ detect collisions"""
        pass
