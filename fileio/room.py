# DELPHINUS - ADVENTURE APP
# CS 467 - Winter 2017
# Team Members: Sara Hashem, Shawn Hillyer, Niza Volair

# room.py
# Description:
# Principal Author of this file per Project plan: Sara Hashem and Shawn Hillyer

# CITATIONS
# CITE: http://askubuntu.com/questions/352198/reading-all-files-from-a-directory
# CITE: http://pythonfiddle.com/
# CITE: https://jsonformatter.curiousconcept.com/

from constants.strings import *
from constants.game_engine_constants import *
from fileio.object import *
import textwrap

from debug.debug import *

logger = logging.getLogger(__name__)

import json
import glob
import copy


class Room:
    '''
    Specifications: A room has at least 2 features, a long and short long_description, and has either been visited or not.

    Each room can have 1 or more room connections, each of which must be able to be accessed by typing
    the name for that connection, the cardinal direction, and various combinations of either ('go' in front is optional).

    The room features are encapsulated as they can be examined by typing in their name. This gives a long_description.

    Rooms can also have objects in them that can be picked up or dropped by the player.
    '''

    def __init__(self, properties):
        # Ensure properties exist then read them into instance of Room verb_object
        if properties:
            self.name = properties['name']
            self.long_description = properties['long_description']
            self.short_description = properties['short_description']
            self.visited = properties['visited']
            self.virtual_space = properties['virtual_space']

            # Call constructors from features and connections and append them to the Room
            self.room_features = []
            for feature_properties in properties['room_features']:
                room_feature = RoomFeature(feature_properties)
                self.room_features.append(room_feature)

            self.room_connections = []
            for room_connection_properties in properties['room_connections']:
                room_connection = RoomConnection(room_connection_properties)
                self.room_connections.append(room_connection)
            # Room starts with no objects. The ObjectBuilder class makes the objects, the new game or load game initializers
            # are responsible for populating the rooms/inventory with objects
            self.objects = []

    def get_name(self):
        return self.name

    def get_long_description(self):
        '''
        Get the "long long_description" version of the room's long_description
        :return: string representing full length long_description
        '''
        # full_description = textwrap.fill(self.long_description, TEXT_WIDTH, replace_whitespace=False) + "\n" + self.get_supplemental_description()
        full_description = textwrap.fill(self.long_description, TEXT_WIDTH) + "\n" + self.get_supplemental_description()
        return full_description

    def get_short_description(self):
        '''
        Get the "short long_description" version of the room's long_description
        :return: string representing shortened long_description used after a room has been visited (visited is True)
        '''
        full_description = textwrap.fill(self.short_description, TEXT_WIDTH) +"\n" + self.get_supplemental_description()
        return full_description

    def get_supplemental_description(self):
        '''
        Get a string of all the connections, features, and objects in the Room
        :return: string
        '''
        description = "\n" + FEATURES_HEADER + "\n" + self.get_feature_list_string() + "\n" + OBJECTS_HEADER + "\n" + self.get_object_list_string() + "\n" + EXITS_HEADER + "\n" + self.get_connection_string()
        return description

    def get_connection_string(self):
        '''
        Return a string of all the connections in the room
        :return: string
        '''
        connection_string = ""
        if self.room_connections:
            for connection in self.room_connections:
                connection_string = connection_string + textwrap.fill(connection.get_connection_description(), TEXT_WIDTH) + "\n"
        return connection_string

    def get_object_list_string(self):
        '''
        Returns a string that describes the interesting objects in the environment.
        Called by get_long_description
        :return:
        '''
        if self.objects:
            objects_string = ""
            for object in self.objects:
                objects_string = objects_string + textwrap.fill(object.get_environmental_description(), TEXT_WIDTH) + "\n"
        else:
            objects_string = NO_INTERESTING_OBJECTS_MESSAGE
        return objects_string

    def get_feature_list_string(self):
        '''
        Returns a string that describes the interesting features in the environment.
        Called by get_long_description
        :return:
        '''
        feature_string = ""
        for feature in self.room_features:
            feature_string = feature_string + textwrap.fill(feature.get_feature_list_label(), TEXT_WIDTH) + "\n"
        return feature_string

    def set_visited(self, visited=True):
        '''
        Sets whether the room has been visited or not
        :return:
        '''
        self.visited = visited

    def get_feature_by_name(self, feature_name):
        '''
        If the feature is in the room, returns that Feature. Called by gameclient for 'look at' verb
        :param feature_name: string. The name of the feature being searched for
        :return: The feature itself or null
        '''
        for room_feature in self.room_features:
            # logger.debug("Checking if " + room_feature.get_name().lower() + " is " + feature.lower() + "...")
            if room_feature.get_name().lower() == feature_name.lower():
                logger.debug("Match found!")
                return room_feature
            # else:
            #     logger.debug("Not a match!")

        # If the room does not have a feature with that name, return None
        return None

    def get_object_by_name(self, object_name):
        '''
        Return reference to an verb_object looked up by name if it exists in the room
        :param object_name:
        :return:
        '''
        for room_object in self.objects:
            if room_object.get_name().lower() == object_name.lower():
                return room_object
        return None

    def add_object_to_room(self, object):
        copy_of_object = copy.copy(object)
        self.objects.append(copy_of_object)

    def remove_object_from_room(self, object):
        self.objects.remove(object)

    # TODO: This method is never called as of 2-17-2017, commenting out. Can uncomment later if needed.
    # def remove_object_from_room_by_name(self, object_name):
    #     object_to_remove = self.get_object_by_name(object_name)
    #     if object_to_remove is not None:
    #         self.remove_object_from_room(object_to_remove)
    #         return True
    #     return False

    # TODO: Deprecated. Delete if never used. --SSH
    # def set_objects(self, object_list):
        # Used by initialize_gamestate() method in GameState class
        # self.objects = object_list

    def is_visited(self):
        return self.visited

    def set_is_visited(self, is_visited=True):
        self.visited = is_visited

    def is_virtual_space(self):
        return self.virtual_space


