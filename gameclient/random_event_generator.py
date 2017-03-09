# DELPHINUS - ADVENTURE APP
# CS 467 - Winter 2017
# Team Members: Sara Hashem, Shawn Hillyer, Niza Volair
#
# random_event_generator.py
# Description:     Used to generate / determine random event results within the game.
# Principal Author of this file per Project plan: Shawn Hillyer
#
# CITATIONS
# CITE: https://docs.python.org/3.3/library/random.html


import random
from constants.probabilities import *
from debug.debug import *
logger = logging.getLogger(__name__)

class RandomEventGenerator:
    '''
    Used to generate / determine random event results within the game.
    Anything that is randomized in the game should be seeded/randomized and returned from here
    '''
    def __init__(self):
        # Defined in constants/probabilities.py
        # 100 is 100% chance, 75 = 75 chance, etc.
        self.spraypaint_success_chance = SPRAYPAINT_SUCCESS_CHANCE
        self.steal_success_chance = STEAL_SUCCESS_CHANCE
        self.hack_success_chance = HACK_SUCCESS_CHANCE
        random.seed()

    def attempt_steal(self):
        num = random.randint(1,100)
        if num <= self.steal_success_chance:
            return True
        return False

    def attempt_hack(self):
        num = random.randint(1,100)
        if num <= self.hack_success_chance:
            return True
        return False

    def get_random_cash_amount(self, min_amount, max_amount):
        amount = random.randint(min_amount, max_amount)
        return amount

    def attempt_spraypaint(self):
        num = random.randint(1,100)
        if num <= self.spraypaint_success_chance:
            return True
        return False

    def coin_flip(self):
        num = random.randint(1,100)
        logger.debug("coin flip value: " + str(num))
        if num <= 50:
            return True
        return False