# DELPHINUS - ADVENTURE APP
# CS 467 - Winter 2017
# Team Members: Sara Hashem:, Shawn Hillyer, Niza Volair

# game_client.py
# Description: GameClient class and closely-related classes
# Principal Author of this file per Project plan: Shawn Hillyer

# CITATIONS
# CITE:


from languageparser.language_parser import LanguageParser
from fileio.room_builder import RoomBuilder
from stringresources.strings import *
from stringresources.verbs import *
from stringresources.status_codes import *

from debug.debug import *
logger = logging.getLogger(__name__)


class GameClient:
    '''
    Main controller for the game's flow and logic
    '''
    def __init__(self):
        self.gamestate = GameState()
        self.gamestate.load_rooms_from_files()

        # Instantiate unenforced singleton-style instances of various components
        self.ui = UserInterface()
        self.lp = LanguageParser()
        self.rb = RoomBuilder()

        # Variables used to store GameClient state
        self.user_input = ""
        self.command = INVALID_INPUT
        self.valid_main_menu_commands = { QUIT, LOAD_GAME, NEW_GAME , HELP }

        # Initiate main loop upon instantiation, as it should only ever be called once
        self.main_loop()

    def main_loop(self):
        '''
        Comments outline the flow of project and intended functions for now
        based on game engine workflow graph
        :return: N/A
        '''


        # Load data from files (Specifically rooms, but can do other files as well)
        # Gamestate level details will later be loaded in the main menu loop
        self.gamestate.rooms = self.rb.load_room_data_from_file()

        # Outer loop makes game play until user decides to quit from the main menu
        while self.command is not QUIT:

            # Inner loop runs the main menu and prompts until a valid command is entered
            self.main_menu_loop()

            # After that, we can either initialize a new or loaded game into the GameState using GameClient Methods..
            if self.command is NEW_GAME:
                self.initialize_new_game()
            elif self.command is LOAD_GAME:
                self.load_game_menu()
            # Or exit the game...
            elif self.command is QUIT:
                print(EXIT_MESSAGE)
                sys.exit()
            # Or print the help menu
            elif self.command is HELP:
                self.ui.print_help_message()
            # If the command was invalid, an error message will display and later on the command and input is cleared
            else:
                print(INVALID_MENU_COMMAND_MESSAGE)


            # ONLY IF Player decided to play the game, gamestate has already been initialized in the if/else above
            if self.command is NEW_GAME or self.command is LOAD_GAME:
                # Actually playing the game will eventually terminate for one of the below reasons
                # We handle each case separately because if a player forfeits and does not save,
                # it can have different logic than if they quit and save, etc.
                # The constants are defined in stringresources\status_codes.py
                exit_code = self.play_game()
                if exit_code is GAMEOVER_FORFEIT:
                    print("Game over: Forfeit")
                elif exit_code is GAMEOVER_WIN:
                    print("Game over: Player won")
                elif exit_code is GAMEOVER_LOSE:
                    print("Game over: Player lost")
                elif exit_code is GAMEOVER_SAVE:
                    print("Game over: Player saved game")
                elif exit_code is GAMEOVER_LOAD:
                    print("Game over: Player loading game")
                    self.load_game_menu()

            # Set these back to default values to ensure we don't enter endless loop
            self.command = INVALID_INPUT
            self.user_input = ""

    def main_menu_loop(self):
        '''
        Prints the main menu and sets self.command until command is set to a proper value
        :return: indirectly - sets instance variable, self.command, to a valid command
        '''
        firstPass = True
        while not self.is_valid_menu_command(self. command):
            if firstPass:
                firstPass = False
            else:
                logger.debug(self.command + " : " + self.user_input)
            self.main_menu_prompt()
            self.command, self.object, self.targets = self.lp.parse_command(self.user_input)



    def main_menu_prompt(self):
        '''
        Prints the main menu then prompts the user for input one time
        :return: Indirectly - sets instance variable user_input to the string typed by user
        '''
        self.ui.print_main_menu()
        self.user_input = self.ui.user_prompt()

    def is_valid_menu_command(self, command):
        '''
        Checks the command returned from language parser against a list of valid menu commands defined on the
        GameClient class (which are in term constants defined in stringresources\verbs.py)
        :param command: A constant defined in stringresources\verbs.py
        :return: True or false depending on presence of the command in the list of valid commands
        '''
        if command in self.valid_main_menu_commands:
            return True
        else:
            return False



    def play_game(self):
        '''
        Primary game loop that prints information to user, reads input, and reacts accordingly
        :return: a status code as defined in stringresources\status_codes.py, used by gameclient to determine how
        and/or why game ended.
        '''

        print(NEW_GAME_MESSAGE)         # Defined in stringresources\strings.py

        status = GAME_CONTINUE          # Force entry into main loop

        print_long_description = False  # Override  if user just typed the 'look' command

        # Game will loop until a 'Gameover' condition is met
        while status is GAME_CONTINUE:
            # Check game status; if Gameover, leave game loop and return status code
            status = self.game_status()
            if status in GAMEOVER_STATES:  # list as defined in stringresources\status_codes.py
                return status


            # Print appropriate Room description. Long if room never visited or player used "look" command
            if self.gamestate.current_location.visited is False or print_long_description is True:
                print(self.gamestate.current_location.get_long_description())
                self.gamestate.current_location.set_visited()
                print_long_description = False
            else:
                print(self.gamestate.current_location.get_short_description())

            # Prompt user for input and parse the command
            self.user_input = self.ui.user_prompt()

                # TODO: The language parser will have to return more than the verb. It will also need to identify the
                #  subject (feature or object) and appropriate prepositions and such. At a minimum I'd expect the LP to
                #  return a python dictionary of a verb that's being called and one or more subjects that are trying to
                #  be interacted. For example "use broom on dusty floor" might return:
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

            self.command, self.object, self.targets = self.lp.parse_command(self.user_input)

            # Conditionally handle each possible verb / command
            if self.command is LOOK:
                print_long_description = True

            elif self.command is LOOK_AT:
                self.verb_look_at(self.object)

            elif self.command is INVENTORY:
                self.verb_inventory()

            elif self.command is TAKE:
                if self.verb_take(self.object) is True:
                    print(PICKUP_SUCCESS_PREFIX + self.object + PICKUP_SUCCESS_SUFFIX)
                else:
                    print(PICKUP_FAILURE_PREFIX + self.object + PICKUP_FAILURE_SUFFIX)


            elif self.command is HELP:
                self.verb_help()

            else:
                print(COMMAND_NOT_IMPLEMENTED_YET)


            # Reset the input and command/object/targets from parser
            self.user_input = ""
            self.command, self.object, self.targets = INVALID_INPUT, None, None






    def load_game_menu(self):
        '''
        Sets appropriate variables in the GameClient's gamestate instance
        :return:
        '''
        # TODO: Implement this function (SSH)
        print(LOAD_GAME_MESSAGE)

    def initialize_new_game(self):
        logger.debug("A new game would be initialized here")
        self.gamestate.set_current_location(self.gamestate.rooms[0])

        # TODO: Set player state / inventory

        # TODO: Set each room to have correct objects

        # FOR TESTING PURPOSES:
        skateboard = Object("Skateboard", "A trendy skateboard with the text 'Z3R0 C007' inked on its surface")
        self.gamestate.current_location.add_object_to_room(skateboard)

    def game_status(self):
        # TODO: Implement this properly. Status codes in stringresources\status_codes.py
        # This function should/will check if player has won or lost(died/whatever)
        # if self.gamestate.player.speed is 0:
        #     return GAMEOVER_LOSE
        #
        # else:
            return GAME_CONTINUE

    def verb_look_at(self, object_name):
        '''
        Attempts to look at the subject
        :param object_name: Grammatical object at which player wishes to look. Could be a feature or an object in environment
        or in their inventory
        :return: None
        '''

        # Check of the 'object_name' is a feature of the room
        room_feature = self.gamestate.current_location.get_feature(object_name)
        if room_feature is not None:
            print(room_feature.get_description())
            return

        # If not, check if object_name in room
        room_object = self.gamestate.current_location.get_object_by_name(object_name) # TODO: Implement get_object_by_name in Room class
        if room_object is not None:
            print(room_object.get_description())
            return

        # If still not found, check player's inventory
        player_object = self.gamestate.player.inventory.get_object_by_name(object_name)
        if player_object is not None:
            print(player_object.get_description())
            return

        # If not anywhere, must not be in this room - tell player they don't see it
        print(LOOK_AT_NOT_SEEN)

    def verb_take(self, object_name):
        '''
        Evaluates a command to take object_name from the Room and if it exists (and is allowed by game rules) then
        object placed in inventory for the player
        :param object_name: string input by player in their command
        :return: True (success), False ( fail, object_name not found in the room)
        '''

        # TODO: Test this function

        # See if the room has the object before trying to update Room and player Inventory
        room_object = self.gamestate.current_location.get_object_by_name(object_name)
        if room_object is not None:
            self.gamestate.current_location.remove_object_from_room(room_object)
            self.gamestate.player.add_object_to_inventory(room_object)
            return True
        # TODO: if we have more complex objects player can take by stealing, this logic may be insufficient
        return False

    def verb_inventory(self):
        inventory_description = self.gamestate.player.get_inventory_string()
        print(inventory_description)

    def verb_help(self):
        self.ui.print_help_message()


