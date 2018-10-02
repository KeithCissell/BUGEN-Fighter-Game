import arcade
import time

class Bullet(arcade.Sprite):
    def __init__(self, bulletSpeed, center_x, center_y, mirror):
        super().__init__()
        self.texture = arcade.load_texture("characters/blast.png", mirrored=mirror, scale=1.25)
        self.center_x = center_x
        self.center_y = center_y
        self.bulletSpeed = bulletSpeed
        self.damage = 15

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
        self.character = arcade.AnimatedWalkingSprite()
        self.all_character_sprites = arcade.SpriteList()

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

        self.block_texture = arcade.load_texture(character_path + "block.png", scale=1.25)

        self.texture = self.left_stand

        # Player Attributes
        self.movementSpeedX = 7.5
        self.movementSpeedY = 10
        self.delayedMovementX = 0
        self.health = 100
        self.energy = 0
        self.energyMax = 100
        self.direction = "Right"
        self.block = False

        # Punching
        self.punch = False
        self.punchClock = int(round(time.time() * 1000))
        self.punchDuration = 10
        self.punchDelay = 250
        self.punchDamage = 5
        self.punchAnimation = False
        self.punchAnimationDuration = 200

        # Projectile attributes
        self.gun_sound = arcade.sound.load_sound("sounds/laser1.mp3")
        self.hit_sound = arcade.sound.load_sound("sounds/phaseJump1.wav")
        self.bullet_list = arcade.SpriteList()
        self.bulletSpeed = 10
        self.shotClock = int(round(time.time() * 1000))
        self.shotDelay = 1000
        self.shotEnergyCost = 20


    def update(self, game):
        """
        Description: This function updates the char for the game canvas.
        """
        # Check different states
        # Punch
        if self.punch or self.punchAnimation:
            self.change_x = 0
            # Handle Punching flag
            if (int(round(time.time() * 1000)) - self.punchClock) > self.punchDuration:
                self.punch = False
            # Handle Punching Animation
            if (int(round(time.time() * 1000)) - self.punchClock) < self.punchAnimationDuration:
                if self.direction == "Right":
                    self.texture = self.right_punch
                else:
                    self.texture = self.left_punch
            else:
                self.punchAnimation = False
        # Block
        elif self.block == True:
            self.texture = self.block_texture
            self.change_x = 0
        # Regular Movement
        else:
            self.change_x += self.delayedMovementX
            self.delayedMovementX = 0

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

        # Keep player in bounds
        if self.left < 0:
            self.left = 0
        elif self.right > game.gameOptions['window']['width'] - 1:
            self.right = game.gameOptions['window']['width'] - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > game.gameOptions['window']['height'] - 1:
            self.top = game.gameOptions['window']['height'] - 1

        self.bullet_list.update()


    def draw(self):
        """
        Description: This function draws the character.
        """
        super().draw()
        self.bullet_list.draw()

    def changeMoveY(self, change):
        """
        Description: Change movement in y direction
        """
        if not self.block and not self.punch:
            self.change_y = min(self.movementSpeedY, self.change_y + change)

    def changeMoveX(self, change):
        """
        Description: Change movement in x direction
        """
        if self.block or self.punchAnimation:
            self.delayedMovementX += change
            self.change_x = 0
        else:
            self.change_x += change

    def shoot(self):
        """
        Description: Shoots a projectile in direction player is facing.
        """
        if self.energy >= self.shotEnergyCost and (int(round(time.time() * 1000)) - self.shotClock) > self.shotDelay:
            self.energy -= self.shotEnergyCost
            if len(self.bullet_list) < 5:
                if self.direction == "Right":
                    new_bullet = Bullet(self.bulletSpeed, self.center_x, self.center_y, False)
                else:
                    new_bullet = Bullet(-self.bulletSpeed, self.center_x, self.center_y, True)
                self.bullet_list.append(new_bullet)
                self.shotClock = int(round(time.time() * 1000))
            else:
                self.bullet_list[0].bulletSpeed = self.bulletSpeed
                self.bullet_list[0].center_x = self.center_x
                self.bullet_list[0].center_y = self.center_y
                self.shotClock = int(round(time.time() * 1000))
            # arcade.sound.play_sound(self.gun_sound)

    def punchAction(self):
        """
        Description: Make character punch.
        """
        if (int(round(time.time() * 1000)) - self.punchClock) > self.punchDelay:
            self.punch = True
            self.punchAnimation = True
            self.delayedMovementX = self.change_x
            self.punchClock = int(round(time.time() * 1000))

    def takeDamage(self, damage):
        """
        Description: Reduce health by damage and possibly KO player.
        """
        if not self.block:
            self.health = max(0, self.health - damage)

    def gainEnergy(self, energy):
        """
        Description: increse energy.
        """
        self.energy = min(self.energyMax, self.energy + energy)

    def reset(self):
        """
        Description: Resets all player variables.
        """
        # Player Attributes
        self.movementSpeed = 5
        self.health = 100
        self.energy = 0
        self.energyMax = 100
        self.direction = "Right"
        self.block = False

        # Punching
        self.punch = False
        self.punchClock = int(round(time.time() * 1000))
        self.punchDuration = 10
        self.punchDelay = 250
        self.punchDamage = 5

        # Projectile attributes
        self.gun_sound = arcade.sound.load_sound("sounds/laser1.mp3")
        self.hit_sound = arcade.sound.load_sound("sounds/phaseJump1.wav")
        self.bullet_list = arcade.SpriteList()
        self.bulletSpeed = 10
        self.shotClock = int(round(time.time() * 1000))
        self.shotDelay = 1000
        self.shotEnergyCost = 20
