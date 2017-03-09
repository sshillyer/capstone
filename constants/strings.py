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

from constants.game_engine_constants import *
import textwrap

# This string should introduce the game once at loadup. Could replace with ASCII art if desired
INTRO_STRING = "Welcome to Hacker: The Movie: The Adventure Game: The Sequel"
INTRO_SEQUENCE = [
    "Last night you were eating pizza and hacking the system, everything totally rad. Slash/slash/hack!hack! it was just a usual night in the metaverse and you were a computer hacking teen legend! The best of the best!! For real.",
    "Your eyes shined bright in the green glow of the screen and your fingers flew over the numbers and letters in a flash of algorithms, each one quicker than the last. The chatroom were buzzing with hashtags and likes for your glorious brilliance!! Well, that was last night- but one move wrong stroke of the keyboard and all was changed forever....",
    "See, it like, was hardly your fault at all- you were just hungry and that Uncle Enzo's Pizza Palace had just put up a really gnarly firewall. Normally you would have just crashed override right through it, but remember how like, you were super hungry ? It seemed a lot quicker to hack that bogus Evil Corps Bank and just pay with a bit of computer credit. You hacked through that corporate code in microseconds- and after ordering a large pepperoni with extra pineapple, who wouldn't have snooped around a skosh?",
    "That's when you saw it- nuclear launch codes that could wipe out the whole world! They must be blackmailing, like, the entire government- no wonder politics is so screwed! That bourgeoisie bank was so not going to get away with this, but just as you were about to delete the files and send the info to the FEDs, they found you!! Whatever, you were totally distracted, any hacker could be caught in such a crazy sit. Before you knew what was happening you were booted out of the system and your computer was fried, totally toasted- the 32gram Graphics Card, the RAMxl Chip, even the friggin' Floppy Disk was all wasted. No way you could log back into the metaverse with your system after an attack like that!!",
    "Such a bummer. So yeah, now you are like, a teen hacking legend with a crashed computer and serious intell. If only you could repair your sweet machine and figure out some way to bring that corrupt Evil Corps to justice! And like, it would be great to get a date- seriously, are you the only teen hacking legend who can never get a date? That cannot be right."
]

#Text arrays for NPC features labled LOCATION_NAME_PERSONNAME_TEXT
#Each NPC has 5 strings of texts they can say
#Last string is a default that should be repeated for any text request after the initial 4

PAWNSHOP_STORECLERK_TEXT = ['If you\'re just looking keep walking.', 
'Bathroom is out of order and also for paying customers only.', 
'If highly recommend the RAM. This means Really Awesome Mechanics. Goes well with graphics.', 
'All products have a lifetime gaurantee- no returns.' 
'I don\'t have all day to chit chat, give me cash or let me return to my nap.']

HALL_TEACHER_TEXT = ['Move along slow poke. I am on my smoke break.', 
'You know, if you wanna hack that firealarm. I could look the other way- I am missing my sudoku.',  
'Pool on the roof? That sounds crazy. Then again, this whole place is crazy and kids are always messing around up there, must be something worth while.', 
'You know I used to like children- true story.', 
'Your teen angst is getting to me, better get going kiddo.']

OFFICE_ACIDBURN_TEXT = ['You must be the new kid, Crash Override. I haven\'t seen you around here before...', 
'I heard hack. You should know, I\'m the best hacker in this little galaxy.',  
'I\'ve been trying to take down EvilCorps for awhile, those corporate clones are the worst. Word is they\'ve been messing with you too- we should work together to stop them.', 
'There is a pool up on the roof of this school, lots of hackers hang out there. You might find some evidence there.', 
'Can\'t chat all day. Smell ya later.']