class RoomFeature:
    '''
    A feature of a room. Each room has a minimum of two features that can be examined

    Per Specification:
    Each room must have at least two "features" that can be examined (a fish on the ground, lightning bolts in the sky,
    a wooden chair, a smoky smell, etc.).
    '''

    def __init__(self, properties):
        self.name = properties['name']
        self.description = properties['description']
        self.hackable = properties['hackable']
        if self.hackable is True:
            self.description_hacked = properties['description_hacked']
        else:
            self.description_hacked = self.description # Shouldn't need this - here as a failsafe
        self.hacked = False

    def get_name(self):
        return self.name

    def get_description(self):
        if self.is_hacked() is True:
            return self.description_hacked
        else:
            return self.description


    def get_feature_list_label(self):
        '''
        Get the string for room features
        :return: string
        '''
        description = FEATURES_LIST_PREFIX + "[" + self.name + "]"
        return description

    def is_hackable(self):
        return self.hackable

    def is_hacked(self):
        return self.hacked

    def set_is_hacked(self, hacked=True):
        self.hacked = hacked

class RoomConnection:
    '''
    Per Specifications:
    Exits from a room must be described in both the short-form and long-form descriptions, and should include a
    direction. For example: "There is a dank-smelling staircase, descending into the dark, at the end of the hall on
    the north wall", or "I can see clouds to the east and west that I think I can jump to from here".
    '''

    def __init__(self, properties):
        self.label = properties['label']
        self.cardinal_direction = properties['cardinal_direction']
        self.description = properties['description']
        self.destination = properties['destination']

    def get_connection_description(self):
        '''
        Get the sting as required per specifications for this particular connection
        :return: string
        '''
        description = CONNECTION_LIST_PREFIX + self.cardinal_direction + CONNECTION_LIST_SEGWAY + self.description + ". [" + self.label + "]"
        return description


class RoomBuilder:
    '''
    This class is designed to build a room or multiple rooms from files
    '''
    def __init__(self):
        # logger.debug("RoomBuilder instantiated")
        pass

    def load_room_data_from_file(self, dir="./gamedata/rooms/*.json"):
        '''
        Called by GameClient to instantiate all of the rooms. This is called whether the game is new
        or loaded. Returns ALL rooms as a list.
        '''
        rooms = []
        rooms_dir = dir
        rooms_files =  glob.glob(rooms_dir)

        # Load room content from directory
        for room in rooms_files:
            with open(room) as room:
                room_properties = json.load(room)
                new_room = Room(room_properties)
                rooms.append(new_room)

        return rooms
