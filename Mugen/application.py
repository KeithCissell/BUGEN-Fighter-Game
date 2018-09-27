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
from screens.PregameScreen import PregameScreen
from screens.TrainingScreen import TrainingScreen
from characters.test.TestChar import TestChar
# Stages
from stages.TrainingFacility.TrainingFacility import TrainingFacility
from stages.Field.Field import Field
from stages.Guild.Guild import Guild
#==============================================================================

#=============================Game Options=====================================
GAME_OPTIONS = {
	"window" : {
		"height" : 500,
		"width" : 1000,
		"name" : "CSC745 M.U.G.E.N Game"
	},

	"game" : {
		'brightness' : 50,
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
        self.gameOptions = GAME_OPTIONS
        self.currentView = None
        self.redraw = False
        self.path = '<the path>'
        # Stage Atributes
        self.stages = [] # list of all stage classes
        self.platforms = arcade.SpriteList() # holds stage platforms
        self.stage = None # selected stage
        # Player Atributes
        self.characters = arcade.SpriteList() # list of all character classes
        self.player1 = None
        self.player2 = None
        # Game Physics
        self.physics = None

    def setup(self):
        """
        Description: Load in resources and set state to pregame screen
        """
        # Display a loading screen
        box_width = 500
        box_height = 60
        font_size = 30
        x = (self.gameOptions['window']['width'] // 2) - (box_width//2)
        y = (self.gameOptions['window']['height'] / 2) - (box_height//2)
        arcade.draw_lrtb_rectangle_outline(x, x + box_width, y + box_height, y, arcade.color.BLUE, 1)
        arcade.draw_text("LOADING...", x, y + (box_height//4), arcade.color.BLACK, font_size, width=box_width, align="center")

        # LOAD GAME SCREENS
        self.pregameScreen = PregameScreen()
        # self.mainMenuScreen = MainMenuScreen()
        # self.loadingScreen = LoadingScreen()
        # self.gameOptionsScreen = GameOptionsScreen()
        # self.characterSelectScreen = CharacterSelectScreen()
        # self.fightingScreen = FightingScreen()
        self.trainingScreen = TrainingScreen()

        # LOAD CHARACTERS
        self.testChar = TestChar()
        self.characters.append(self.testChar)

        # LOAD STAGES
        self.trainingFacility = TrainingFacility()
        self.stages.append(self.trainingFacility)
        self.field = Field()
        self.stages.append(self.field)
        self.guild = Guild()
        self.stages.append(self.guild)

        # Set game state to PregameScreen
        self.currentView = self.pregameScreen

	#---------------------------------Game Logic--------------------------------------------------

    def update(self, delta_time):
        """
        Description: this function updates the current view.
        """
        self.currentView.update(arcade, self, delta_time)

    def on_key_press(self, key, key_modifiers):
        """
        Description: This function is called whenever a key is pressed.	http://arcade.academy/arcade.key.html
        """
        self.currentView.handleKeyPress(arcade, self, key, key_modifiers)

    def on_key_release(self, key, key_modifiers):
        """
        Description: This function is called whenever the user lets off a previously pressed key.
        """
        self.currentView.handleKeyRelease(arcade, self, key, key_modifiers)

    def on_mouse_press(self, x, y, button, modifiers):
        """
        This function is called when the user presses a mouse button.
        """
        self.currentView.handleMousePress(arcade, self, x, y, button, modifiers)

    def on_draw(self):
        """
        Description: The rendering function.
        """
        arcade.start_render()
        self.currentView.draw(arcade, self)


def main():
    window = Game()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
