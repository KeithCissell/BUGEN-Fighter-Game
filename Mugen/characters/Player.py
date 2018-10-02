import arcade
import time

class Bullet(arcade.Sprite):
    def __init__(self, bulletSpeed, center_x, center_y):
        super().__init__("images/ball.jpg", 0.1)
        self.center_x = center_x
        self.center_y = center_y
        self.bulletSpeed = bulletSpeed
        self.damage = 10

    def update(self):
        if self.center_x > 1000 or self.center_x < 0:
            self.kill()
        else:
            self.center_x += self.bulletSpeed

    def draw(self):
        super().draw()

class Player(arcade.Sprite):
    """ Class to represent a character on the screen """

    def __init__(self, char):
        """ Initialize our character variables """
        # Resource Setup
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

        # Player Attributes
        self.movementSpeed = 5
        self.health = 100
        self.energy = 0

        # Projectile attributes
        self.gun_sound = arcade.sound.load_sound("sounds/laser1.mp3")
        self.hit_sound = arcade.sound.load_sound("sounds/phaseJump1.wav")
        self.bullet_list = arcade.SpriteList()
        self.bulletSpeed = 5
        self.shotClock = int(round(time.time() * 1000))
        self.shotDelay = 1000


    def update(self, game):
        """
        Description: This function updates the char for the game canvas.
        """
        self.character = arcade.AnimatedWalkingSprite()
        self.all_character_sprites = arcade.SpriteList()
        self.bullet_list.update()

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
        self.bullet_list.draw()

    def shoot(self):
        """
        Description: Shoots a projectile in direction player is facing.
        """
        if len(self.bullet_list) < 5 and (int(round(time.time() * 1000)) - self.shotClock) > self.shotDelay:
            new_bullet = Bullet(self.bulletSpeed, self.center_x, self.center_y)
            self.bullet_list.append(new_bullet)
            self.shotClock = int(round(time.time() * 1000))
        elif (int(round(time.time() * 1000)) - self.shotClock) > self.shotDelay:
            self.bullet_list[0].bulletSpeed = self.bulletSpeed
            self.bullet_list[0].center_x = self.center_x
            self.bullet_list[0].center_y = self.center_y
            self.shotClock = int(round(time.time() * 1000))
        # arcade.sound.play_sound(self.gun_sound)

    def takeDamage(self, damage):
        """
        Description: Reduce health by damage and possibly KO player.
        """
        self.health -= damage

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
