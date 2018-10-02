# BUGEN-Fighter-Game
A M.U.G.E.N. fighting game using The Python Arcade Library as the engine.

Current State of our Game:
1.	Opens to pregame screen
2.	Player selects game mode
  *  Player presses ENTER to go to 2-player game
  *  Player presses TAB to go to training screen (1-Player vs. Thy’s AI)
3.	In Game Controls
  *	Player1 always uses the num-pad (make sure num-lock is on)
    *	8 – jump
    *	4 – move left
    * 6 – move right
    *	5 – block (you take no damage in this state) HOLD DOWN
    *	7 – punch (meele attack – less damage, landing hit gains energy)
    *	9 – blast move (shoots projectile – more damage, consumes energy)
  *.  Player2 uses WASD
    *	W– jump
    *	A – move left
    *	D – move right
    *	S – block (you take no damage in this state) HOLD DOWN
    *	Q – punch (meele attack – less damage, landing hit gains energy)
    *	E – blast move (shoots projectile – more damage, consumes energy)
4.	Game plays until someone reaches 0 health and a victor is decided
5.	Player(s) can then hit enter to return to the pregame screen (back to 1.)
