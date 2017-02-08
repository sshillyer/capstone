# DELPHINUS - ADVENTURE APP
# CS 467 - Winter 2017
# Team Members: Sara Hashem, Shawn Hillyer, Niza Volair

# wprint.py
# Description: One-off function to word-wrap paragraphs when desired
# Principal Author of this file per Project plan: Shawn Hillyer

from constants.constants import TEXT_WIDTH
import textwrap


def wprint(raw_string):
    print(textwrap.fill(raw_string, TEXT_WIDTH))