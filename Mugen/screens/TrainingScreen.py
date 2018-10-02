import arcade

class TrainingScreen():
    """ Class to represent a screen state for the game """

    def __init__(self):
        """ Initialize Screen variables """

    def setup(self, arcade, game, stage, p1, p2):
        """
        Initial setup to prepare the Training Screen
        """
        # Setup Stage
        game.stage = stage
        game.platforms = game.stage.platform_list

        # Setup Players
        game.player1 = p1
        game.player1.reset()
        game.player1.center_x = game.stage.p1_start_y
        game.player1.center_y = game.stage.p1_start_y
        game.player2 = p2
        game.player2.reset()
        game.player2.center_x = game.stage.p2_start_y
        game.player2.center_y = game.stage.p2_start_x

        game.playerPlatform1.append(game.player2)
        game.playerPlatform2.append(game.player1)

        # Setup Physics
        game.physics1 = arcade.PhysicsEnginePlatformer(game.player1, game.platforms, gravity_constant = 0.5)
        game.physics2 = arcade.PhysicsEnginePlatformer(game.player2, game.platforms, gravity_constant = 0.5)

        # Game Over Flag
        self.gameOver = False
        self.winner = ""

        # Set new view state
        game.currentView = game.trainingScreen

    def update(self, arcade, game, delta_time):
        """
        Description: This function is passed the game itself to modify.
        """
        # Check if game is still going
        if game.player1.health > 0 and game.player2.health > 0:
            # PLAYER DIRECTIONS
            if game.player1.get_position()[0] < game.player2.get_position()[0]:
                game.player1.direction = "Right"
                game.player2.direction = "Left"
            else:
                game.player1.direction = "Left"
                game.player2.direction = "Right"
            # PHYSICS
            game.physics1.update()
            game.physics2.update()
            game.stage.update(arcade, game)
            game.player1.update(game)
            game.player2.update(game)

            # CHECK FOR DAMAGE
            # Physical
            if arcade.geometry.check_for_collision(game.player1, game.player2):
                if game.player1.punch and not game.player2.block:
                    game.player2.takeDamage(game.player1.punchDamage)
                    game.player1.gainEnergy(10)
                if game.player2.punch and not game.player1.block:
                    game.player1.takeDamage(game.player2.punchDamage)
                    game.player2.gainEnergy(10)
            # Bullet
            for bullet in game.player1.bullet_list:
                if arcade.geometry.check_for_collision(game.player2, bullet):
                    game.player2.takeDamage(bullet.damage)
                    bullet.kill()
            for bullet in game.player2.bullet_list:
                if arcade.geometry.check_for_collision(game.player1, bullet):
                    game.player1.takeDamage(bullet.damage)
                    bullet.kill()
        # GAME OVER
        # Player 1 Wins
        elif game.player2.health <= 0:
            game.player2.kill()
            self.gameOver = True
            self.winner = "PLAYER 1"

        # Player 2 Wins
        elif game.player1.health <= 0:
            game.player1.kill()
            self.gameOver = True
            self.winner = "PLAYER 2"

    def handleKeyPress(self, arcade, game, key, key_modifiers):
        """
        Description: This function handles key presses.
        """
        if key == arcade.key.NUM_8:
            game.player1.changeMoveY(game.player1.movementSpeedY)
        elif key == arcade.key.NUM_4:
            game.player1.changeMoveX(-game.player1.movementSpeedX)
        elif key == arcade.key.NUM_6:
            game.player1.changeMoveX(game.player1.movementSpeedX)
        elif key == arcade.key.NUM_7:
            game.player1.punchAction()
        elif key == arcade.key.NUM_9:
            game.player1.shoot()
        elif key == arcade.key.NUM_5:
            game.player1.block = True
        elif key == arcade.key.W:
            game.player2.changeMoveY(game.player2.movementSpeedY)
        elif key == arcade.key.A:
            game.player2.changeMoveX(-game.player2.movementSpeedX)
        elif key == arcade.key.D:
            game.player2.changeMoveX(game.player2.movementSpeedX)
        elif key == arcade.key.Q:
            game.player2.punchAction()
        elif key == arcade.key.E:
            game.player2.shoot()
        elif key == arcade.key.S:
            game.player2.block = True
        elif key == arcade.key.ENTER and self.gameOver:
            game.currentView = game.pregameScreen

    def handleKeyRelease(self, arcade, game, key, key_modifiers):
        """
        Description: This function is called whenever the user lets off a previously pressed key.
        """
        if key == arcade.key.NUM_4:
            game.player1.changeMoveX(game.player1.movementSpeedX)
        elif key == arcade.key.NUM_6:
            game.player1.changeMoveX(-game.player1.movementSpeedX)
        elif key == arcade.key.NUM_5:
            game.player1.block = False
        elif key == arcade.key.A:
            game.player2.changeMoveX(game.player2.movementSpeedX)
        elif key == arcade.key.D:
            game.player2.changeMoveX(-game.player2.movementSpeedX)
        elif key == arcade.key.S:
            game.player2.block = False

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
        # Render the text
        arcade.draw_text(f"Player1 Health: {game.player1.health}", 800, 480, arcade.color.BLACK, 14)
        arcade.draw_text(f"Player1 Energy: {game.player1.energy}", 800, 20, arcade.color.BLACK, 14)
        arcade.draw_text(f"Player2 Health: {game.player2.health}", 10, 480, arcade.color.BLACK, 14)
        arcade.draw_text(f"Player2 Energy: {game.player2.energy}", 10, 20, arcade.color.BLACK, 14)
        # Game Over Display
        if self.gameOver:
            arcade.draw_text(text=f"{self.winner} WINS!", start_x=350, start_y=350, color=arcade.color.BLACK, font_size=35, bold=True)
            arcade.draw_text(text=f"Press ENTER to return to menu", start_x=350, start_y=300, color=arcade.color.BLACK, font_size=20, italic=True)
