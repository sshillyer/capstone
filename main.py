#!/usr/bin/env python3

# DELPHINUS - ADVENTURE APP
# CS 467 - Winter 2017
# Team Members: Sara Hashem, Shawn Hillyer, Niza Volair

# game_client.py
# Description: GameClient class and closely-related classes
# Principal Author of this file per Project plan: Shawn Hillyer

# CITATIONS
# CITE: http://stackoverflow.com/questions/566746/how-to-get-console-window-width-in-python

from gameclient.game_client import *
from constants.game_engine_constants import *
from gameclient.game_client import UserInterface
import subprocess
# For debugging
from debug.debug import *

logger = logging.getLogger(__name__)


def main():
    '''
    Launches the game client and serves as an entry point
    :return:
    '''

    # Check terminal dimensions before running game
    ui = UserInterface()
    if ui.op_system == "Linux":
        rows, cols = get_terminal_dimensions()
        if is_minimum_terminal_size(rows, cols) is not True:
            print_minimum_terminal_size_error(MIN_ROWS, MIN_COLS)
            sys.exit(1)
    elif ui.op_system == "Windows":
        # TODO Not critical for assignment as we must run on LINUX but can still implement this
        pass

    GC = GameClient()
    GC.main_loop()

def get_terminal_dimensions():
    # uses the 'stty size' linux command to get the terminal's size (num rows/cols)
    return subprocess.check_output(['stty', 'size']).split()

def is_minimum_terminal_size(rows, cols):
    # Minimums are defined in constants.constants module
    if int(rows) >= int(MIN_ROWS) and int(cols) >= int(MIN_COLS):
        return True
    return False

def print_minimum_terminal_size_error(rows, cols):
    print("The minimum terminal size is " + str(rows) + " rows and " + str(cols) + " columns. \nResize your terminal and try launching again.")

if __name__ == "__main__": main()