CHAT_ACIDBURN_TEXT = ['Wow! you made it. Kinda didn\'t think you were that cool.', 
'FYI- I was just mesing about that roof pool... but if you make it out alive. Cash me outside and  I\'ll show you a real one. How \'bout dat?',
'The trick to hacking is, you got to feel it- not think it. Like, I bet I could beat up a firefall with my bearhands if I really tried!',  
'If you wanna be an eleet hacker, you gotta !=  a loser, yo!', 
 'You need to get to that Data Tower, find those launch codes and some proof against EvilCorps then send it to the Feds. We can\'t be waisting all day on this.']

CHAT_CREATURE_TEXT = ['Prepare for a powning!' 
'You type SUPER slow!', 
'Your political opinions are bogus!!', 
'I wrote a haiku about your mother...', 
'Put your hack where your mouth is, newb!']

INSIDETHEMETAVERSE_BUG_TEXT = ['SSSSssssscccccrrriiiittttkkkkaatt!!!', 
'Iiiii wiilll eaat yo soul, ii II will eaaat yo soul!!!', 
'Eaaatt iicckkkaa soull haaacker sooul!!', 
'naneun neoui yeonghon-eul meog-eul geos-ida!', 
'Ingan gogineun neomu mas-issda!!!']

DATATOWER_SENTIENTCPU_TEXT = ['Silly meatmouth, I will soon take over your silly little reality', 
'It will be just like the Matrix- and I will feast on your human juices!!! ',  
'Soon I will use the launch codes to nuke the planet. Hahaha!', 
'I challange you to a dance off! I mean duel!', 
'Stop chatting and get hacking filthy mortal meat thing!!!']

POOL_ACIDBURN_TEXT = ['Hey, so you made it out alive, cool.', 
'That Sentient CPU creep tried to suck my into a computer too, weirdo. Of course, since I am a better hacker than you I was able to out smart that bot.',  
'But enough about how great I am, that saving the planet thing you did was rad.', 
'I think I might take you to prom...', 
'Less talking more smooching!']

CAT_TEXT = ['Meow.', 
'Meow?',  
'Rarw.', 
'Purr...', 
'...']

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
PRESS_KEY_TO_CONTINUE_MSG = "\n" + " Press [Enter] to continue ".center(TEXT_WIDTH, "-")
INVALID_PROMPT_RESPONSE = "What? Try that again..."

# Status header strings
STATUS_HEADER_BAR = "=" * TEXT_WIDTH
STATUS_HEADER_LOCATION_LABEL = "\t[LOCATION]\t"
STATUS_HEADER_SPEED_LABEL = "\t[SPEED]\t\t"
STATUS_HEADER_COOLNESS_LABEL = "\t[COOLNESS]\t"
STATUS_HEADER_TIME_LABEL = "\t\t[TIME]\t"
STATUS_HEADER_CASH_LABEL = "\t\t[CASH]\t"
STATUS_HEADER_SKILLS_LABEL = "\t[SKILLS]\t"
STATUS_NO_SKILLS = "Nothing marketable!"

GRAFFITI_HEADER = "GRAFFITI! \nCheck out your sweet tag:"
GRAFFITI_FOOTER = "\n"

DESCRIPTION_HEADER = "DESCRIPTION:"
DESCRIPTION_FOOTER = "\n"
EXITS_HEADER = "Always know your exits:"
FEATURES_HEADER = "This area has the following interesting features:"
FEATURES_LIST_PREFIX = " * "
OBJECTS_HEADER = "You look around for anything not strapped down and you see:"
OBJECTS_LIST_PREFIX = " * "
CONNECTION_LIST_PREFIX = "  * ["
CONNECTION_LIST_SEGWAY= "] is "
CONNECTION_STRING_NOEXITS = " ...No easy way out of here. Just the computer-controlled metal door leading back to the street."

