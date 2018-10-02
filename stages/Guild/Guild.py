import arcade

class Guild():
    """ Stage used for player training """

    def __init__(self):
        # Initialize stagek
        # Background texture
        self.background = arcade.load_texture("stages/Guild/img/FairyTailGuild.png")
        # Load list of platforms
        self.platform_list = arcade.SpriteList()
        self.platform_list.append(arcade.sprite.Sprite("stages/Guild/img/platform.jpg", image_width = 1000, image_height = 2, center_x = 500, center_y = 70)) # bottom
        self.platform_list.append(arcade.sprite.Sprite("stages/Guild/img/platform.jpg", image_width = 190, image_height = 2, center_x = 285, center_y = 232)) # mid left
        self.platform_list.append(arcade.sprite.Sprite("stages/Guild/img/platform.jpg", image_width = 185, image_height = 2, center_x = 700, center_y = 232)) # mid right
        self.platform_list.append(arcade.sprite.Sprite("stages/Guild/img/platform.jpg", image_width = 420, image_height = 2, center_x = 490, center_y = 335)) # top
        self.platform_list.append(arcade.sprite.Sprite("stages/Guild/img/platform.jpg", image_width = 220, image_height = 2, center_x = 490, center_y = 415)) # top

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
