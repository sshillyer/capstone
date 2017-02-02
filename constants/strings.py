# DELPHINUS - ADVENTURE APP
# CS 467 - Winter 2017
# Team Members: Sara Hashem, Shawn Hillyer, Niza Volair
#
# strings.py
# Description:  Used by game engine
# Principal Author of this file per Project plan: Shawn Hillyer
#
# CITATIONS
# CITE: Used a similar concept as seen in Android app development. Android uses an XML format; I just am localizing all
# of the strings here to one file so we can easily modify things without having to dig through code to find strings (SSH)
# CITE: Also this is similar to how our assembly programs stored strings in one spot and just referenced by name later


# This string should introduce the game once at loadup. Could replace with ASCII art if desired
INTRO_STRING = "Welcome to Hacker: The Movie: The Adventure Game: The Sequel"
DEFAULT_ROOM = "Street"

INVALID_MENU_COMMAND_MESSAGE = " is not a valid command at the main menu"
COMMAND_NOT_UNDERSTOOD = "What?! How dare you say that to me!"

# main menu related strings
MAIN_MENU_1 = "MAIN MENU"
MAIN_MENU_2 = "newgame :: \tbegin a new game"
MAIN_MENU_3 = "loadgame:: \tload game from save"
MAIN_MENU_4 = "quit :: \texit game"
MAIN_MENU_5 = "help :: \tPrint instructions for the game"
MAIN_MENU_LINES = [
    MAIN_MENU_1,
    MAIN_MENU_2,
    MAIN_MENU_3,
    MAIN_MENU_4,
    MAIN_MENU_5,
]

# General UI strings
PROMPT_TEXT = ">> "
PRESS_KEY_TO_CONTINUE_MSG = "\n>>>> Press [Enter] to continue. <<<<"
STATUS_HEADER_BAR = "+----------------------------------------------------------------------+"
DESCRIPTION_HEADER = "DESCRIPTION:"
DESCRIPTION_FOOTER = "\n"
EXITS_HEADER = "Always know your way out. You see a few ways to go from here:"
OBJECTS_HEADER = "You see the following interesting items in the area:"
OBJECTS_LIST_PREFIX = "\t* "
CONNECTION_LIST_PREFIX = "\t* ["
CONNECTION_LIST_SEGWAY= "] is "

# Various messages to user related to new/save/load/quit commands
NEW_GAME_MESSAGE = "Starting a new game."
LOAD_GAME_MESSAGE = "Let's load saved game..."
SAVE_GAME_MESSAGE = "This would be a menu to save the game..."
LOAD_CONFIRM_PROMPT = "Loading a game will cause you to lose unsaved progress.\nDo you wish to continue? (Y)es or (N)o"
QUIT_CONFIRM_PROMPT = "Quitting the game will cause you to lose unsaved progress.\nDo you wish to continue? (Y)es or (N)o"
YES_ALIASES = {'yes', 'y'}


# The HELP message
# TODO: Make this a lot more extensive
HELP_MESSAGE_1 = "Here's the information on how to play the game..."
HELP_MESSAGE_2 = "Type in a command. Valid commands are: "
VALID_VERB_LIST = "newgame, loadgame, quit, help, look, look at <verb_object>, go <direction or description>, take <verb_object>, \ndrop <verb_object>, inventory, hack, steal <verb_object>, buy <verb_object>, spraypaint, use <verb_object or feature>\n"
HELP_MESSAGE = [
    HELP_MESSAGE_1,
    HELP_MESSAGE_2,
    VALID_VERB_LIST
]

# 'buy' strings
BUY_NOT_IN_ROOM = "That doesn't seem to be something you can buy here."
BUY_FREE_ITEM = "You don't have to buy that. Just take it!"
BUY_INSUFFICIENT_CASH_PREFIX = "You lack the necessary funds to make that purchase. It would cost $"
BUY_INSUFFICIENT_CASH_SUFFIX = " to buy that."
BUY_SUCCESS_PREFIX = "You hand over the cash and purchase the "
BUY_SUCCESS_SUFFIX = ", then carefully place it in your bag."

# 'drop' strings
DROP_SUCCESS_PREFIX = "You drop the "
DROP_SUCCESS_SUFFIX = " on the ground."
DROP_FAILURE_PREFIX = "Your attempt to drop a "
DROP_FAILURE_SUFFIX = " fails because, alas, you do not have one."
DROP_FAILURE_VIRTUALSPACE = "You can't drop things in the virtual space!"

# 'go' strings
GO_SUCCESS_PREFIX = "You head off towards the "
GO_SUCCESS_SUFFIX = " without a problem."
GO_FAILURE_PREFIX = "You try to go to the "
GO_FAILURE_SUFFIX = " but just can't find a way."

# 'Inventory' related strings
INVENTORY_LIST_HEADER = "========================================================================\nBackpack Contents\n------------------------------------------------------------------------"
INVENTORY_LIST_FOOTER = "========================================================================"
INVENTORY_EMPTY = "Empty... not even a floppy disk"

# 'look' strings
NO_INTERESTING_OBJECTS_MESSAGE = "You see nothing else laying about worth taking."

# 'Look at' strings
LOOK_AT_NOT_SEEN = "You do not see that here."

# 'take' strings
PICKUP_SUCCESS_PREFIX = "You pick up the "
PICKUP_SUCCESS_SUFFIX = " and put it in your backpack."
PICKUP_FAILURE_PREFIX = "You grasp for the non-existent "
PICKUP_FAILURE_SUFFIX = " and unsurprisingly fail!"
PICKUP_NOT_FREE = "That's not free. Perhaps you have the cash to Buy it... or, just steal it!"

# ' use' strings
USE_FAIL = "There's just no way to use that because it's not in your bag!"
USE_CASH_SUCCESS = "You count the bills and put them in your wallet."
USE_COMPUTER_PARTS_SUCCESS = "You have used the computer parts successfully. Obviously we need to implement something here?!"
USE_COMPUTER_PARTS_MISSING = "You are missing some parts to the computer. Maybe you should read 'The Hacker's Guide to Building Amazing Hacking Machines' to see what you need?"
USE_SNACKS_SUCCESS = "Crunchy yet satisfying. You feel faster, do you Grok it?"
USE_SKATEBOARD_SUCCESS = "Stepping onto the Skateboard, you feel as though you can do anything faster. Maybe that's just the Surge you drank for breakfast surging through your veins, though?"
USE_SPRAYPAINT_SUCCESS = "You spend a few moments shaking the Spray Paint and test it out. You can now spraypaint the town red!"
USE_SURGE_SUCCESS = "You gulp down the Surge and let out a belch. You feel energized!"

# Gameover cheating messages
GAMEOVER_CHEAT_WIN_MESSAGE = "Too cool for this game, eh? Well, you win!"
GAMEOVER_CHEAT_LOSE_MESSAGE = "Game too hard for you, script kiddie? L2Play, noob!"

# 'exit' messages
EXIT_MESSAGE = "Exiting the game, bye."
