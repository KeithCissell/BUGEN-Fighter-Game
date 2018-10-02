import arcade

class TrainingScreen():
    """ Class to represent a screen state for the game """

    def __init__(self, arcade):
        """ Initialize Screen variables """

    def setup(self, arcade, game):
        """
        Initial setup to prepare the Training Screen
        """
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
        # Check if game is still going
        if game.player1.health > 0 and game.player2.health > 0:
            # PHYSICS
            game.physics1.update()
            game.physics2.update()
            game.physicsP1.update()
            game.physicsP2.update()
            game.stage.update(arcade, game)
            game.player1.update(game)
            game.player2.update(game)

            # CHECK FOR DAMAGE
            # Physical

            # Bullet
            for bullet in game.player1.bullet_list:
                if arcade.geometry.check_for_collision(game.player2, bullet):
                    game.player2.takeDamage(bullet.damage)
                    bullet.kill()
            for bullet in game.player2.bullet_list:
                if arcade.geometry.check_for_collision(game.player1, bullet):
                    game.player1.takeDamage(bullet.damage)
                    bullet.kill()
        else:
            # GAME OVER
            # TO-DO
            pass

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
        elif key == arcade.key.L:
            game.player1.shoot()
        elif key == arcade.key.W:
            game.player2.change_y += game.player2.movementSpeed
        elif key == arcade.key.A:
            game.player2.change_x -= game.player2.movementSpeed
        elif key == arcade.key.D:
            game.player2.change_x = game.player2.movementSpeed
        elif key == arcade.key.E:
            game.player2.shoot()

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
        # Render the text
        arcade.draw_text(f"Player1 Health: {game.player1.health}", 10, 480, arcade.color.BLACK, 14)
        arcade.draw_text(f"Player1 Energy: {game.player1.energy}", 10, 20, arcade.color.BLACK, 14)
        arcade.draw_text(f"Player2 Health: {game.player2.health}", 850, 480, arcade.color.BLACK, 14)
        arcade.draw_text(f"Player2 Energy: {game.player2.energy}", 850, 20, arcade.color.BLACK, 14)
