#!/usr/bin/env python3

# DELPHINUS - ADVENTURE APP
# CS 467 - Winter 2017
# Team Members: Sara Hashem:, Shawn Hillyer, Niza Volair

# game_client.py
# Description: GameClient class and closely-related classes
# Principal Author of this file per Project plan: Shawn Hillyer

# CITATIONS
# CITE:

from gameclient.game_client import *

# For debugging
from debug.debug import *
logger = logging.getLogger(__name__)


def main():
    '''
    Launches the game client and serves as an entry point
    :return:
    '''

    # TODO: Implement some code that checks if the screen height and width meets some minimum requirement. Note sure
    # if we have a min h/w requirement or not yet
    logger.debug("Entering main() loop")
    GC = GameClient()



if __name__ == "__main__": main()
