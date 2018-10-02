import arcade

class Field():
    """ Stage used for player training """

    def __init__(self):
        # Initialize stagek
        # Background texture
        self.background = arcade.load_texture("stages/Field/img/TrainingField.PNG")
        # Load list of platforms
        self.platform_list = arcade.SpriteList()
        self.platform_list.append(arcade.sprite.Sprite("stages/Field/img/platform.jpg", image_width = 1000, image_height = 2, center_x = 500, center_y = 15)) # bottom

        # Player Start Positions
        self.p1_start_x = 900
        self.p1_start_y = 30
        self.p2_start_x = 100
        self.p2_start_y = 30

    def update(self, arcade, game):
        """
        Description: This function updates the stage for the game canvas.
        """
        self.platform_list.update()

    def draw(self, arcade, game):
        """
        Description: This function draws the stage.
        """
        # Draw Background
        arcade.draw_texture_rectangle(game.gameOptions["window"]["width"] // 2, game.gameOptions["window"]["height"] // 2,
                                      game.gameOptions["window"]["width"], game.gameOptions["window"]["height"], self.background)
        # Draw platforms (for debugging)
        # self.platform_list.draw()
