# DELPHINUS - ADVENTURE APP
# CS 467 - Winter 2017
# Team Members: Sara Hashem, Shawn Hillyer, Niza Volair

# art.py
# Description: Object and related classes
# Principal Authors of this file: Sara Hashem & Shawn Hillyer

# CITATIONS
# CITE:

from fileio.room import *

from debug.debug import *

import json
import glob

class Art:
    '''
    Art for game objects. Printed to console alongside object names.
    '''
    def __init__(self, properties):
        if 'name' in properties:
            self.name = properties['name']
        if 'image' in properties:
            self.image = properties['image']

    def get_art(self):
        return self.image

class ArtBuilder:
    '''
    Generates object art and returns them to caller
    '''
    def __init__(self):
        pass

    def load_art_from_file(self, dir="./gamedata/art/*.json"):
        '''
        Called by GameClient to instantiate all of the objects. This is called whether the game is new
        or loaded. Returns ALL art as a list.
        '''
        art_list = []
        art_dir = dir
        art_files =  glob.glob(art_dir)

        # Load object content from directory
        for art in art_files:
            with open(art) as art:
                art_properties = json.load(art)
                new_art = Art(art_properties)
                art_list.append(new_art)

        return art_list