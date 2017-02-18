# DELPHINUS - ADVENTURE APP
# CS 467 - Winter 2017
# Team Members: Sara Hashem, Shawn Hillyer, Niza Volair
#
# language_words.py
# Description:  Used by language parser - possibly a temporary solution to parsing the commands.
# Principal Author of this file per Project plan: Shawn Hillyer (Shawn conceived this to help in developing the language
#  parser enough to implement the game engine)
#
# CITATIONS
# CITE: None
#Additions of subjects & prepositions add to language parser functionality, though they don't do much for the file name -NV
#Added directions as well -NV
DESTINATIONS = [
    #cardinal directions
    'north', 'south', 'east', 'west',
    # room names
    # TODO: Update language parser to allow multi-word destinations to be typed in alone and still move player ('county jail' for example is unrecognized command)
    # 'street', 'subway', 'arcade', 'pawn shop', 'evilCorp bank', 'county jail', 'hall', 'office', '"pool" on the roof', 'your computer', 'inside the metaverse', 'chat room', 'evil computer', 'secret files', 'virus room', 'actual pool on the roof'
]


#subjects- objects and features
#objects and aliases
CASH_CRISP = 'crisp cash'
CASH_CRISP_ALIASES = ['crisp cash', 'crisp', 'crisp money'] 
CASH_WAD = 'cash wad'
CASH_WAD_ALIASES = ['cash wad', 'wad of cash', 'wad of money', 'money wad']
SKATEBOARD = 'skateboard'
SKATEBORD_ALIASES = ['skateboard', 'board', 'plank']
HACKER_MANUAL = 'hacker manual'
HACKER_MANUAL_ALIASES = ['hacker manual']
HACKERSNACKS = 'hackersnacks'
HACKERSNACKS_ALIASES = ['hackersnacks', 'snacks', 'munchies']
SURGE = 'surge'
SURGE_ALIASES = ['surge', 'soda', 'drink', 'beverage'] 
SPRAY_PAINT = 'spray paint'
SPRAY_PAINT_ALIASES = ['spray paint', 'can of spray paint', 'spray paint can', 'paint can']
FLOPPY_DISK = 'floppy disk'
FLOPPY_DISK_ALIASES = ['floppy disk', 'floppy', 'disk']
GRAPHICS_CARD = 'graphics card'
GRAPHICS_CARD_ALIASES = ['graphics card', 'card', 'graphics']
RAM = 'ram chip'
RAM_ALIASES = ['ram chip', 'random access memory', 'memory', 'chip', 'ram']

OBJECT_ALIASES = [CASH_CRISP_ALIASES , CASH_WAD_ALIASES,  SKATEBORD_ALIASES, HACKERSNACKS_ALIASES, HACKER_MANUAL_ALIASES, SURGE_ALIASES, SPRAY_PAINT_ALIASES, FLOPPY_DISK_ALIASES, GRAPHICS_CARD_ALIASES, RAM_ALIASES]

#features 
#TODO: add aliases, simple 'look at' features and descriptions to ROOMS, then add logic here
R1_F = ['"no skateboarding" sign', 'guardrails', 'traffic lights']
R2_F = ['phone booth', 'trash can', 'turnstiles']
R3_F = ['ramp', 'death to the patriarchy']
R4_F = ['counter', 'shelves', 'store clerk']
R5_F = ['atm', 'money', 'guard']
R6_F = ['your gear', 'unattended police computer', 'police officer', 'unoccupied desk', 'metal door']
R7_F = ['locker', 'teacher', 'fire alarm']
R8_F = ['school-wide intercom mic', 'office computer', 'acid burn', 'clock', 'poster']
R9_F = ['door', 'ledge']
R10_F = ['disk drive', 'panel', 'terminal']
R11_F = ['bug', 'firewall']
R12_F = ['emojis', 'creature', 'acid burn']
R13_F = ['input / output port', 'sentient cpu']
R14_F = ['cat videos from the internet', 'nuclear launch codes']
R15_F = ['binary files', 'corrupted files']
R16_F = ['acid burn', 'diving board', 'windows']

FEATURES = [R1_F, R2_F, R3_F, R4_F, R5_F, R6_F, R7_F, R8_F, R9_F, R10_F, R11_F, R12_F, R13_F, R14_F, R15_F, R16_F]

