# DELPHINUS - ADVENTURE APP
# CS 467 - Winter 2017
# Team Members: Sara Hashem, Shawn Hillyer, Niza Volair
#
# language_parser.py
# Description: Class used to parse the language and return relevant components
# Principal Author of this file per Project plan: Niza Volair
#
# CITATIONS
# CITE:

from constants.verbs import *
from languageparser.language_parser_wrapper import *
from debug.debug import *
logger = logging.getLogger(__name__)


class LanguageParser:
    def __init__(self):
        # logger.debug("Language Parser initialized")
        pass

    def parse_command(self, verb):
        '''

        :param verb:
        :return:
        '''

        # Parse any command to all lowercase to reduce complexity of our parser.
        # TODO: Might also want to strip trailing whitespace (SSH)
        # l.strip() strips the left-side whitespace, not sure on right side whitespace (SSH)
        verb = verb.lower().lstrip()
        noun = None
        targets = None
        noun_type = 'object'

        # Hacky way to parse a "look at" command to find the verb_subject_name/feature player wants to examine.
        # NOTE: Doesn't parse aliases
        if 'look at' in verb:
            noun = verb.replace("look at ", "", 1) # replace "look at " with empty string - rest is the verb_subject_name
            verb = "look at"

        # hacky way to parse a 'take' command.
        # NOTE: Doesn't parse aliases
        elif 'take' in verb:
            noun = verb.replace("take ", "", 1) # replace at most one instance of "take " with empty str
            verb = "take"

        # hacky way to parse a 'drop' command
        # NOTE: Doesn't parse aliases
        elif 'drop' in verb:
            noun = verb.replace("drop ", "", 1) # replace at most one instance of "drop " with empty str
            verb = "drop"

        # Same thing for go
        elif 'go' in verb:
            noun = verb.replace("go ", "", 1)
            verb = "go"

        elif 'buy' in verb:
            noun = verb.replace("buy ", "", 1)
            verb = "buy"

        elif 'use' in verb:
            noun = verb.replace("use ", "", 1)
            verb = "use"

        elif 'steal' in verb:
            noun = verb.replace("steal ", "", 1)
            verb = "steal"

        elif 'hack' in verb:
            noun = verb.replace("hack ", "", 1)
            verb = "hack"
        # This simple code just checks if the string entered by user us in one of several Lists defined in the resource
        # file constants/verbs.py. Each list is a set of aliases for each verb and it returns a simple string that
        # the gameclient is able to examine.
        # Once this is re-implemented in a stable way, gameclient will need to be reconfigured to properly parse whatever
        # ends up being returned by the parser. -- (SSH)

        if verb in QUIT_ALIASES:
            verb = QUIT
            noun = None
        elif verb in NEW_GAME_ALIASES:
            verb = NEW_GAME
            noun = None

        elif verb in LOAD_GAME_ALIASES:
            verb = LOAD_GAME
            noun = None
        elif verb in SAVE_GAME_ALIASES:
            verb = SAVE_GAME
            noun = None
        elif verb in HACK_ALIASES:
            verb = HACK
        elif verb in HELP_ALIASES:
            verb = HELP

        elif verb in LOOK_ALIASES:
            verb = LOOK
            noun = None

        elif verb in LOOK_AT_ALIASES:
            verb = LOOK_AT

        elif verb in GO_ALIASES:
            verb = GO
            noun_type = 'destination'

        elif verb in TAKE_ALIASES:
            verb = TAKE

        elif verb in DROP_ALIASES:
            verb = DROP

        elif verb in INVENTORY_ALIASES:
            verb = INVENTORY
            noun = None

        elif verb in BUY_ALIASES:
            verb = BUY

        elif verb in USE_ALIASES:
            verb = USE

        elif verb in SPRAYPAINT_ALIASES:
            verb = SPRAYPAINT

        elif verb in STEAL_ALIASES:
            verb = STEAL

        # cheat codes
        elif verb == "mess with the best":
            verb = CHEATCODE_LOSE
            noun = None

        elif verb == "die like the rest":
            verb = CHEATCODE_WIN
            noun = None

        else:
            verb = None
            noun = None

        # return (command, subject, targets)

        results = LanguageParserWrapper()
        results.set_verb(str(verb))
        if noun is None:
            results.noun = {'name': None, 'type': None }
        else:
            results.set_noun(str(noun), noun_type)
        results.extras = None
        results.preposition = None
        results.error_message = None

        # logger.debug("Returning: \n" + str(results))
        return results