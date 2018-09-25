import arcade

class TrainingFacility():
    """ Stage used for player training """

    def __init__(self):
        # Initialize stagek
        # Background texture
        self.background = arcade.load_texture("stages/TrainingFacility/img/main.jpg")
        # Load list of platforms
        self.platform_list = arcade.SpriteList()
        self.platform_list.append(arcade.sprite.Sprite("stages/TrainingFacility/img/platform.jpg", image_width = 800, image_height = 2, center_x = 500, center_y = 220)) # bottom
        self.platform_list.append(arcade.sprite.Sprite("stages/TrainingFacility/img/platform.jpg", image_width = 190, image_height = 2, center_x = 265, center_y = 325)) # mid left
        self.platform_list.append(arcade.sprite.Sprite("stages/TrainingFacility/img/platform.jpg", image_width = 185, image_height = 2, center_x = 720, center_y = 325)) # mid right
        self.platform_list.append(arcade.sprite.Sprite("stages/TrainingFacility/img/platform.jpg", image_width = 180, image_height = 2, center_x = 490, center_y = 425)) # top

    def update(self, arcade, game):
        """
        Description: This function updates the stage for the game canvas.
        """
        self.platform_list.update()

    def draw(self, arcade, game):
        """
        Description: This function draws the stage.
        """
        arcade.draw_texture_rectangle(game.gameOptions["window"]["width"] // 2, game.gameOptions["window"]["height"] // 2,
                                      game.gameOptions["window"]["width"], game.gameOptions["window"]["height"], self.background)
        self.platform_list.draw()
