import arcade

class Player(arcade.Sprite):
    """ Class to represent a character on the screen """

    def __init__(self, char):
        """ Initialize our character variables """
        super().__init__()
        character_path = "characters/" + char + "/img/"
        self.character = None
        self.all_character_sprites = None
        self.direction = "Right"
        self.punch = False

        self.left_stand = arcade.load_texture(character_path + "default.png", mirrored=True, scale=1.25)
        self.left_walk_forward = arcade.load_texture(character_path + "characterW1.png", mirrored=True, scale=1.25)
        self.left_walk_back = arcade.load_texture(character_path + "characterW2.png", mirrored=True, scale=1.25)
        self.left_fall = arcade.load_texture(character_path + "characterW3.png", mirrored=True, scale=1.25)
        self.left_jump = arcade.load_texture(character_path + "characterW4.png", mirrored=True, scale=1.25)

        self.right_stand = arcade.load_texture(character_path + "default.png", scale=1.25)
        self.right_walk_forward = arcade.load_texture(character_path + "characterW1.png", scale=1.25)
        self.right_walk_back = arcade.load_texture(character_path + "characterW2.png", scale=1.25)
        self.right_fall = arcade.load_texture(character_path + "characterW3.png", scale=1.25)
        self.right_jump = arcade.load_texture(character_path + "characterW4.png", scale=1.25)

        self.right_punch = arcade.load_texture(character_path + "punch.png", scale=1.25)
        self.left_punch = arcade.load_texture(character_path + "punch.png", mirrored=True, scale=1.25)

        self.texture = self.left_stand

        self.movementSpeed = 0


    def update(self, game):
        """
        Description: This function updates the char for the game canvas.
        """

        self.character = arcade.AnimatedWalkingSprite()
        self.all_character_sprites = arcade.SpriteList()

        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.direction == "Right":
            if self.change_x < 0:
                self.texture = self.right_walk_back
            elif self.change_x > 0:
                self.texture = self.right_walk_forward
            elif self.change_y > 0:
                self.texture = self.right_jump
            elif self.change_y < -1:
                self.texture = self.right_fall
            else:
                self.texture = self.right_stand
        else:
            if self.change_x > 0:
                self.texture = self.left_walk_back
            elif self.change_x < 0:
                self.texture = self.left_walk_forward
            elif self.change_y > 0:
                self.texture = self.left_jump
            elif self.change_y < -1:
                self.texture = self.left_fall
            else:
                self.texture = self.left_stand

        if self.punch == True:
            if self.direction == "Right":
                self.texture = self.right_punch
            else:
                self.texture = self.left_punch

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
