# DELPHINUS - ADVENTURE APP
# CS 467 - Winter 2017
# Team Members: Sara Hashem, Shawn Hillyer, Niza Volair

# game_client.py
# Description: GameClient class and closely-related classes
# Principal Author of this file per Project plan: Shawn Hillyer

# CITATIONS
# CITE: http://stackoverflow.com/questions/4810537/how-to-clear-the-screen-in-python
# CITE: http://stackoverflow.com/questions/110362/how-can-i-find-the-current-os-in-python
# CITE: https://docs.python.org/3.3/library/random.html

from constants.gameplay_settings import *
from constants.language_words import *
from gameclient.game_state import *
from gameclient.random_event_generator import *
from gameclient.user_interface import *
from gameclient.wprint import *
from languageparser.language_parser import LanguageParser

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
        self.rand_event = RandomEventGenerator()

        # Variables used to store GameClient state
        self.reset_input_and_command()
        self.valid_main_menu_commands = { QUIT, LOAD_GAME, NEW_GAME , HELP }

        # Clear old console text before beginning game
        self.ui.clear_screen()

    def main_loop(self):
        '''
        Comments outline the flow of project and intended functions for now
        based on game engine workflow graph
        :return: N/A
        '''

        # Outer loop makes game play until user decides to quit from the main menu
        while self.command is not QUIT:

            # Inner loop runs the main menu and prompts until a valid command is entered
            self.main_menu_loop()

            # Branch initializes a new game or ends up loading a game, quits, or just prints the help and loops
            if self.command is NEW_GAME:
                try:
                    self.gamestate.initialize_new_game()
                except:
                    logger.debug("initialize_gamestate() exception")
            elif self.command is LOAD_GAME:
                try:
                    self.load_game_menu()
                except:
                    logger.debug("load_game_menu() exception")
            # Or exit the game...
            elif self.command is QUIT:
                wprint(EXIT_MESSAGE)
                sys.exit()
            # Or print the help menu
            elif self.command is HELP:
                self.ui.print_help_message()
                self.reset_input_and_command()
                continue

            # This logic exits ONLY IF Player decided to play game. GameState initialized in the if/elif structure above
            if self.command is NEW_GAME or self.command is LOAD_GAME:
                # Actually playing the game will eventually terminate for one of the below reasons
                # We handle each case separately because if a player forfeits and does not save,
                # it can have different logic than if they quit and save, etc.
                # The constants are defined in constants\gameover_status_codes.py

                if self.command is NEW_GAME:
                    self.ui.print_splash_screen_new_game()
                elif self.command is LOAD_GAME:
                    self.ui.print_splash_screen_load_game()

                exit_code = self.play_game()
                if exit_code is GAMEOVER_FORFEIT:
                    wprint("Game over: Forfeit")
                elif exit_code is GAMEOVER_WIN:
                    wprint("Game over: Player won")
                elif exit_code is GAMEOVER_LOSE:
                    wprint("Game over: Player lost")
                elif exit_code is GAMEOVER_SAVE:
                    # DEBUG
                    print("ABOUT TO SAVE THIS GAME...")
                    self.save_game_menu()
                    wprint("Game over: Player saved game")
                elif exit_code is GAMEOVER_LOAD:
                    wprint("Game over: Player loading game")
                    self.reset_input_and_command()
                    self.command = LOAD_GAME
                    continue
                elif exit_code is GAMEOVER_QUIT:
                    wprint("Game over: Player quit")
                    self.reset_input_and_command()
            self.ui.wait_for_enter()
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
                wprint(self.user_input + INVALID_MENU_COMMAND_MESSAGE + "\n\n")
                self.ui.wait_for_enter()
            self.main_menu_prompt()

            self.send_command_to_parser()

    def main_menu_prompt(self):
        '''
        Prints the main menu then prompts the user for input one time_left
        :return: Indirectly - sets instance variable user_input to the string typed by user
        '''
        self.ui.print_main_menu()
        self.user_input = self.ui.user_prompt()

    def is_valid_menu_command(self, command):
        '''
        Checks the command returned from language parser against a list of valid menu commands defined on the
        GameClient class (which are in term constants defined in constants\verbs.py)
        :param command: A constant defined in constants\verbs.py
        :return: True or false depending on presence of the command in the list of valid commands
        '''
        if command in self.valid_main_menu_commands:
            return True
        else:
            return False

    def reset_input_and_command(self):
        # Reset the input and command/verb_noun_name/targets from parser
        self.user_input = None
        self.verb_noun_name = None
        self.verb_noun_type = None
        self.verb_targets = None
        self.verb_preposition = None
        self.command = INVALID_INPUT

    def play_game(self):
        '''
        Primary game loop that prints information to user, reads input, and reacts accordingly
        :return: a status code as defined in constants\status_codes.py, used by gameclient to determine how
        and/or why game ended.
        '''

        status = GAME_CONTINUE          # Force entry into main loop

        print_long_description = False  # Override if user just typed the 'look' command

        # Game will loop until a 'Gameover' condition is met
        while status is GAME_CONTINUE:
            # Check game status; if Gameover, leave game loop and return status code
            status = self.gamestate.game_status()

            if status in GAMEOVER_STATES:  # list as defined in constants\gameover_status_codes.py
                return status

            # Print the current room's appropriate long_description
            self.verb_look(print_long_description)
            print_long_description = False # Reset this to false after printing

            # Prompt user for input and parse the command
            self.user_input = self.ui.user_prompt()
            self.send_command_to_parser()


            # TODO: Refactor verb_*() methods to check the parser_error_message before proceeding
            # Conditionally handle each possible verb / command
            if self.command is LOOK:
                # The verb_look() method is called at the top of each loop, so not explicitly called here
                print_long_description = True
                self.gamestate.update_time_left(LOOK_COST)
                self.ui.clear_screen()
            # Verbs
            elif self.command is LOOK_AT:
                self.verb_look_at(self.verb_noun_name, self.verb_noun_type)
            elif self.command is INVENTORY:
                self.verb_inventory()
            elif self.command is TAKE:
                self.verb_take(self.verb_noun_name, self.verb_noun_type)
            elif self.command is DROP:
                self.verb_drop(self.verb_noun_name)
            elif self.command is GO:
                self.verb_go(self.verb_noun_name, self.parser_error_message)
            elif self.command is HACK:
                self.verb_hack(self.verb_noun_name, self.verb_noun_type)
            elif self.command is STEAL:
                self.verb_steal(self.verb_noun_name, self.verb_noun_type)
            elif self.command is BUY:
                self.verb_buy(self.verb_noun_name)
            elif self.command is SPRAYPAINT:
                # TODO: Finish implementing verb_spraypaint and remove the debug print
                logger.debug("Spraypaint is not fully implemented yet.")
                self.verb_spraypaint(self.verb_noun_name)
            elif self.command is USE:
                self.verb_use(self.verb_noun_name, self.verb_noun_type)
            elif self.command is HELP:
                self.verb_help(self.verb_noun_name, self.verb_noun_type)
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
                save_game_prompt = self.verb_save(SAVE_GAME_PROMPT)
                if quit_confirmed == True and save_game_prompt == False:
                    status = GAMEOVER_QUIT
                elif quit_confirmed == True and save_game_prompt == True:
                    # Save game to file and exit
                    status = GAMEOVER_SAVE
                    # if quit_confirmed == True:
                    #     status = SAVE_GAME
            else:
                wprint(COMMAND_NOT_UNDERSTOOD)
                self.ui.wait_for_enter()

            # This is called to ensure no lingering variables set in the GameClient by user or language parser returns
            # self.reset_input_and_command()
        return status

    def load_game_menu(self):
        '''
        Sets appropriate variables in the GameClient's gamestate instance
        :return:
        '''
        wprint(LOAD_GAME_MESSAGE)

        savegame_list = SaveGame.get_savegame_filenames()

        if savegame_list:
            input_is_valid = False
            option = -1

            while input_is_valid is False:
                input_is_valid = True # Turn this back to false if we get exception converting to an int
                counter = 1
                for savegame in savegame_list:
                    wprint(str(counter) + ": " + savegame)
                    counter += 1

                wprint(LOAD_FILENAME_PROMPT)
                user_choice = self.ui.user_prompt()

                # Cite: http://stackoverflow.com/questions/5424716/how-to-check-if-input-is-a-number
                try:
                    option = int(user_choice)
                except:
                    wprint(LOAD_NOT_INTEGER)
                    input_is_valid = False
                    continue

                option -= 1
                if option < 0 or option >= len(savegame_list):
                    wprint(LOAD_OUT_OF_RANGE_MESSAGE)
                    input_is_valid = False
                    continue

            # If here we have a valid option
            self.gamestate.initialize_load_game(savegame_list[option])
            return True

        else:
            wprint(LOAD_GAME_NO_SAVES)
            return False

    def save_game_menu(self):
        save_game = SaveGame(self.gamestate)
        file_name = ""
        valid_filename = False

        while valid_filename is False or file_name == "":
            wprint(SAVE_GAME_FILE_PROMPT)
            file_name = self.ui.user_prompt() + '.json'
            valid_filename = save_game.is_existing_saved_game(file_name)
            if valid_filename is False:
                wprint(SAVE_GAME_VALID_FILENAME_MESSAGE)

        if save_game.write_to_file(file_name) is True:
            wprint(SAVE_GAME_SUCCESS + file_name)
        else:
            wprint(SAVE_GAME_FAILED + file_name)

        self.ui.wait_for_enter()

    def go_to_jail(self):
        county_jail = self.gamestate.get_room_by_name("County Jail")
        self.gamestate.set_current_room(county_jail)
        wprint(JAIL_GO_TO_MESSAGE)
        self.gamestate.update_time_left(JAIL_COST)
        self.ui.wait_for_enter()

    def verb_buy(self, noun_name):
        '''
        :param noun_name: string, name of the object desired
        :return: True if player bought object_name, false otherwise
        '''
        buy_succeeded = False

        room_feature = self.gamestate.get_current_room().get_feature_by_name(noun_name)
        if room_feature is not None:
            wprint(BUY_FEATURE_PREFIX + room_feature.get_name())
            buy_succeeded = False
        else:
            object = self.gamestate.get_current_room().get_object_by_name(noun_name)
            player_cash = self.gamestate.player.get_cash()

            if object is None:
                wprint(BUY_NOT_IN_ROOM)
            elif object.get_cost() is 0:
                wprint(BUY_FREE_ITEM)
            elif object.is_owned_by_player() is True:
                wprint(BUY_FREE_ITEM)
            elif object.get_cost() > player_cash:
                wprint(BUY_INSUFFICIENT_CASH_PREFIX + str(object.get_cost()) + BUY_INSUFFICIENT_CASH_SUFFIX)
            else:
                self.gamestate.player.add_object_to_inventory(object)
                self.gamestate.get_current_room().remove_object_from_room(object)
                self.gamestate.player.update_cash(object.get_cost() * -1 ) # Send in cost as negative to reduce cash
                wprint(BUY_SUCCESS_PREFIX + object.get_name() + BUY_SUCCESS_SUFFIX)
                buy_succeeded = True

        if buy_succeeded:
            self.gamestate.update_time_left(BUY_COST)

        self.ui.wait_for_enter()
        return buy_succeeded

    def verb_cheat_win(self):
        self.ui.clear_screen()
        wprint(GAMEOVER_CHEAT_WIN_MESSAGE)
        return GAMEOVER_WIN

    def verb_cheat_lose(self):
        self.ui.clear_screen()
        wprint(GAMEOVER_CHEAT_LOSE_MESSAGE)
        return GAMEOVER_FORFEIT

    def verb_drop(self, object_name):
        drop_success = False

        room_feature = self.gamestate.get_current_room().get_feature_by_name(object_name)
        if room_feature is not None:
            wprint(DROP_INVALID_PREFIX + room_feature.get_name() + DROP_INVALID_SUFFIX)
            drop_success = False

        else:
            inventory_object = self.gamestate.player.inventory.get_object_by_name(object_name)

            if self.gamestate.get_current_room().is_virtual_space() is True:
                wprint(DROP_FAILURE_VIRTUALSPACE)
            elif inventory_object is not None:
                self.gamestate.player.inventory.remove_object(inventory_object)
                self.gamestate.get_current_room().add_object_to_room(inventory_object)
                wprint(DROP_SUCCESS_PREFIX + self.verb_noun_name + DROP_SUCCESS_SUFFIX)
                drop_success = True
            else:
                wprint(DROP_FAILURE_PREFIX + self.verb_noun_name + DROP_FAILURE_SUFFIX)

        if drop_success:
            self.gamestate.update_time_left(DROP_COST)

        self.ui.wait_for_enter()
        return drop_success

    def verb_go(self, destination, error_message):
        go_success = False

        if error_message is not None:
            wprint(error_message)
            wprint("This is probably because typing a destination's label like 'pawn shop', is not yet implemented")
            self.ui.wait_for_enter()
            return go_success

        destination = destination.lower()
        cur_room = self.gamestate.get_current_room()
        destination_room_name = None

        if destination is None or destination.isspace():
           message = GO_FAILURE_DESTINATION_MISSING

        room_feature = self.gamestate.get_current_room().get_feature_by_name(destination)
        if room_feature is not None:
            message = GO_INVALID_PREFIX + room_feature.get_name() + GO_INVALID_SUFFIX

        else:
            # See if the destination is the cardinal direction OR the name of one of the room_connections
            for connection in cur_room.room_connections:
                if connection.label.lower() == destination or connection.cardinal_direction.lower() == destination:
                    destination_room_name = connection.destination.lower()
                    # Handle sub-way logic:
                    if cur_room.get_name().lower() == "subway":
                        # It's free to go back where you came from, so check that first
                        if destination_room_name.lower() == self.gamestate.get_prior_room().get_name().lower():
                            go_success = True
                            break
                        elif cur_room.get_feature_by_name("Turnstiles").is_hacked() is not True:
                            if self.gamestate.player.get_cash() < SUBWAY_GO_DOLLAR_COST:
                                message = GO_FAILURE_SUBWAY_CASH
                                go_success = False
                                break
                            else:
                                self.gamestate.player.update_cash(SUBWAY_GO_DOLLAR_COST * -1)
                                go_success = True
                                break
                        else:
                            go_success = True
                            break
                    else:
                        go_success = True
                        break
                else:
                    message = GO_FAILURE_PREFIX + self.verb_noun_name + GO_FAILURE_SUFFIX


        if go_success is True:
            new_room = self.gamestate.get_room_by_name(destination_room_name)
            if new_room:
                self.gamestate.set_current_room(new_room)
                message = GO_SUCCESS_PREFIX + new_room.get_name() + GO_SUCCESS_SUFFIX
                self.gamestate.update_time_left(GO_COST)
                go_success = True
            else:
                # If go failed to find the room / direction desired, print a failure message
                logger.debug("The 'go' command almost worked, but the destination room isn't in the GameState.rooms list")
                logger.debug(GO_FAILURE_PREFIX + self.verb_noun_name + GO_FAILURE_SUFFIX)
                message = GO_FAILURE_PREFIX + self.verb_noun_name + GO_FAILURE_SUFFIX



        wprint(message)
        self.ui.wait_for_enter()
        return go_success

    def verb_hack(self, noun_name, noun_type):
        # TODO: Finish implementing verb_hack
        hack_success = False

        if self.gamestate.player.can_hack() is False:
            message = HACK_FAIL_NOSKILL

        else:
            # TODO: Once noun_type is passed by language-parser, change this to use commneted out if statements
            # if noun_type == NOUN_TYPE_OBJECT:
            #     message = HACK_FAIL_INVALID_TARGET
            #     hack_success = False

            # if noun_type == NOUN_TYPE_FEATURE:
            if True: # Swap this with preceeding line later on
                cur_room = self.gamestate.get_current_room()
                try:
                    feature = cur_room.get_feature_by_name(noun_name)
                    logger.debug("feature retreived by name " + noun_name)
                    feature_name = feature.get_name().lower()
                    logger.debug("feature name.get_name() called: " + feature_name)
                    if feature.is_hackable() is True:
                        if feature.is_hacked() is True:
                            message = HACK_FAIL_ALREADY_HACKED

                        elif feature_name == "traffic lights":
                            message = HACK_SUCCESS_TRAFFIC_LIGHTS
                            self.gamestate.player.update_speed(HACK_LIGHT_SPEED_CHANGE)
                            hack_success = True

                        elif feature_name == "atm":
                            message = HACK_SUCCESS_ATM + " You get " + str(HACK_ATM_CASH_AMOUNT) + " bucks."
                            self.gamestate.player.update_cash(HACK_ATM_CASH_AMOUNT)
                            hack_success = True

                        elif feature_name == "turnstiles":
                            message = HACK_SUCCESS_TURNSTILE
                            hack_success = True

                        else:
                            message = "You tried to hack something that is hackable and has not already been hacked, but the programmers forgot to program an effect. Email the authors!"
                    else:
                        message = HACK_FAIL_INVALID_TARGET
                except:
                    message = HACK_FAIL_FEATURE_NOT_PRESENT
            else: # TODO: Delete t his else statement once parser works with type/object identification
                message = "This should never print."

        if hack_success is True:
            try:
                feature.set_is_hacked(True)
            except:
                logger.debug("hack_success is True but failed to call feature.set_is_hacked(True)")

        print(message)
        self.ui.wait_for_enter()
        return hack_success


    def verb_help(self, noun_name, noun_type):
        '''
        Print help. Gives a generic message if user tries to call help on a feature or object in the room/inventory,
        otherwise just prints the generic help message.
        :param noun_name: subject passed back by language parser
        :param noun_type: subject's type (object/feature) as passed back from language parser
        :return:
        '''
        if noun_type == NOUN_TYPE_FEATURE:
            # Only print a hep message if the feature is part of current room to avoid confusion and player trying to
            # call the 'look at' verb on features in other rooms that they are not presently in
            room_feature = self.gamestate.get_current_room().get_feature_by_name(noun_name)
            if room_feature is not None:
                wprint(room_feature.get_name() + HELP_FEATURE_GENERIC)
                self.ui.wait_for_enter()
                return

        elif noun_type == NOUN_TYPE_OBJECT:
            # Only display help on objects in the current room or player's inventory. Generic message but avoids people
            # mining for information by spamming 'help' I suppose
            obj = self.gamestate.get_current_room().get_object_by_name(noun_name)
            if obj is None:
                obj = self.gamestate.player.inventory.get_object_by_name(noun_name)
            if obj is not None:
                wprint(obj.get_name() + HELP_OBJECT_GENERIC)
                self.ui.wait_for_enter()
                return
            else:
                self.ui.print_help_message()
        else:
            self.ui.print_help_message()

    def verb_inventory(self):
        self.gamestate.update_time_left(INVENTORY_COST)
        inventory_description = self.gamestate.player.get_inventory_string()
        self.ui.print_inventory(inventory_description)
        self.ui.wait_for_enter()

    def verb_look(self, print_long_description):
        '''
        First clear the screen then determine correct version to print.
        :param print_long_description: If set to true, forces long_description to print even if user has been in room
        before. Used for 'look' command
        :return:
        '''
        self.ui.clear_screen()

        if self.gamestate.get_current_room().is_visited() is False or print_long_description is True:
            description = self.gamestate.get_current_room().get_long_description()
        else:
            description = self.gamestate.get_current_room().get_short_description()

        header_info = self.gamestate.get_header_info()
        self.ui.print_status_header(header_info)
        self.ui.print_room_description(description)
        self.gamestate.get_current_room().set_visited()

    def verb_look_at(self, noun_name, noun_type):
        '''
        Attempts to look at the subject
        :param noun_name: Grammatical object at which player wishes to look.
                            Could be a feature or an object in environment or in their inventory
        :return: None
        '''
        room_feature = self.gamestate.get_current_room().get_feature_by_name(noun_name)
        room_object = self.gamestate.get_current_room().get_object_by_name(noun_name)
        player_object = self.gamestate.player.inventory.get_object_by_name(noun_name)

        looked_at_trash_can = False

        if room_feature is not None:
            try:
                description = room_feature.get_description()
                if room_feature.get_name().lower() == "trash can":
                    looked_at_trash_can = True
            except:
                logger.debug("verb_look_at(): room_feature.get_description() exception")
                description = "Uh oh, something has gone wrong. Contact the developer!"
        elif room_object is not None:
            try:
                description = room_object.get_long_description()
            except:
                logger.debug("verb_look_at(): room_object.get_description() exception")
                description = "Uh oh, something has gone wrong. Contact the developer!"
        elif player_object is not None:
            try:
                description = player_object.get_long_description()
            except:
                logger.debug("verb_look_at(): player_object.get_description() exception")
                description = "Uh oh, something has gone wrong. Contact the developer!"
        else:
            description = LOOK_AT_NOT_SEEN

        self.gamestate.update_time_left(LOOK_AT_COST)
        description = textwrap.fill(description, TEXT_WIDTH)
        print(description) # Don't use wprint() or it will remove linebreaks
        self.ui.wait_for_enter()

        if looked_at_trash_can:
            self.search_trash_can()

    def verb_quit(self, message):
        '''
        Prints the message passed in then prompts user if they are sure they wish to quit
        :param message: string
        :return: message that should be printed
        '''
        self.ui.clear_screen()
        self.ui.print_quit_confirm(message)
        confirm = self.ui.user_prompt().lower()
        if confirm in YES_ALIASES:
            return True
        return False

    def verb_save(self, message):
        '''
        Prints the message passed in then prompts user if they are sure they wish to save
        :param message: string
        :return: message that should be printed
        '''
        self.ui.clear_screen()
        self.ui.print_quit_confirm(message)
        confirm = self.ui.user_prompt().lower()
        if confirm in YES_ALIASES:
            return True
        return False

    def verb_take(self, noun_name, noun_type):
        '''
        Evaluates a command to take object_name from the Room and if it exists (and is allowed by game rules) then
        object placed in inventory for the player
        :param noun_name: string input by player in their command
        :return: True (success), False ( fail, object_name not found in the room)
        '''
        take_success = False

        if noun_type == NOUN_TYPE_FEATURE:
            # logger.debug("verb_take() noun_type == 'feature'")
            room_feature = self.gamestate.get_current_room().get_feature_by_name(noun_name)
            if room_feature is None:
                wprint("You don't see a " + noun_name + " to try and take.")
            else:
                wprint("You cannot take the " + room_feature.get_name() + " - that's impractical.")

        elif noun_type == NOUN_TYPE_OBJECT:
            # logger.debug("verb_take() noun_type == 'object'")
            room_object = self.gamestate.get_current_room().get_object_by_name(noun_name)

            if room_object is not None:
                if room_object.get_cost() is 0 or room_object.is_owned_by_player() is True:
                    self.gamestate.get_current_room().remove_object_from_room(room_object)
                    self.gamestate.player.add_object_to_inventory(room_object)
                    wprint(PICKUP_SUCCESS_PREFIX + self.verb_noun_name + PICKUP_SUCCESS_SUFFIX)
                    take_success = True
                elif room_object.get_cost() > 0:
                    wprint(PICKUP_NOT_FREE)
            # Otherwise failed:
            else:
                wprint(PICKUP_FAILURE_PREFIX + self.verb_noun_name + PICKUP_FAILURE_SUFFIX)

        if take_success:
            self.gamestate.update_time_left(TAKE_COST)

        self.ui.wait_for_enter()
        return take_success

    def verb_use(self, noun_name, noun_type):
        use_success = True

        if noun_type == NOUN_TYPE_FEATURE:
            wprint("You cannot use that.")
            use_success = False
        elif noun_type == NOUN_TYPE_OBJECT:
            used_object = self.gamestate.player.inventory.get_object_by_name(noun_name)

            if used_object is not None:
                obj_label = used_object.get_name().lower()

                if obj_label == "crisp cash":
                    cash_gained = self.rand_event.get_random_cash_amount(CASH_CRISP_MIN, CASH_CRISP_MAX)
                    self.gamestate.player.update_cash(cash_gained)
                    self.gamestate.player.remove_object_from_inventory(used_object)
                    wprint(USE_CASH_SUCCESS_PREFIX + str(cash_gained) + USE_CASH_SUCCESS_SUFFIX)
                elif obj_label == "cash wad":
                    cash_gained = self.rand_event.get_random_cash_amount(CASH_WAD_CASH_MIN, CASH_WAD_CASH_MAX)
                    self.gamestate.player.update_cash(cash_gained )
                    self.gamestate.player.remove_object_from_inventory(used_object)
                    wprint(USE_CASH_SUCCESS_PREFIX + str(cash_gained) + USE_CASH_SUCCESS_SUFFIX)
                elif obj_label in {"graphics card", "ram chip", "floppy disk"}:
                    # TODO: Build logic to confirm player has all components to build a PC, in correct location to build one
                    # and then update some game-state variable so that player can do things they can do if they have a PC
                    g_card = self.gamestate.player.inventory.get_object_by_name("graphics card")
                    ram_chip = self.gamestate.player.inventory.get_object_by_name("ram chip")
                    floppy_disk = self.gamestate.player.inventory.get_object_by_name("floppy disk")

                    if g_card is not None and \
                         ram_chip is not None and \
                        floppy_disk is not None:
                        wprint(USE_COMPUTER_PARTS_SUCCESS)
                        self.ui.wait_for_enter()
                        self.gamestate.player.remove_object_from_inventory(g_card)
                        self.gamestate.player.remove_object_from_inventory(ram_chip)
                        self.gamestate.player.remove_object_from_inventory(floppy_disk)
                        self.gamestate.set_current_room(self.gamestate.get_room_by_name("Your Computer"))
                    else:
                        wprint(USE_COMPUTER_PARTS_MISSING)
                elif obj_label == "hackersnacks":
                    self.gamestate.player.remove_object_from_inventory(used_object)
                    self.gamestate.player.update_speed(SNACK_SPEED_INCREASE)
                    wprint(USE_SNACKS_SUCCESS)
                elif obj_label == "skateboard":
                    self.gamestate.player.set_has_skate_skill(True)
                    self.gamestate.player.remove_object_from_inventory(used_object)
                    self.gamestate.player.update_speed(SKATEBOARD_SPEED_INCREASE)
                    wprint(USE_SKATEBOARD_SUCCESS)
                elif obj_label == "spray paint":
                    self.gamestate.player.set_has_spraypaint_skill(True)
                    self.gamestate.player.remove_object_from_inventory(used_object)
                    wprint(USE_SPRAYPAINT_SUCCESS)
                elif obj_label == "hacker manual":
                    self.gamestate.player.set_has_hack_skill(True)
                    self.gamestate.player.remove_object_from_inventory(used_object)
                    wprint(USE_HACKERMANUAL_SUCCESS)
                elif obj_label == "surge":
                    self.gamestate.player.remove_object_from_inventory(used_object)
                    self.gamestate.player.update_speed(SNACK_SPEED_INCREASE)
                    wprint(USE_SURGE_SUCCESS)
                else:
                    logger.debug("Not implemented: use " + used_object.get_name())
                    wprint("You used something that the game doesn't know what to do with, please tell your local dev!")
                    use_success = False
            else:
                wprint(USE_FAIL)
                use_success = False

        if use_success:
            self.gamestate.update_time_left(USE_COST)

        self.ui.wait_for_enter()
        return use_success

    def verb_spraypaint(self, verb_object):
        # TODO: Implement this fully. Check that object/feature is spraypaintable and handle logic if not/fails
        # TODO: also chance of getting caught / going to jail or some other bad effect

        spraypaint_success = True

        if self.gamestate.player.can_spraypaint():
            wprint("TODO: You spraypaint stuff and coolness should go up and description should update. ")
            self.gamestate.player.update_coolness(SPRAYPAINT_COOLNESS_INCREASE)
        else:
            wprint("You need to [use Spray Paint] before you can try to spraypaint the world.")
            spraypaint_success = False

        if spraypaint_success:
            self.gamestate.update_time_left(SPRAYPAINT_COST)

        self.ui.wait_for_enter()
        return spraypaint_success

    def verb_steal(self, noun_name, noun_type):
        steal_success = False

        if noun_type == NOUN_TYPE_FEATURE:
            wprint("You cannot steal that.")
            steal_success = False

        elif noun_type == NOUN_TYPE_OBJECT:

            room_object = self.gamestate.get_current_room().get_object_by_name(noun_name)

            if room_object is not None:
                if room_object.is_owned_by_player() is True:
                    wprint(STEAL_FAIL_ALREADY_OWNED)
                elif room_object.get_cost() is 0:
                    wprint(STEAL_FAIL_FREE_ITEM)
                elif room_object.get_cost() > 0:
                    if (self.rand_event.attempt_steal() is True):
                        self.gamestate.get_current_room().remove_object_from_room(room_object)
                        self.gamestate.player.add_object_to_inventory(room_object)
                        wprint(STEAL_SUCCESS_PREFIX + room_object.get_name() + STEAL_SUCCESS_SUFFIX)
                        steal_success = True
                        self.gamestate.update_time_left(STEAL_COST)
                    else:
                        wprint(STEAL_FAIL_PRISON)
                        self.gamestate.update_time_left(STEAL_COST) # Still took the time to try and steal it
                        self.go_to_jail()
                        return steal_success
            else:
                wprint(STEAL_FAIL_NOT_HERE)

        self.ui.wait_for_enter()
        return steal_success

    def send_command_to_parser(self):
        results = self.lp.parse_command(self.user_input)
        try:
            self.command = results.get_verb()
        except:
            self.command = INVALID_INPUT
        try:
            self.verb_noun_name = results.get_noun()['name']
        except:
            self.verb_noun_name = None
        try:
            self.verb_noun_type = results.get_noun()['type']
        except:
            self.verb_noun_type = None
        try:
            self.extras = results.get_extras()
        except:
            self.extras = None
        try:
            self.verb_preposition = results.get_preposition()
        except:
            self.verb_preposition = None
        try:
            self.parser_error_message = results.get_error_message()
        except:
            self.parser_error_message = None

    def search_trash_can(self):
        if self.gamestate.is_trash_can_looted is True:
            message = LOOK_AT_TRASH_CAN_ALREADY_LOOTED
        else:
            wprint(LOOK_AT_TRASH_CAN_PROMPT)
            confirm = self.ui.user_prompt().lower()
            if confirm in YES_ALIASES:
                message = LOOK_AT_TRASH_SEARCHED
                ram_chip = self.gamestate.get_object_by_name("RAM Chip")
                self.gamestate.player.add_object_to_inventory(ram_chip)
                self.gamestate.player.update_coolness(TRASH_CAN_SEARCH_COOLNESS_COST)
                self.gamestate.is_trash_can_looted = True
            else:
                message = LOOK_AT_TRASH_NOT_SEARCHED

        wprint(message)
        self.ui.wait_for_enter()
