# DELPHINUS - ADVENTURE APP
# CS 467 - Winter 2017
# Team Members: Sara Hashem, Shawn Hillyer, Niza Volair

# user_interface.py
# Description: UserInterface functions for basic termina IO
# Principal Author of this file per Project plan: Shawn Hillyer

# CITATIONS
# CITE: http://stackoverflow.com/questions/4810537/how-to-clear-the-screen-in-python
# CITE: http://stackoverflow.com/questions/110362/how-can-i-find-the-current-os-in-python


import platform
from fileio.save_game import *
from gameclient.player import *
from gameclient.wprint import *

from debug.debug import *
logger = logging.getLogger(__name__)

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
            # logger.debug("System is Linux")
            self.op_system = 'Linux'
        elif operating_system == 'Windows':
            # logger.debug("System is Windows")
            self.op_system = 'Windows'


    def print_introduction(self):
        wprint(INTRO_STRING)

    def print_main_menu(self):
        for line in MAIN_MENU_LINES:
            wprint(line)

    def user_prompt(self):
        user_input = input(self.prompt_text)
        return user_input

    def print_help_message(self):
        for line in HELP_MESSAGE:
            wprint(line) # Don't use wprint here, prefer linebreaks as defined in strings.py
        self.wait_for_enter()

    def print_quit_confirm(self, message):
        wprint(message)

    def clear_screen(self):
        # Cite: http://stackoverflow.com/questions/4810537/how-to-clear-the-screen-in-python
        if self.op_system == "Windows":
            os.system('cls')
        elif self.op_system == "Linux":
            os.system('clear')
        else:
            pass

    def print_splash_screen_new_game(self):
        self.clear_screen()
        wprint(NEW_GAME_MESSAGE)  # Defined in constants\strings.py
        self.wait_for_enter()

    def print_splash_screen_load_game(self):
        self.clear_screen()
        wprint(LOAD_GAME_SPLASH)
        self.wait_for_enter()

    def saved_game_splash_screen(self):
        self.clear_screen()
        wprint(LOAD_GAME_MESSAGE)  # Defined in constants\strings.py
        self.wait_for_enter()

    def print_status_header(self, info):
        wprint(STATUS_HEADER_BAR)
        wprint(STATUS_HEADER_LOCATION_LABEL + str(info['current_room']))
        wprint(STATUS_HEADER_SPEED_LABEL + str(info['speed']) + STATUS_HEADER_TIME_LABEL + str(info['time_left']))
        wprint(STATUS_HEADER_COOLNESS_LABEL  + str(info['coolness']) + STATUS_HEADER_CASH_LABEL + str(info['cash']))

        # conditionally print player's acquired abilities if they have them
        skills_row_text = STATUS_HEADER_SKILLS_LABEL
        has_hack_skill = info['hack_skill']
        has_skate_skill = info['skate_skill']
        has_spraypaint_skill = info['spraypaint_skill']

        if has_hack_skill is False and has_skate_skill is False and has_spraypaint_skill is False:
            # logger.debug(has_hack_skill + has_spraypaint_skill + has_skate_skill)
            skills_row_text += STATUS_NO_SKILLS
        if has_hack_skill is True:
            skills_row_text +=  "hack\t"
        if has_skate_skill is True:
            skills_row_text += "skate\t"
        if has_spraypaint_skill is True:
            skills_row_text += "spraypaint\t"
        wprint(skills_row_text)

        wprint(STATUS_HEADER_BAR)

    def wait_for_enter(self):
        input(PRESS_KEY_TO_CONTINUE_MSG)
        self.clear_screen()

    def print_room_description(self, description):
        wprint(DESCRIPTION_HEADER)
        print(description) # Don't use wprint here or it will remove linebreaks

    def print_inventory(self, inventory_description):
        wprint(INVENTORY_LIST_HEADER)
        print(inventory_description)
        wprint(INVENTORY_LIST_FOOTER)