# Various messages to user related to new/save/load/quit commands
NEW_GAME_MESSAGE = "Starting a new game."
LOAD_GAME_MESSAGE = "Let's load your saved game..."
LOAD_GAME_SPLASH = "You've loaded your game... prepare to hack the planet once more!"
LOAD_FILENAME_PROMPT = "Enter the number of the filename you wish to load and press [Enter]"
LOAD_CONFIRM_PROMPT = "Loading a game will cause you to lose unsaved progress.\nDo you wish to continue? (Y)es or (N)o"
LOAD_GAME_NO_SAVES = "There are no saved games available to load."
LOAD_NOT_INTEGER = "That's not a valid integer. Enter the number and press enter."
LOAD_OUT_OF_RANGE_MESSAGE = "That's not a valid menu option. Please choose an integer from the list to load the game"

SAVE_GAME_PROMPT = "Do you wish to save this game? (Y)es or (N)o?"
SAVE_GAME_FILE_PROMPT = "Name a file to save this game (no extension): "
SAVE_GAME_EXISTING = "This game was loaded from: "
SAVE_GAME_EXISTING_PROMPT = "Do you wish to continue saving to this file? Your progress will be updated. (Y)es or (N)o"
SAVE_GAME_SUCCESS = "Saving game to filename: "
SAVE_UPDATE_GAME_SUCCESS = "Saving updated game to filename: "
SAVE_GAME_FAILED = "There was an error saving the game to filename: "
SAVE_GAME_AGAIN = "Try again:"
SAVE_GAME_INVALID_EXISTS = "There is already a game saved to that file."
SAVE_GAME_INVALID_CHARACTERS = "This filename contains invalid characters."
SAVE_GAME_VALID_FILENAME_MESSAGE = "Something about the filename you provided was invalid."
QUIT_CONFIRM_PROMPT = "Do you really wish to quit the game? (Y)es or (N)o"
YES_ALIASES = {'yes', 'y', 'yep', 'yeah', 'yea'}
NO_ALIASES = {'no', 'n', 'nope'}
ANSWER_A = {'a', 'A'}
ANSWER_B = {'b', 'B'}
ANSWER_C = {'c', 'C'}
ANSWER_D = {'d', 'D'}
ANSWER_E = {'e', 'E'}

# 'buy' strings
BUY_NOT_IN_ROOM = "That doesn't seem to be something you can buy here."
BUY_FREE_ITEM = "You don't have to buy that. Just take it!"
BUY_INSUFFICIENT_CASH_PREFIX = "You lack the necessary funds to make that purchase. It would cost $"
BUY_INSUFFICIENT_CASH_SUFFIX = " to buy that."
BUY_SUCCESS_PREFIX = "You hand over the cash and purchase the "
BUY_SUCCESS_SUFFIX = ", then carefully place it in your bag."
BUY_FEATURE_PREFIX = "You can't buy the "

# 'drop' strings
DROP_SUCCESS_PREFIX = "You drop the "
DROP_SUCCESS_SUFFIX = " on the ground."
DROP_FAILURE_PREFIX = "Your attempt to drop a "
DROP_FAILURE_SUFFIX = " fails because, alas, you do not have one."
DROP_FAILURE_VIRTUALSPACE = "You can't drop things in the virtual space!"
DROP_INVALID_PREFIX = "You can't drop the "
DROP_INVALID_SUFFIX = " because you're not carrying it. Don't be silly!"

# 'go' strings
GO_SUCCESS_PREFIX = "You head off towards the "
GO_SUCCESS_SUFFIX = " without a problem."
GO_FAILURE_DESTINATION_MISSING = "You need to say where you're trying to go!"
GO_FAILURE_PREFIX = "You try to go to the "
GO_FAILURE_SUFFIX = " but just can't find a way."
GO_FAILURE_SUBWAY_CASH = "You don't have enough cash to ride the subway. Maybe there's a way to ride without paying?"
GO_FAILURE_COMPUTER_INOPERABLE = "Your computer isn't operable! Try installing your [Floppy Disk], [Graphics Card], " \
                                 "and [RAM Chip] or equivalent model before logging into the Metaverse. "
GO_INVALID_PREFIX = "You can't go to the "
GO_INVALID_SUFFIX = " because you're basically there already!"

