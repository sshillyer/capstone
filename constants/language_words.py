# DELPHINUS - ADVENTURE APP
# CS 467 - Winter 2017
# Team Members: Sara Hashem, Shawn Hillyer, Niza Volair
#
# language_words.py
# Description:  Used by language parser - possibly a temporary solution to parsing the commands.
# Principal Author of this file per Project plan: Niza Volair 
# Note: Shawn conceived this to help in developing the language parser enough to implement the game engine)
#
# CITATIONS
# CITE: None

#room destininations and aliases
R1 = ['street']
R2 = ['evilcorp bank', 'evil corp', 'evil bank', 'evilcorp', 'bank']
R3 = ['arcade']
R4 = ['pawn shop', 'pawn', 'shop']
R5 = ['subway', 'metro', 'underground']
R7 = ['jail', 'prison', 'slammer']
R6 = ['pool on the roof', 'roof pool', 'pool', 'roof']
R8 = ['hall', 'hallway']
R9 = ['school office']
R10 = ['your computer']
R11 = ['inside the metaverse', 'metaverse', 'internet']
R12 = ['chat room', 'chat']
R13 = ['data tower', 'data', 'tower']
R14 = ['encrypted files', 'encrypted', 'encrypt']
R15 = ['spaghetti code', 'spaghetti', 'spagett']
#no room 16 as player will be sent automatically if they win

#destinations include directions and room names
DESTINATIONS = [['north'], ['south'], ['east'], ['west'], R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15]

#subjects- objects and features
#objects and aliases
ORANGE_CAT = 'orange cat'
ORANGE_CAT_ALIASES = ['orange cat', 'gogi']
CASH_CRISP = 'crisp cash'
CASH_CRISP_ALIASES = ['crisp cash', 'crisp', 'crisp money'] 
CASH_WAD = 'cash wad'
CASH_WAD_ALIASES = ['cash wad', 'wad of cash', 'wad of money', 'money wad', 'wad']
CODE = 'code'
CODE_ALIASES = ['code']
COMPUTER = 'computer'
COMPUTER_ALIASES = ['computer']
SKATEBOARD = 'skateboard'
SKATEBORD_ALIASES = ['skateboard', 'board', 'plank']
HACKER_MANUAL = 'hacker manual'
HACKER_MANUAL_ALIASES = ['hacker manual', 'manual']
HACKERSNACKS = 'hackersnacks'
HACKERSNACKS_ALIASES = ['hackersnacks', 'snacks', 'munchies']
SURGE = 'surge'
SURGE_ALIASES = ['surge', 'soda', 'drink', 'beverage'] 
SPRAY_PAINT = 'cans of superspraypaint'
SPRAY_PAINT_ALIASES = ['cans of superspraypaint', 'superspraypaint', 'cans']
FLOPPY_DISK = 'floppy disk'
FLOPPY_DISK_ALIASES = ['floppy disk', 'floppydisk', 'floppy']
GRAPHICS_CARD = 'graphics card'
GRAPHICS_CARD_ALIASES = ['graphics card', 'graphic card', 'graphicscard', 'graphiccard', 'card', 'graphics']
NEW_LAPTOP = 'new laptop'
NEW_LAPTOP_ALIASES = ['new laptop', 'laptop']
RAM = 'ram chip'
RAM_ALIASES = ['ram chip', 'random access memory', 'memory', 'chip', 'ram']
ACMERAM = 'acmeram'
ACMERAM_ALIASES = ['acmeram', 'acme']
KEY= 'key'
KEY_ALIASES = ['key', 'jailkey', 'cellkey' ]
FIREBALL = 'fireball'
FIREBALL_ALIASES = ['fireball', 'ball']
CARCASS = 'carcass'
CARCASS_ALIASES = ['carcass']
CPUHEAD = 'cpu head'
CPUHEAD_ALIASES = ['cpu head', 'head']
BINARY_STRING = 'binary string'
BINARY_STRING_ALIASES = ['binary string', 'string']
LOCK_PICKS = "lock picks"
LOCK_PICKS_ALIASES = ['lock picks']

