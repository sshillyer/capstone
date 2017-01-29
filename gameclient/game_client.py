# DELPHINUS - ADVENTURE APP
# CS 467 - Winter 2017
# Team Members: Sara Hashem, Shawn Hillyer, Niza Volair

# game_client.py
# Description: GameClient class and closely-related classes
# Principal Author of this file per Project plan: Shawn Hillyer

# CITATIONS
# CITE: http://stackoverflow.com/questions/4810537/how-to-clear-the-screen-in-python
# CITE: http://stackoverflow.com/questions/110362/how-can-i-find-the-current-os-in-python

import os
import platform

from languageparser.language_parser import LanguageParser
from gameclient.player import *
from gameclient.object import *
from fileio.save_game import *
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

        # Instantiate unenforced singleton-style instances of various components
        self.ui = UserInterface()
        self.lp = LanguageParser()

        # Variables used to store GameClient state
        self.user_input = ""
        self.command = INVALID_INPUT
        self.valid_main_menu_commands = { QUIT, LOAD_GAME, NEW_GAME , HELP }

        # Clear old console text before beginning game
        self.ui.clear_screen()

    def main_loop(self):
        '''
        Comments outline the flow of project and intended functions for now
        based on game engine workflow graph
        :return: N/A
        '''


        # Load data from files (Specifically rooms, but can do other files as well)
        # Gamestate level details will later be loaded in the main menu loop
        self.gamestate.rooms = self.gamestate.rb.load_room_data_from_file()

        # Outer loop makes game play until user decides to quit from the main menu
        while self.command is not QUIT:

            # Inner loop runs the main menu and prompts until a valid command is entered
            self.main_menu_loop()

            # Branch initializes a new game or ends up loading a game, quits, or just prints the help and loops
            if self.command is NEW_GAME:
                self.gamestate.initialize_new_game()
            elif self.command is LOAD_GAME:
                self.load_game_menu()
            # Or exit the game...
            elif self.command is QUIT:
                print(EXIT_MESSAGE)
                sys.exit()
            # Or print the help menu
            elif self.command is HELP:
                self.ui.print_help_message()

            # This logic exits ONLY IF Player decided to play game. GameState initialized in the if/elif structure above
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
                    self.reset_input_and_command()
                    self.play_game()
                elif exit_code is GAMEOVER_QUIT:
                    print("Game over: Player quit")
                    self.reset_input_and_command()

            self.reset_input_and_command()

    def main_menu_loop(self):
        '''
        Prints the main menu and sets self.command until command is set to a proper value
        :return: indirectly - sets instance variable, self.command, to a valid command
        '''
        # first_pass logic is to ensure we don't print invalid command to the user unless it's their second attempt
        first_pass = True
        while not self.is_valid_menu_command(self.command):
            if first_pass:
                first_pass = False
            else:
                self.ui.clear_screen()
                print(self.user_input + INVALID_MENU_COMMAND_MESSAGE + "\n\n")
                self.ui.wait_for_enter()
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

        self.ui.new_game_splash_screen()

        status = GAME_CONTINUE          # Force entry into main loop

        print_long_description = False  # Override if user just typed the 'look' command

        # Game will loop until a 'Gameover' condition is met
        while status is GAME_CONTINUE:
            # Check game status; if Gameover, leave game loop and return status code
            status = self.gamestate.game_status()

            if status in GAMEOVER_STATES:  # list as defined in stringresources\status_codes.py
                return status

            # Print the current room's appropriate description
            self.verb_look(print_long_description)
            print_long_description = False # Reset this to false after printing

            # Prompt user for input and parse the command
            self.user_input = self.ui.user_prompt()

            # TODO: Update this once languageparser fully implemented
            self.command, self.object, self.targets = self.lp.parse_command(self.user_input)

            # Conditionally handle each possible verb / command
            if self.command is LOOK:
                # The verb_look() method is called at the top of each loop, so not explicitly called here
                print_long_description = True
                self.ui.clear_screen()

            elif self.command is LOOK_AT:
                self.verb_look_at(self.object)

            elif self.command is INVENTORY:
                self.verb_inventory()

            elif self.command is TAKE:
                if self.verb_take(self.object) is True:
                    print(PICKUP_SUCCESS_PREFIX + self.object + PICKUP_SUCCESS_SUFFIX)
                else:
                    print(PICKUP_FAILURE_PREFIX + self.object + PICKUP_FAILURE_SUFFIX)

            elif self.command is DROP:
                self.verb_drop(self.object)

            elif self.command is GO:
                destination = self.verb_go(self.object)
                if destination:
                    print(GO_SUCCESS_PREFIX + destination.get_name() + GO_SUCCESS_SUFFIX)
                else:
                    print(GO_FAILURE_PREFIX + self.object + GO_FAILURE_SUFFIX)

            elif self.command is HELP:
                self.verb_help()

            elif self.command is LOAD_GAME:
                load_confirmed = self.verb_quit(LOAD_CONFIRM_PROMPT)
                if load_confirmed == True:
                    status = GAMEOVER_LOAD

            elif self.command is SAVE_GAME:
                self.save_game_menu()

            elif self.command is CHEATCODE_WIN:
                status = self.verb_cheat_win()

            elif self.command is CHEATCODE_LOSE:
                status = self.verb_cheat_lose()

            elif self.command is QUIT:
                quit_confirmed = self.verb_quit(QUIT_CONFIRM_PROMPT)
                if quit_confirmed == True:
                    status = GAMEOVER_QUIT
            else:
                # TODO: This should be a different string once every verb is implemented
                print(COMMAND_NOT_IMPLEMENTED_YET)

            # This is called to ensure no lingering variables set in the GameClient by user or language parser returns
            self.reset_input_and_command()
        return status


    def load_game_menu(self):
        '''
        Sets appropriate variables in the GameClient's gamestate instance
        :return:
        '''
        # TODO: Implement this function ((SSH))
        print(LOAD_GAME_MESSAGE)

        # TODO: This should ultimately result in a self.gamestate.initialize_load_game(filename) call (not implemented ((SSH))

    def save_game_menu(self):
        # TODO: Implement the save game menu and logic ((SSH))
        print(SAVE_GAME_MESSAGE)
        self.ui.wait_for_enter()

    def verb_look_at(self, object_name):
        '''
        Attempts to look at the subject
        :param object_name: Grammatical object at which player wishes to look.
                            Could be a feature or an object in environment or in their inventory
        :return: None
        '''

        # Check of the 'object_name' is a feature of the room
        room_feature = self.gamestate.get_current_room().get_feature(object_name)
        room_object = self.gamestate.get_current_room().get_object_by_name(object_name)
        player_object = self.gamestate.player.inventory.get_object_by_name(object_name)

        if room_feature is not None:
            description = room_feature.get_description()
        elif room_object is not None:
            description = room_object.get_description()
        elif player_object is not None:
            description = player_object.get_description()
        else:
            description = LOOK_AT_NOT_SEEN

        print(description)
        self.ui.wait_for_enter()


    def verb_take(self, object_name):
        '''
        Evaluates a command to take object_name from the Room and if it exists (and is allowed by game rules) then
        object placed in inventory for the player
        :param object_name: string input by player in their command
        :return: True (success), False ( fail, object_name not found in the room)
        '''

        # See if the room has the object before trying to update Room and player Inventory
        room_object = self.gamestate.get_current_room().get_object_by_name(object_name)
        if room_object is not None:
            self.gamestate.get_current_room().remove_object_from_room(room_object)
            self.gamestate.player.add_object_to_inventory(room_object)
            print(TAKE_MESSAGE_PREFIX + room_object.get_name() + TAKE_MESSAGE_SUFFIX)
            self.ui.wait_for_enter()
            return True
        return False

    def verb_help(self):
        self.ui.print_help_message()
        self.ui.wait_for_enter()

    def verb_inventory(self):
        inventory_description = self.gamestate.player.get_inventory_string()
        self.ui.print_inventory(inventory_description)
        self.ui.wait_for_enter()


    def verb_drop(self, object_name):
        inventory_object = self.gamestate.player.inventory.get_object_by_name(object_name)
        if inventory_object is not None:
            self.gamestate.player.inventory.remove_object(inventory_object)
            self.gamestate.get_current_room().add_object_to_room(inventory_object)
            print(DROP_SUCCESS_PREFIX + self.object + DROP_SUCCESS_SUFFIX)
        else:
            print(DROP_FAILURE_PREFIX + self.object + DROP_FAILURE_SUFFIX)
            return False
        self.ui.wait_for_enter()


    def verb_go(self, destination):
        # See if the destination is the cardinal direction OR the name of one of the room_connections
        for connection in self.gamestate.get_current_room().room_connections:
            if connection.label.lower() == destination.lower() \
                    or connection.cardinal_direction.lower() == destination.lower():
                new_room = self.gamestate.get_room_by_name(connection.destination.lower())
                if new_room:
                    self.gamestate.set_current_room(new_room)
                    return new_room
                else:
                    logger.debug("The 'go' command almost worked, but the destination room isn't in the GameState.rooms list")
        return None

    def verb_cheat_win(self):
        self.ui.clear_screen()
        print(GAMEOVER_CHEAT_WIN_MESSAGE)
        return GAMEOVER_WIN

    def verb_cheat_lose(self):
        self.ui.clear_screen()
        print(GAMEOVER_CHEAT_LOSE_MESSAGE)
        return GAMEOVER_FORFEIT

    def verb_quit(self, message):
        self.ui.clear_screen()
        self.ui.print_quit_confirm(message)
        confirm = self.ui.user_prompt().lower()
        if confirm in YES_ALIASES:
            return True
        return False

    def reset_input_and_command(self):
        # Reset the input and command/object/targets from parser
        self.user_input = ""
        self.command, self.object, self.targets = INVALID_INPUT, None, None



    def verb_look(self, print_long_description):
        '''
        First clear the screen then determine correct version to print.
        :param print_long_description: If set to true, forces long description to print even if user has been in room
        before. Used for 'look' command
        :return:
        '''
        self.ui.clear_screen()

        if self.gamestate.get_current_room().visited is False or print_long_description is True:
            description= self.gamestate.get_current_room().get_long_description()
        else:
            description = self.gamestate.get_current_room().get_short_description()

        header_info = self.gamestate.get_header_info()
        self.ui.print_status_header(header_info)

        self.ui.print_room_description(description)
        self.gamestate.get_current_room().set_visited()