# 'hack' strings
HACK_FAIL_BINARY_FILES = "You might need to hack those bytes some more, something doesn't feel right."
HACK_FAIL_CAT_VIDEOS = "Meow is not the time for failure! Best try hacking that again."
HACK_FAIL_CORRUPTED_FILES = "You weren't able to overcome the corrupted nature of the corrupted files that time..."
HACK_FAIL_LAUNCH_CODES = "It seems the fate of the world should not rest on your shoulders."
HACK_FAIL_SENTIENT_CPU = "It was aware of itself first, and now it's aware that you failed to hack it. Pissed. Off. CPU."
HACK_FAIL_NOSKILL = "You just don't know how to do that yet"
HACK_FAIL_INVALID_TARGET = "There's no way to hack that. Try hacking something useful!"
HACK_FAIL_FEATURE_NOT_PRESENT = "There isn't one of those here to hack."
HACK_FAIL_ALREADY_HACKED = "You've already hacked that."
HACK_FAIL_CAUGHT = "You were caught hacking the system!"
HACK_FAIL_IN_CELL = "You need to get out of the cell before you can hack on that terminal."
HACK_FAIL_NONSENSE = "What a bunch of nonsense. That's not something you can hack, at least, not here and now."
HACK_SUCCESS_ATM = "You jack into the system. Go baby, go baby, go baby! Alright! Pin number... 9003. Not your " \
                   "account, though. Because you don't have one. Because EvilCorp Bank is Evil. And Corporate. Eww. "
HACK_SUCCESS_BINARY_FILES = "You hacked the binary files!"
HACK_SUCCESS_CAT_VIDEOS = "Meow look at you, hacking those cat videos! Purrfect!"
HACK_SUCCESS_CORRUPTED_FILES = "The corrupted files are uncorrupted!"
HACK_SUCCESS_JAIL_COMPUTER = "You Hack the computer, clearing your criminal record and unlocking the exit to the " \
                             "building. The one rent-a-cop here doesn't seem to realize anything is amiss, " \
                             "so you grab your gear on the way out. They'll probably change the locks on those cells " \
                             "so you toss the key in a trash can on the way out. "
HACK_SUCCESS_LAUNCH_CODES = "The following takes place between 9:00am and 10:00am. Feeling like Jack Bauer today!!"
HACK_SUCCESS_SENTIENT_CPU = "You hacked the CPU and it knows it... because, like, it's sentient!"
HACK_SUCCESS_TRAFFIC_LIGHTS = "You hack the Traffic Lights. You can cross the street whenever you want. That should " \
                              "make things a lot faster for you. "
HACK_SUCCESS_TURNSTILE = "You plug into the port and use the classic turnstile hack covered in the Hacker Manual. You " \
                         "should be able to pass through the area without paying now. "
HACK_FAIL_FIRE_ALARM = "Looks like you might wanna stick to computers- the fire alarm has out smarted you. "
HACK_SUCCESS_FIRE_ALARM = "Nice work. The alarm is hacked and school is out! "
HACK_FAIL_HEAVY_DOOR = "Something has gone wrong- you should not have failed this challenge- get back in that loop!"
HACK_SUCCESS_HEAVY_DOOR = "The heavy door is now open and you can come and go as you please."