OBJECT_ALIASES = [ORANGE_CAT_ALIASES, CASH_CRISP_ALIASES , CASH_WAD_ALIASES, CODE_ALIASES, COMPUTER_ALIASES, SKATEBORD_ALIASES, HACKERSNACKS_ALIASES, HACKER_MANUAL_ALIASES, SURGE_ALIASES, SPRAY_PAINT_ALIASES, FLOPPY_DISK_ALIASES, GRAPHICS_CARD_ALIASES, NEW_LAPTOP_ALIASES, RAM_ALIASES, ACMERAM_ALIASES, KEY_ALIASES, FIREBALL_ALIASES, CARCASS_ALIASES, CPUHEAD_ALIASES, BINARY_STRING_ALIASES, LOCK_PICKS_ALIASES]

#features 
#TODO: add aliases, simple 'look at' features and descriptions to ROOMS, then add logic here
R1_F = [['"no skateboarding" sign', 'no skateboarding sign', 'sign'], ['guardrails', 'rails', 'rail'], ['traffic lights', 'traffic', 'lights', 'light']]
R2_F = [['phone booth', 'phone', 'booth'], ['trash can', 'trash'], ['turnstiles', 'turn stile', 'turn stiles', 'turnstile']]
R3_F = [['ramp'], ['death to the patriarchy', 'game', 'death', 'patriarchy']]
R4_F = [['counter'], ['shelves'], ['store clerk', 'clerk']]
R5_F = [['atm'], ['security officer', 'security']]
R6_F = [['your gear', 'gear'], ['unattended police desktop', 'police desktop'], ['police officer', 'cop'], ['unoccupied desk', 'desk'], ['metal door']]
R7_F = [['locker'], ['teacher', 'teach'], ['fire alarm', 'alarm']]
R8_F = [['school intercom mic', 'intercom mic', 'intercom', 'mic'], ['office desktop'], ['clock'], ['poster']]
R9_F = [['control box', 'control', 'box'], ['heavy door'], ['ledge']]
R10_F = [['disk drive', 'drive'], ['panel'], ['terminal']]
R11_F = [['bug'], ['firewall']]
R12_F = [['emojis', 'emoji', 'emoticons'], ['creature', 'troll'], ['leet translator', 'leet', 'translator']]
R13_F = [['input output port', 'input output port', 'in out port', 'input output', 'in out' 'port'], ['sentient cpu', 'sentient']]
R14_F = [['cat videos from the internet', 'internet cat videos', 'cat videos', 'videos', 'vids'], ['nuclear launch codes', 'nuclear codes', 'codes']]
R15_F = [['binary files', 'binary'], ['corrupted files', 'corrupted']]
R16_F = [['diving board', 'diving'], ['walls']]
R_MULTI = [['acid burn']]

FEATURES_ALIASES_ARRAYS = [R1_F, R2_F, R3_F, R4_F, R5_F, R6_F, R7_F, R8_F, R9_F, R10_F, R11_F, R12_F, R13_F, R14_F, R15_F, R16_F, R_MULTI]

#propositions
PREPOSITIONS = [ 'in front of', 'next to', 'on', 'in', 'inside', 'onto', 'into', 'below', 'behind', 'above', 'over', 'about', 'with', 'around', 'off', 'up']

CHEATCODE_LOSE = 'lose cheatcode'
CHEATCODE_LOSE_ALIASES = ['cheatcode lose', 'mess with the best', 'lose cheatcode']
CHEATCODE_WIN = 'cheatcode win'
CHEATCODE_WIN_ALIASES = ['cheatcode win', 'die like the rest', 'win cheatcode']