class GameState:
    '''
    Holds all of the variables that maintain the game's state
    '''
    def __init__(self):
        self.rooms = []
        self.player = Player()
        self.ob = ObjectBuilder()
        self.rb = RoomBuilder()

    def set_current_room(self, room):
        '''
        Update the location the player is in
        :param room: The room the player is in (actual room)
        :return: N/A
        '''
        # TODO: Decide if we should set this by reference or by doing a room.name lookup and then setting it to that room ((SSH))
        # TODO: THis lookup would be done out of the GameState.rooms[] list of course ((SSH))
        self.current_room = room

    def get_room_by_name(self, room_name):
        for room in self.rooms:
            if room.name.lower() == room_name.lower():
                return room
        return None

    def initialize_new_game(self):
        # TODO: Need to make sure initialize new game clears ALL gamestate variables. At present, starting new game ((SSH))
        # TODO: then quitting and starting another new game causes another skateboard to appear in street if left there ((SSH))
        # TODO: Set player state ((SSH))

        self.set_room_vars_to_default()
        self.set_default_room("Street")

        # Get a list of every object in game. Each object has a default location so we can put in each room or inventory
        game_objects = self.ob.get_game_objects()
        self.place_objects_in_rooms(game_objects)


    def initialize_load_game(self, filename):
        # TODO: Finish fleshing out these ideas and test this function. Will require constant tweaking of this and the SaveGame
        # TODO: class because of the interdependence, unless better plan is developed ((SSH))
        # TODO: Write UNIT TESTS for this code, entirely untested
        self.set_room_vars_to_default()

        save_game = SaveGame(None)
        save_game.load_from_file(filename)

        # Set each room's visited status
        visited_rooms_list = save_game.get_visited_rooms_list()
        for room_name in visited_rooms_list:
            room = self.get_room_by_name(room_name)
            room.set_visited(True)

        # Retrieve the dictionary of room_name : [object_list] pairs and iterate through, setting each room's objects
        # to the list in the SaveGame object
        room_objects_dictionary = save_game.get_objects_in_rooms()
        for room_name in room_objects_dictionary:
            room = self.get_room_by_name(room_name)
            if room:
                for room_objects in room_objects_dictionary[room_name]:
                    room.set_objects(room_objects)
            else:
                logger.debug("Error finding the room stored in a SaveGame object")

        # Also set the current_room
        current_room_name = save_game.get_current_room()
        current_room = self.get_room_by_name(current_room_name)
        self.set_current_room(current_room)




    def game_status(self):
        # TODO: Implement this properly. Status codes in stringresources\status_codes.py  ((SSH))
        # This function should/will check if player has won or lost(died/whatever)
        # if self.gamestate.player.speed is 0:
        #     return GAMEOVER_LOSE
        #
        # else:
        return GAME_CONTINUE

    def get_header_info(self):
        header_info = {
            'speed' : self.player.speed,
            'coolness' : self.player.coolness,
            'current_room' : self.current_room.get_name()
        }
        return header_info

    def set_room_vars_to_default(self):
        for room in self.rooms:
            room.set_visited(False)
            room.objects = []

    def set_default_room(self, room_name):
        default_room = self.get_room_by_name(room_name)
        self.set_current_room(default_room)

    def place_objects_in_rooms(self, game_objects):
        for object in game_objects:
            room_name = object.get_default_location_name()
            if room_name.lower() == "inventory":
                self.player.add_object_to_inventory(object)
            else:
                room = self.get_room_by_name(room_name)
                room.add_object_to_room(object)

    def get_current_room(self):
        return self.current_room