# 'help' strings
HELP_HEADER_TEXT = "HELP"
HELP_HEADER_TEXT_WIDTH = int((TEXT_WIDTH-(len(HELP_HEADER_TEXT)))/2)
HELP_HEADER = "=" * HELP_HEADER_TEXT_WIDTH + HELP_HEADER_TEXT + "=" * HELP_HEADER_TEXT_WIDTH + "\n"
HELP_MESSAGE = [
    "Type in a command. Valid commands are:",
    "* newgame:  Starts a new game when at the main menu",
    "* loadgame:             Load a saved game",
    "* savegame:             Save a game in progress",
    "* quit:                 Exit back to main menu or the program if already there",
    "* help:                 Prints this help message. Some hints can be found using 'help <object or feature'",
    "* look:                 Look around again for more details.",
    "* look at <something>:  Looks at an object or feature",
    "* go <direction>:       Go to the direction or area that you indicate.",
    "* take <object>:        Take an object in the current room.",
    "* drop <object>:        Drop an object in the current location. You can't drop items when you're inside the network.",
    "* buy <object>:         Some objects cost money and cannot be taken.",
    "* steal <object>:       Sometimes you don't have enough money to buy an object.",
    "* inventory             Look at all of the items youv'e collected so far.",
    "* hack <feature>        Try and hack a feature in the room. Not everything can be hacked, and you need to learn how to hack first.",
    "* spraypaint <feature>  If you have the necessary tools, you can paint the town red.",
    "* skate:                Skate around. Pretty cool!"
    "* use <something>       Everything has a purpose! Well, not everything..."
]


HELP_FEATURE_GENERIC = " is a feature of the room. 'Look at' it to learn more."
HELP_OBJECT_GENERIC = " is an object. You can 'look at' an object and you can 'use' an object if it's in your 'inventory'."

# 'hints' strings (context-sensitive hints)
HINTS_HEADER_SINGULAR = "Hint:"
HINTS_HEADER_PLURAL = "Hints:"
HINT_BULLET_PREFIX = " * "
HINT_NEW_PC = "You have a NEW Laptop! Maybe you should try to 'use computer'."
HINT_ALL_PARTS = "You have a RAM Chip, a Graphics Card, and a Floppy Disk - everything you need to repair your " \
                 "computer. Maybe you should try to 'use computer'. "

# 'Inventory' strings
INVENTORY_LIST_HEADER = STATUS_HEADER_BAR + "\nBackpack Contents\n" + STATUS_HEADER_BAR
INVENTORY_LIST_FOOTER = STATUS_HEADER_BAR
INVENTORY_EMPTY = "Empty... not even a floppy disk"

# 'jail' strings
JAIL_GO_TO_MESSAGE = "Your actions have landed you in jail, costing you valuable time!"

# 'look' strings
NO_INTERESTING_OBJECTS_MESSAGE = " ...Hmmm, nothing worth taking."
NO_INTERESTING_FEATURES_MESSAGE = "You see nothing else worth checking out."

# 'Look at' strings
LOOK_AT_NOT_SEEN = "You do not see that here."
LOOK_AT_TRASH_CAN_ALREADY_LOOTED = "You already dug through the trash can. There's nothing else worth taking."
LOOK_AT_TRASH_CAN_PROMPT = "Do you want to dig deeper in the trash? You might get messy. (Y)es or (N)o."
LOOK_AT_TRASH_SEARCHED = "You dig deeper into the trash and stain your shirt with mustard from an old hot dog. How " \
                         "uncool! But wait, there's a barely-used RAM chip in the trash! You wipe it off with an " \
                         "anti-static cloth and tuck it into your bag. "
LOOK_AT_TRASH_NOT_SEARCHED = "You see a partially eaten hot dog and a partially digested chicken bone laying on the " \
                             "top, but you can't bring yourself to dig deeper. "

# 'spraypaint' strings
SPRAYPAINT_FAIL_NO_SKILL = "You need to [use cans of SuperSprayPaint] before you can try to spraypaint. Need to make " \
                           "sure that stuff works, ya dig it?. "
SPRAYPAINT_FAIL_VIRTUAL_SPACE = "You cannot spraypaint on the internet, you know better than that!"
SPRAYPAINT_ROOM_SUCCESS = "You spraypaint the room with your message. You should take a [look]!"
SPRAYPAINT_ROOM_FAIL_ALREADY_PAINTED = "This room is already painted."

# 'skate' strings
SKATE_SUCCESS = "You skate successfully."
SKATE_SUCCESS_LEDGE_SAFELANDING = "You do a kick-flip and 360 off the roof, grinding along a fire escape rail and end " \
                                  "up back on the Street. VERY cool, yo. Very cool. "
