# DELPHINUS - ADVENTURE APP
# CS 467 - Winter 2017
# Team Members: Sara Hashem:, Shawn Hillyer, Niza Volair
#
# language_parser.py
# Description: Class used to parse the language and return relevant components
# Principal Author of this file per Project plan: Niza Volair
#
# CITATIONS
# CITE:
#
# #########################################################################################################
# DEV NOTES:
# 1/22/17:
# The language parser will have to return more than the verb. It will also need to identify the
# subject (feature or object) and appropriate prepositions and such. At a minimum I'd expect the LP to
# return a python dictionary of a verb that's being called and one or more subjects that are trying to
# be interacted. For example "use broom on dusty floor" might return:
#
# {
#     'verb' : 'use',
#     'object' : 'broom',
#     'targets' : [
#         'dusty floor'
#     ]
# }
#
# (SSH)
#
# #########################################################################################################


from stringresources.verbs import *

from debug.debug import *
logger = logging.getLogger(__name__)



class LanguageParser:
    '''
        TODO:

    '''
    def __init__(self):
        logger.debug("Language Parser initialized")


    def parse_command(self, command):
        '''
        Presently returning a constant defined in a stringresources/verbs.py file so that the
        return values from parser can just be set. Thi is Shawn's temporary solution. Later on
        we will need to send more than just the verb back (the subject etc. also needed). See Dev note near file head
        '''


        # Parse any command to all lowercase to reduce complexity of our parser.
        # TODO: Might also want to strip trailing / leading whitespace (but not inner whitespace)
        # l.strip() strips the left-side whitespace, not sure on right side whitespace
        command = command.lower().lstrip()
        object = None
        targets = None

        # Hacky way to parse a "look at" command to find the object/feature player wants to examine.
        # NOTE: Doesn't parse aliases
        if 'look at' in command:
            object = command.replace("look at ", "", 1) # replace "look at " with empty string - rest is the object
            command = "look at"

        # hacky way to parse a 'take' command.
        # NOTE: Doesn't parse aliases
        if 'take' in command:
            object = command.replace("take ", "", 1) # replace at most one instance of "take " with empty str
            command = "take"

        # hacky way to parse a 'drop' command
        # NOTE: Doesn't parse aliases
        if 'drop' in command:
            object = command.replace("drop ", "", 1) # replace at most one instance of "drop " with empty str
            command = "drop"

        # Same thing for go
        if 'go' in command:
            object = command.replace("go ", "", 1)
            command = "go"

        # This simple code just checks if the string entered by user us in one of several Lists defined in the resource
        # file stringresources/verbs.py. Each list is a set of aliases for each verb and it returns a simple string that
        # the gameclient is able to examine.
        # Once this is re-implemented in a stable way, gameclient will need to be reconfigured to properly parse whatever
        # ends up being returned by the parser. -- (SSH)

        if command in QUIT_ALIASES:
            command = QUIT
        elif command in NEW_GAME_ALIASES:
            command = NEW_GAME
        elif command in LOAD_GAME_ALIASES:
            command = LOAD_GAME
        elif command in HELP_ALIASES:
            command = HELP
        elif command in LOOK_ALIASES:
            command = LOOK
        elif command in LOOK_AT_ALIASES:
            command = LOOK_AT
        elif command in GO_ALIASES:
            command = GO
        elif command in TAKE_ALIASES:
            command = TAKE
        elif command in DROP_ALIASES:
            command = DROP
        elif command in INVENTORY_ALIASES:
            command = INVENTORY

        else:
            command = INVALID_INPUT

        logger.debug("Returning: " + str(command) + ", " + str(object) + ", " + str(targets))
        return (command, object, targets)