"""
Program: Mugen Fighting Game
Programmed By: Jared Hall, <insert name>
Description: A simple mugen style fighting game with characters from anime and other fighting games.
Notes:
	1. Pretty much everything should be done with classes. The characters, the screens, everything.
		This allows development to be done concurrently.
"""

#================================IMPORTS=======================================
import arcade

#==============================================================================

#=============================Game Options=====================================
GAME_OPTIONS = {
	"window" : {
		"height" : 500,
		"width" : 1000,
		"name" : "CSC745 M.U.G.E.N Game"
	},
	
	"game" : {
		'brightness' : 50
	}
}
#==============================================================================


class Game(arcade.Window):
	"""
	Description: The main class for the fighting game.
	"""

	def __init__(self):
		"""
		Description: The constructor for the game. Global game setup goes here.
		"""
		super().__init__(GAME_OPTIONS['window']['width'], GAME_OPTIONS['window']['height'], GAME_OPTIONS['window']['name'])
		
		#game setup
		arcade.set_background_color(arcade.color.WHITE)
		self.currentView = 'pregame'
		self.redraw = False
		self.path = '<the path>'
		self.characters = None #sprites for all chars
		self.players = None #sprites for selected char
	
	def setup(self):
		"""
		Description:
		"""
		#load the character classes into a sprites list (1 for each character)
		pass
	
	#-----------------------------------Screens--------------------------------------
	
	def pregameScreen(self):
		"""
		Description: This page displays the main game start page and waits till the user presses the "Enter" key.
		"""
		
		#********DELETE THIS***********
		#i deleted the rest of my base code so that we can load in the actual art assets.
		#This makes a basic logo like what I was talking about yesterday. I left it in here for posterity.
		
		#STEP-01: load the game logo
		box_width = 500
		box_height = 60
		font_size = 30
		x = (GAME_OPTIONS['window']['width'] // 2) - (box_width//2)
		y = (GAME_OPTIONS['window']['height'] / 2) - (box_height//2)
		arcade.draw_lrtb_rectangle_outline(x, x + box_width, y + box_height, y, arcade.color.BLUE, 1)
		arcade.draw_text(GAME_OPTIONS['window']['name'], x, y + (box_height//4), arcade.color.BLACK, font_size, width=box_width, align="center")
		#********************************
		#STEP-02: if user presses the enter key then exit loop.
		
	def mainMenuScreen(self):
		"""
		Description: This is the main menue screen. It should have the logo on top and a list of buttons for the user to press.
		"""
		pass
	
	def loadingScreen(self):
		"""
		Description:
		"""
		pass
	
	def gameOptionsScreen(self):
		"""
		Description:
		"""
		pass
	
	def characterSelectScreen(self):
		"""
		Description:
		"""
		pass
	
	def fightingScreen(self):
		"""
		Description:
		"""
		pass
	
	def trainingScreen(self):
		"""
		Description:
		"""
		pass
	#------------------------------------------------------------------------------------------------
	
	#---------------------------------Game Logic--------------------------------------------------

	def update(self, delta_time):
		"""
		Description: this function updates the current view.
		"""
		pass

	def on_key_press(self, key, key_modifiers):
		"""
		Description: This function is called whenever a key is pressed.	http://arcade.academy/arcade.key.html
		"""
		pass

	def on_key_release(self, key, key_modifiers):
		"""
		Description: This function is called whenever the user lets off a previously pressed key.
		"""
		pass
	
	 def on_mouse_press(self, x, y, button, modifiers):
	 """
	 This function is called when the user presses a mouse button.
	"""
	pass
	
	def on_draw(self):
		"""
		Description: The rendering function.
		"""
		arcade.start_render()
		if(self.redraw == False):
			#first time load the particular screen
			if(self.currentView == 'pregame'):
				self.pregameScreen()
		else:
			#update the current screen (may delete giving screens their own classes is better)
			pass
		

def main():
	Game()
	arcade.run()


if __name__ == "__main__":
	main()