class UserInterface:
    '''
    Primarily used to print information to the user's screen
    '''

    def __init__(self):
        self.prompt_text = PROMPT_TEXT

        # Determine OS and set variable to call correct system calls for clearing screen etc
        # CITE: http://stackoverflow.com/questions/1854/how-to-check-what-os-am-i-running-on-in-python
        operating_system = platform.system()
        if operating_system == 'Linux':
            logger.debug("System is Linux")
            self.op_system = 'Linux'
        elif operating_system == 'Windows':
            logger.debug("System is Windows")
            self.op_system = 'Windows'


    def print_introduction(self):
        print(INTRO_STRING)

    def print_main_menu(self):
        for line in MAIN_MENU_LINES:
            print(line)

    def user_prompt(self):
        user_input = input(self.prompt_text)
        return user_input

    def print_help_message(self):
        for line in HELP_MESSAGE:
            print(line)
        self.wait_for_enter()

    def print_quit_confirm(self, message):
        print(message)

    def clear_screen(self):
        # Cite: http://stackoverflow.com/questions/4810537/how-to-clear-the-screen-in-python
        if self.op_system == "Windows":
            os.system('cls')
        elif self.op_system == "Linux":
            os.system('clear')
        else:
            pass

    def new_game_splash_screen(self):
        self.clear_screen()
        print(NEW_GAME_MESSAGE)  # Defined in stringresources\strings.py
        self.wait_for_enter()

    def print_status_header(self, info):
        print(STATUS_HEADER_BAR)
        print("|\tSPEED: " + str(info['speed']))
        print("|\tCOOLNESS: " + str(info['coolness']) )
        print("|\tCURRENT LOCATION: " + str(info['current_room']))
        print(STATUS_HEADER_BAR)

    def wait_for_enter(self):
        input(PRESS_KEY_TO_CONTINUE_MSG)
        self.clear_screen()

    def print_room_description(self, description):
        print(DESCRIPTION_HEADER)
        print(description)
        print(DESCRIPTION_FOOTER)

    def print_inventory(self, inventory_description):
        print(INVENTORY_LIST_HEADER)
        print(inventory_description)
        print(INVENTORY_LIST_FOOTER)