#verbs
# In alphabetical order
BUY = 'buy'
BUY_ALIASES = ['buy', 'pay for', 'purchase']
DROP = 'drop'
DROP_ALIASES = ['drop', 'put down', 'let go', 'leave']
GO = 'go'
GO_ALIASES = ['go', 'move', 'walk', 'run']
HACK = 'hack'
HACK_ALIASES = ['hack']
HELP = 'help'
HELP_ALIASES = ['help', 'information', 'assistance', 'assist', 'info']
LOAD_GAME = 'load game'
LOAD_GAME_ALIASES = ['load game', 'load my game', 'load saved game', 'load old game', 'loadgame']
LOOK = 'look'
LOOK_ALIASES = ['look']
LOOK_AT = 'look at'
LOOK_AT_ALIASES = ['look at', 'examine']
TAKE = 'take'
TAKE_ALIASES = ['take', 'pick up', 'grab', 'acquire']
TALK = 'talk'
TALK_ALIASES = ['talk', 'speak', 'ask']
INVENTORY = 'inventory'
INVENTORY_ALIASES = ['inventory', 'backpack', 'bag']
NEW_GAME = 'new game'
NEW_GAME_ALIASES = [ 'new game', 'hack the planet', 'new game', 'hacktheplanet', 'newgame']
QUIT = 'quit'
QUIT_ALIASES = ['quit', 'leave game', 'exit', 'bye', 'goodbye']
SAVE_GAME = 'save game'
SAVE_GAME_ALIASES = ['save game', 'save game', 'savegame', 'save']
SKATE = 'skate'
SKATE_ALIASES = ['skate', 'ride skateboard']
SPRAYPAINT = 'spray paint'
SPRAYPAINT_ALIASES = ['spray paint', 'spraypaint', 'spray', 'paint', 'tag']
STEAL = 'steal'
STEAL_ALIASES = ['steal']
USE = 'use'
USE_ALIASES = ['use']



VERB_ALIASES = [BUY_ALIASES, DROP_ALIASES, GO_ALIASES, HACK_ALIASES, HELP_ALIASES, LOAD_GAME_ALIASES, LOOK_AT_ALIASES, 
LOOK_ALIASES, TAKE_ALIASES, TALK_ALIASES, INVENTORY_ALIASES, NEW_GAME_ALIASES, QUIT_ALIASES, SAVE_GAME_ALIASES, SKATE_ALIASES, SPRAYPAINT_ALIASES, STEAL_ALIASES, USE_ALIASES]


NEGATIONS = ['not', 'don\'t', 'no']

#Invalid strings
INVALID_INPUT = 'invalid command'
INVALID_EMPTY = 'invalid command: You uh, wanna type with some letters?'
INVALID_EXTRA_VERBS = 'invalid command: please only use one verb at a time, k?'
INVALID_EXTRA_DESTINATIONS = 'invalid command: woah, can be everywhere at once, pick one direction'
INVALID_GO_NO_DESTINATION = 'invalid command: what direction would you like to go?'
INVALID_DESTINATION_WRONG_VERB = 'invalid command: weird verb + destination == i don\'t get it?'
INVALID_NO_VERB = 'invalid command: please enter a verb'
INVALID_EXTRA_NOUNS = 'invalid command: woah, there are like 3+ nouns, that is hard to compute, yo.'
INVALID_EXTRA_PREPOSITONS = 'invalid command: please limit yourself to one preposition, if you please'
INVALID_PREPOSITION_NO_NOUN = 'invalid command: uh, what you want to do with that preposition? Noun please'
INVALID_DOUBLE = 'invalid command: no need to repeat the same thing twice- simply your life, yo'
INVALID_SPRAYPAINT_NO_MESSAGE = 'invalid command: what do you want to write with your spraypaint?'
INVALID_NEGATION = 'invalid command: if you don\'t wanna do that what DO you wanna do??'
INVALID_SENTENCE_STRUCTURE = 'invalid command: you made a weird sentence. Try verb-noun yo.'