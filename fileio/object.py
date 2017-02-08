# DELPHINUS - ADVENTURE APP
# CS 467 - Winter 2017
# Team Members: Sara Hashem, Shawn Hillyer, Niza Volair

# verb_object.py
# Description: Object and related classes
# Principal Author*** of this file per Project plan: Shawn Hillyer
#  *** The code for ObjectBuilder is essentially the same as what Sara wrote for RoomBuilder method

# CITATIONS
# CITE:

from fileio.room import *

from debug.debug import *
logger = logging.getLogger(__name__)

import json
import glob
import pprint

class Object:
    '''
    A game object. Can be in a Room or players inventory.
     Can be picked up from a room, dropped in a room, used, 'look at'ed, and possibly other actions
    '''
    def __init__(self, properties):
        # logger.debug(properties)
        if 'name' in properties:
            self.name = properties['name']
        if 'long_description' in properties:
            self.long_description = properties['long_description']
        if 'short_description' in properties:
            self.short_description = properties['short_description']
        if 'default_location' in properties:
            self.default_location = properties['default_location']
        if 'cost' in properties:
            self.cost = properties['cost']

        # So a player isn't forced to steal or buy an object more than once
        if self.default_location == "inventory":
            self.owned_by_player = True
        else:
            self.owned_by_player = False

    def get_long_description(self):
        return self.long_description

    def get_short_description(self):
        return self.short_description

    def get_name(self):
        return self.name

    def get_default_location_name(self):
        if self.default_location:
            return self.default_location
        return None

    def get_cost(self):
        return self.cost

    def get_environmental_description(self):
        description = OBJECTS_LIST_PREFIX + "[" + self.get_name() + "]"
        return description

    def set_is_owned_by_player(self, is_owned_by_player = True):
        '''
        :param is_owned_by_player: Boolean. True if player has acquired the object at some point (buy, take, stolen)
        '''
        self.owned_by_player = is_owned_by_player

    def is_owned_by_player(self):
        return self.owned_by_player

class ObjectBuilder:
    '''
    Generates objects and returns them to caller
    '''
    def __init__(self):
        pass

    def load_object_data_from_file(self):
        '''
        Called by GameClient to instantiate all of the objects. This is called whether the game is new
        or loaded. Returns ALL objects as a list.
        '''
        object_list = []
        objects_dir = './gamedata/objects/*.json'
        objects_files =  glob.glob(objects_dir)

        # Load object content from directory
        for object in objects_files:
            with open(object) as object:
                object_properties = json.load(object)
                new_object = Object(object_properties)
                object_list.append(new_object)


        return object_list