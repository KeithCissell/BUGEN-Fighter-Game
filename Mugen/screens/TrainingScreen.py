class TrainingScreen():
    """ Class to represent a screen state for the game """

    def __init__(self):
        """ Initialize Screen variables """
        pass

    def setup(self, arcade, game):
        """
        Initial setup to prepare the Training Screen
        """
        # Setup Stag
        game.stage = game.trainingFacility
        game.platforms = game.stage.platform_list

        
        # Setup Players
        game.player1 = game.testChar1
        game.player2 = game.testChar2
        
        
        game.playerPlatform1  =  arcade.SpriteList() 
        game.playerPlatform1.append(game.player2)
        
        game.playerPlatform2  =  arcade.SpriteList() 
        game.playerPlatform2.append(game.player1)
        
        
        # Setup Physics
        game.physics1 = arcade.PhysicsEnginePlatformer(game.player1, game.platforms, gravity_constant = 0.25)
        game.physics2 = arcade.PhysicsEnginePlatformer(game.player2, game.platforms, gravity_constant = 0.25)
        game.physicsP1 = arcade.PhysicsEnginePlatformer(game.player1,game.playerPlatform1 , gravity_constant = 0)
        game.physicsP2 = arcade.PhysicsEnginePlatformer(game.player2,game.playerPlatform2 , gravity_constant = 0)
        #game.physics
        # Set new view state
        game.currentView = game.trainingScreen

    def update(self, arcade, game, delta_time):
        """
        Description: This function is passed the game itself to modify.
        """
        #game.physics.update()
        game.physics1.update()
        game.physics2.update()
        
        game.stage.update(arcade, game)
        game.player1.update(game)
        game.player2.update(game)
        game.physicsP2.update()
        game.physicsP1.update()
        

    def handleKeyPress(self, arcade, game, key, key_modifiers):
        """
        Description: This function handles key presses.
        """
        if key == arcade.key.UP:
            game.player1.change_y = game.player1.movementSpeed
        elif key == arcade.key.DOWN:
            game.player1.change_y = -game.player1.movementSpeed
        elif key == arcade.key.LEFT:
            game.player1.change_x = -game.player1.movementSpeed
        elif key == arcade.key.RIGHT:
            game.player1.change_x = game.player1.movementSpeed
        elif key == arcade.key.W:
            game.player2.change_y = game.player2.movementSpeed
        elif key == arcade.key.S:
            game.player2.change_y = -game.player2.movementSpeed
        elif key == arcade.key.A:
            game.player2.change_x = -game.player2.movementSpeed
        elif key == arcade.key.D:
            game.player2.change_x = game.player2.movementSpeed

    def handleKeyRelease(self, arcade, game, key, key_modifiers):
        """
        Description: This function is called whenever the user lets off a previously pressed key.
        """
        if key == arcade.key.UP or key == arcade.key.DOWN:
            game.player1.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            game.player1.change_x = 0
        elif key == arcade.key.W or key == arcade.key.S:
            game.player2.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            game.player2.change_x = 0

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
