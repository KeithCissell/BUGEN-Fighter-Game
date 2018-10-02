import arcade
BULLET_SPEED = 5


class Bullet(arcade.Sprite):
    def update(self):
        self.center_y += BULLET_SPEED

class TrainingScreen():
    """ Class to represent a screen state for the game """

    def __init__(self, arcade):
        """ Initialize Screen variables """
        self.gun_sound = arcade.sound.load_sound("sounds/laser1.mp3")
        self.hit_sound = arcade.sound.load_sound("sounds/phaseJump1.wav")
        self.bullet_list = None
        self.player_list = None
        self.score1 = 0
        self.score2 = 0


    def setup(self, arcade, game):
        """
        Initial setup to prepare the Training Screen
        """
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        # Set up the players scores
        self.score1 = 0
        self.score2 = 0

        # Setup Stage
        game.stage = game.guild
        game.platforms = game.stage.platform_list

        # Setup Players
        game.player1 = game.goku
        game.player1.center_x = 50 #game.stage.p1_start_y
        game.player1.center_y = 100 #game.stage.p1_start_y
        game.player2 = game.goku2
        game.player2.center_x = 450 #game.stage.p2_start_y
        game.player2.center_y = 100 #game.stage.p2_start_y

        self.player_list.append(game.player1)
        self.player_list.append(game.player2)

        game.playerPlatform1.append(game.player2)
        game.playerPlatform2.append(game.player1)

        # Setup Physics
        game.physics1 = arcade.PhysicsEnginePlatformer(game.player1, game.platforms, gravity_constant = 0.25)
        game.physics2 = arcade.PhysicsEnginePlatformer(game.player2, game.platforms, gravity_constant = 0.25)
        game.physicsP1 = arcade.PhysicsEnginePlatformer(game.player1, game.playerPlatform1, gravity_constant = 0.0)
        game.physicsP2 = arcade.PhysicsEnginePlatformer(game.player1, game.playerPlatform2, gravity_constant = 0.0)

        # Set new view state
        game.currentView = game.trainingScreen

    def update(self, arcade, game, delta_time):
        """
        Description: This function is passed the game itself to modify.
        """
        game.physics1.update()
        game.physics2.update()
        game.physicsP1.update()
        game.physicsP2.update()
        game.stage.update(arcade, game)
        game.player1.update(game)
        game.player2.update(game)

    def handleKeyPress(self, arcade, game, key, key_modifiers):
        """
        Description: This function handles key presses.
        """
        if key == arcade.key.UP:
            game.player1.change_y += game.player1.movementSpeed
        elif key == arcade.key.LEFT:
            game.player1.change_x -= game.player1.movementSpeed
        elif key == arcade.key.RIGHT:
            game.player1.change_x += game.player1.movementSpeed
        elif key == arcade.key.W:
            game.player2.change_y += game.player2.movementSpeed
        elif key == arcade.key.A:
            game.player2.change_x -= game.player2.movementSpeed
        elif key == arcade.key.D:
            game.player2.change_x = game.player2.movementSpeed
        elif key == arcade.key.E:
            # Gunshot sound
            arcade.sound.play_sound(self.gun_sound)
            # Create a bullet
            bullet1 = Bullet("images/ball.jpg", 0.1)
            bullet1.angle = 90
            # Position the bullet
            bullet1.center_x = game.player2.center_x
            bullet1.bottom = game.player2.top

            ## Add the bullet to the appropriate lists
            self.bullet_list.append(bullet1)
        elif key == arcade.key.L:
            # Gunshot sound
            arcade.sound.play_sound(self.gun_sound)
            # Create a bullet
            bullet2 = Bullet("images/ball.jpg", 0.1)
            bullet2.angle = 90
            # Position the bullet
            bullet2.center_x = game.player1.center_x
            bullet2.bottom = game.player2.top
            self.bullet_list.append(bullet2)

    def handleKeyRelease(self, arcade, game, key, key_modifiers):
        """
        Description: This function is called whenever the user lets off a previously pressed key.
        """
        if key == arcade.key.LEFT:
            game.player1.change_x += game.player1.movementSpeed
        elif key == arcade.key.RIGHT:
            game.player1.change_x -= game.player1.movementSpeed
        elif key == arcade.key.A:
            game.player2.change_x += game.player2.movementSpeed
        elif key == arcade.key.D:
            game.player2.change_x -= game.player2.movementSpeed

    def handleMousePress(self, arcade, game, x, y, button, modifiers):
        """
        This function is called when the user presses a mouse button.
        """
        pass

    def draw(self, arcade, game):
        """
        Description: The rendering function.
        """
        game.stage.draw(arcade, game)
        game.player1.draw()
        game.player2.draw()
        self.bullet_list.draw()
        # Render the text
        arcade.draw_text(f"Player1 Score: {self.score1}", 10, 20, arcade.color.BLACK, 14)
        arcade.draw_text(f"Player2 Score: {self.score2}", 850, 20, arcade.color.BLACK, 14)
