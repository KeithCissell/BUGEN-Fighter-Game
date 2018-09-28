import arcade

class Player(arcade.Sprite):
    """ Class to represent a character on the screen """

    def __init__(self, char):
        """ Initialize our character variables """
        super().__init__()
        character_path = "characters/" + char + "/img/"
        self.character = None
        self.all_character_sprites = None

        self.stand_left_textures = arcade.load_texture(character_path + "default.png", mirrored=True, scale=1.25)
        self.stand_right_textures = arcade.load_texture(character_path + "default.png", scale=1.25)

        self.walk_right_textures = arcade.load_texture(character_path + "characterW1.png", scale=1.25)
        self.walk_left_textures = arcade.load_texture(character_path + "characterW2.png", scale=1.25)
        self.fall_textures = arcade.load_texture(character_path + "characterW3.png", scale=1.25)
        self.jump_textures = arcade.load_texture(character_path + "characterW4.png", scale=1.25)

        self.texture = self.stand_left_textures

        self.movementSpeed = 5


    def update(self, game):
        """
        Description: This function updates the char for the game canvas.
        """
        self.character = arcade.AnimatedWalkingSprite()
        self.all_character_sprites = arcade.SpriteList()

        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.change_x < 0:
            self.texture = self.walk_left_textures
        elif self.change_x > 0:
            self.texture = self.walk_right_textures
        elif self.change_y > 0:
            self.texture = self.jump_textures
        elif self.change_y < -1:
            self.texture = self.fall_textures
        else:
            self.texture = self.stand_right_textures


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

    def move(self, direction):
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
