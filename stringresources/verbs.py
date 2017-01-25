# DELPHINUS - ADVENTURE APP
# CS 467 - Winter 2017
# Team Members: Sara Hashem:, Shawn Hillyer, Niza Volair
#
# verbs.py
# Description:  Used by language parser - possibly a temporary solution to parsing the commands.
# Principal Author of this file per Project plan: Shawn Hillyer (Shawn conceived this to help in developing the language
#  parser enough to implement the game engine)
#
# CITATIONS
# CITE: None

######################
# MAIN MENU COMMANDS #
######################

# NEW_GAME
NEW_GAME_ALIASES = { 'newgame', 'new game', "hacktheplanet"}
NEW_GAME = 'new game'

# LOAD_GAME
LOAD_GAME_ALIASES = { 'loadgame', 'load game', 'load_game_menu'}
LOAD_GAME = 'load game'

# QUIT and its aliases
QUIT_ALIASES = { 'quit', 'exit', 'bye'}
QUIT = 'quit'

# SAVE_GAME
SAVE_GAME_ALIASES = [ 'savegame', 'save game', 'save_game']
SAVE_GAME = 'save game'

###############
# OTHER VERBS #
###############

# HELP
HELP_ALIASES = {'help'}
HELP = 'help'

# LOOK
LOOK_ALIASES = {'look'}
LOOK = 'look'

# LOOK AT
LOOK_AT_ALIASES = {'look at', 'examine'}
LOOK_AT = 'look at'

# TAKE
TAKE_ALIASES = {'take', 'pick up'}
TAKE = 'take'

# DROP
DROP_ALIASES = {'drop', 'put down', 'let go'}
DROP = 'drop'

# INVENTORY
INVENTORY_ALIASES = {'inventory', 'backpack', 'bag'}
INVENTORY = 'inventory'

# GO
GO_ALIASES = {'go'}
GO = "go"


INVALID_INPUT = 'invalid command'