#propositions
PREPOSITIONS = ['on', 'in', 'onto', 'into', 'below', 'behind', 'above', 'over', 'next to', 'in front of', 'about', 'with']

#verbs
# In alphabetical order
BUY = 'buy'
BUY_ALIASES = ['buy', 'purchase', 'pay for']
CHEATCODE_LOSE = 'lose cheatcode'
CHEATCODE_LOSE_ALIASES = ['cheatcode lose', 'lose cheatcode', 'mess with the best']
CHEATCODE_WIN = 'cheatcode win'
CHEATCODE_WIN_ALIASES = ['cheatcode win', 'win cheatcode', 'die like the rest']
DROP = 'drop'
DROP_ALIASES = ['drop', 'put down', 'let go', 'leave']
GO = 'go'
GO_ALIASES = ['go', 'move', 'walk', 'run']
HACK = 'hack'
HACK_ALIASES = ['hack']
HELP = 'help'
HELP_ALIASES = ['help', 'info', 'information', 'assist', 'assistance']
LOAD_GAME = 'load game'
LOAD_GAME_ALIASES = ['load game', 'loadgame',  'load_game_menu', 'load my game', 'load saved game', 'load old game']
LOOK = 'look'
LOOK_ALIASES = ['look']
LOOK_AT = 'look at'
LOOK_AT_ALIASES = ['look at', 'examine']
TAKE = 'take'
TAKE_ALIASES = ['take', 'pick up', 'grab', 'acquire']
INVENTORY = 'inventory'
INVENTORY_ALIASES = ['inventory', 'backpack', 'bag']
NEW_GAME = 'new game'
NEW_GAME_ALIASES = [ 'new game', 'new', 'newgame', 'new game', 'hacktheplanet', 'hack the planet']
QUIT = 'quit'
QUIT_ALIASES = ['quit', 'exit', 'bye', 'goodbye', 'leave game']
SAVE_GAME = 'save game'
SAVE_GAME_ALIASES = ['save game', 'save', 'savegame', 'save game', 'save_game']
SPRAYPAINT = 'spraypaint'
SPRAYPAINT_ALIASES = ['spraypaint', 'tag', 'spray', 'paint']
STEAL = 'steal'
STEAL_ALIASES = ['steal']
USE = 'use'
USE_ALIASES = ['use']


VERB_ALIASES = [BUY_ALIASES, CHEATCODE_LOSE_ALIASES, CHEATCODE_WIN_ALIASES, DROP_ALIASES, GO_ALIASES, HACK_ALIASES, HELP_ALIASES, LOAD_GAME_ALIASES, LOOK_AT_ALIASES, 
LOOK_ALIASES, TAKE_ALIASES, INVENTORY_ALIASES, NEW_GAME_ALIASES, QUIT_ALIASES, SAVE_GAME_ALIASES, SPRAYPAINT_ALIASES, STEAL_ALIASES, USE_ALIASES]


NEGATIONS = ['not', 'don\'t', 'no']

#Invalid strings
INVALID_INPUT = 'invalid command'
INVALID_EMPTY = 'invalid command: You uh, wanna type with some letters?'
INVALID_EXTRA_VERBS = 'invalid command: please only use one verb at a time, k?'
INVALID_EXTRA_DESTINATIONS = 'invalid command: woah, can be everywhere at once, pick one direction'
INVALID_GO_NO_DESTINATION = 'invalid command: what direction would you like to go?'
INVALID_NO_VERB = 'invalid command: please enter a verb'
INVALID_EXTRA_NOUNS = 'invalid command: woah, there are like 3+ nouns, that is hard to compute, yo.'
INVALID_EXTRA_PREPOSITONS = 'invalid command: please limit yourself to one preposition, if you please'
INVALID_PREPOSITION_NO_NOUN = 'invalid command: uh, what you want to do with that preposition? Noun please'
INVALID_DOUBLE = 'invalid command: no need to repeat the same thing twice- simply your life, yo'
INVALID_SPRAYPAINT_NO_MESSAGE = 'invalid command: what do you want to write with your spraypaint?'
INVALID_NEGATION = 'invalid command: if you don\'t wanna do that what DO you wanna do??'