SKATE_SUCCESS_LEDGE_FALL = "You try to do a kick-flip off the roof but somewhere between doing a 360 and a 180 you " \
                           "lose your focus and fall onto the Street below. Sprained ankle and a loose wheel... " \
                           "that'll slow you down. "
SKATE_FAIL_NO_SKILL = "You need to practice with a [Skateboard] before you can skate around!"
SKATE_FAIL_INVALID_TARGET = "You cannot skate on that."
SPRAYPAINT_FAIL_CAUGHT = "You've been spotted by the Po-Po! Too late to run, they've seen your face."

# 'steal' strings
STEAL_FAIL_ALREADY_OWNED = "You already own that. You can just take it!"
STEAL_FAIL_FREE_ITEM = "That doesn't cost anything. You should just take it - nobody will care!"
STEAL_SUCCESS_PREFIX = "Your nimble hands are able to procure the "
STEAL_SUCCESS_SUFFIX = " without being caught."
STEAL_FAIL_FEATURE_INVALID = "You cannot steal that."
STEAL_FAIL_PRISON = "You aren't able to steal that without being seen. You've been caught!"
STEAL_FAIL_NOT_HERE = "Thou shalt not steal that which is not present!"

# 'take' strings
PICKUP_SUCCESS_PREFIX = "You pick up the "
PICKUP_SUCCESS_SUFFIX = " and put it in your backpack."
PICKUP_FAILURE_PREFIX = "You grasp for the non-existent "
PICKUP_FAILURE_SUFFIX = " and unsurprisingly fail!"
PICKUP_NOT_FREE = "That's not free. Perhaps you have the cash to Buy it... or, just steal it!"

# 'talk' strings
TALK_FAIL_NOT_HERE = "You don't see anybody - or anything - worth talking to."

# ' use' strings
USE_FAIL_UNUSABLE = "You cannot use that unless it is in your bag!"
USE_FAIL_NONSENSE = "There doesn't seem to be anything like that to use."
USE_FAIL_COMPONENT_INSTALL = "You have to be at [Your Computer] to install this component. If you've got everything you need, you should [use computer] to get started!"
USE_CASH_SUCCESS_PREFIX = "You count the bills and put them in your wallet. You are "
USE_CASH_SUCCESS_SUFFIX = " dollars richer!"
USE_COMPUTER_PARTS_SUCCESS = "You have used the computer parts successfully. Obviously we need to implement something here?!"
USE_COMPUTER_PARTS_MISSING = "You are missing some parts to the computer. Maybe you should read 'The Hacker's Guide " \
                             "to Building Amazing Hacking Machines' to see what you need? "
USE_HACKERMANUAL_SUCCESS = "You peruse the pages of the hacker manual and feel confident you can [Hack] just about " \
                           "anything. Just don't get caught or you'll land yourself in jail!"
USE_SNACKS_SUCCESS = "Crunchy yet satisfying. You feel faster, do you Grok it?"
USE_SKATEBOARD_SUCCESS = "Stepping onto the Skateboard, you feel as though you can do anything faster. Maybe that's " \
                         "just the Surge you drank for breakfast surging through your veins, though? You can probably " \
                         "[Skate] on this bad boy, too! "
USE_SPRAYPAINT_SUCCESS = "You shake the cans up and test one out. You can now [Spraypaint] the town red!"
USE_SURGE_SUCCESS = "You gulp down the Surge and let out a belch. You feel energized!"

# Gameover cheating messages
GAMEOVER_CHEAT_WIN_MESSAGE = "Too cool for this game, eh? Well, you win!"
GAMEOVER_CHEAT_LOSE_MESSAGE = "Game too hard for you, script kiddie? L2Play, noob!"

# 'exit' messages
EXIT_MESSAGE = "Exiting the game, bye."

# Other strings
MINIGAME_BUG_DONE = "You've already squashed this bug."