class GameState:
    '''
    Holds all of the variables that maintain the game's state
    '''
    def __init__(self):
        self.rooms = []
        self.player = Player()

    def load_rooms_from_files(self):
        # TODO: Possibly delete this method, the GameClient is currently responsible for calling its room builder instance
        logger.debug("Loading rooms from files (This is a stub)")

    def set_current_location(self, room):
        '''
        Update the location the player is in
        :param room: The room the player is in (actual room)
        :return: N/A
        '''
        # TODO: Decide if we should set this by reference or by doing a room.name lookup and then setting it to that room
        # TODO: THis lookup would be done out of the GameState.rooms[] list of course
        self.current_location = room





class UserInterface:
    '''
    Primarily used to print information to the user's screen
    '''
    def __init__(self):
        # TODO: why can't reference this inside input() call in user_prompt(), or just make a stringresource variable (SSH)
        self.prompt_text = ">> "

    def print_introduction(self):
        print(INTRO_STRING)

    def print_main_menu(self):
        for line in MAIN_MENU_LINES:
            print(line)

    def user_prompt(self):
        user_input = ""  # TODO: Test if I can delete this line or not  (SSH)
        user_input = input(">> ")
        return user_input

    def print_help_message(self):
        for line in HELP_MESSAGE:
            print(line)


