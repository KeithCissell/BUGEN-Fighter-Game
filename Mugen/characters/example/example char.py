class example(arcade.Sprite)::
    """ Class to represent a character on the screen """

    def __init__(self):
        """ Initialize our character variables """

        #initialize the char
		#load the sprites into spritelists
		# i.e. self.player_sprite = arcade.Sprite("sprites/character.png", SPRITE_SCALING_PLAYER)
		#load character sounds
		#load caracter effects
		
	def update(self):
		"""
		Description: This function updates the char for the game canvas.
		"""
		pass

    def draw(self):
       """
	   Description: This function draws the character.
	   """
	   pass

	def move(self):
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