class Player:
    '''
    Player stats and methods
    '''
    def __init__(self):
        self.cash = 0
        self.coolness = 0
        self.speed = 0
        self.inventory = Inventory()

    def add_object_to_inventory(self, object):
        self.inventory.add_object(object)

    def remove_object_from_inventory(self, object):
        self.inventory.remove_object(object)

    def get_inventory_string(self):
        list = self.inventory.get_inventory_string()
        print(INVENTORY_LIST_HEADER)
        print(list + "\n\n")



class Inventory:
    '''
    Objects and methods related to adding and removing them from inventory
    '''
    def __init__(self):
        self.objects = []

    def get_object_by_name(self, object_name):
        '''
        Finds an object in the inventory by name and returns a reference to it
        :param object_name:
        :return:
        '''
        # TODO: Test function
        for object in self.objects:
            if object.name.lower() == object.name.lower():
                return object

        return None


    def add_object(self, object):
        self.objects.append(object)


    def remove_object(self, object):
        self.objects.remove(object)

    def get_inventory_string(self):
        '''
        Get a comma-delineated list of the objects in the inventory
        :return:
        '''
        if self.objects:
            inventory_size = len(self.objects)
            count = 0
            inventory_string = ""
            for object in self.objects:
                count += 1
                inventory_string += object.get_name()
                if count is not inventory_size:
                    inventory_string += ", "
                else:
                    inventory_string += "."
            return inventory_string
        return INVENTORY_EMPTY





class Object:
    '''
    An object. Can be in a Room or players inventory.
     Can be picked up from a room, dropped in a room, used, 'look at'ed, and possibly other actions
    '''
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_description(self):
        return self.description

    def get_name(self):
        return self.name

    def get_environmental_description(self):
        # TODO: Refine the output of this function somewhat? Could give objects unique environmental descriptions but
        # TODO: 1depending on the room they are in it wouldn't make sense once dropped somewhere else(SSH)
        description = "You see a " + self.name + " laying around."
        return description