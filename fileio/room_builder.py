# DELPHINUS - ADVENTURE APP
# CS 467 - Winter 2017
# Team Members: Sara Hashem:, Shawn Hillyer, Niza Volair

# room_builder.py
# Description:
# Principal Author of this file per Project plan: Sara Hashem

# CITATIONS
# CITE:

from gameclient.room import *

from debug.debug import *
logger = logging.getLogger(__name__)

import json
from pprint import pprint


class RoomBuilder:
    '''
    This class is designed to build a room or multiple rooms from files

    Todo: Read all files from gamedata/rooms and append them to rooms before returning it
    Game-engine presently assumes first room in the list is the starting room, this is probably
    "bad" solution -- if order of file read changes, let Shawn know. Plan is to set current room to
    "Street" room so I can just update the initialization to look up that room first. -- SSH
    '''
    def __init__(self):
        logger.debug("RoomBuilder instantiated")

    def load_room_data_from_file(self):
        '''
        Called by GameEngine to instantiate all of the rooms. This is called whether the game is new
        or loaded. Should return ALL rooms.
        :return:
        '''
        rooms = []

        # Could refactor this out as a method that is then called on each file in the folder if desired
        with open('./gamedata/rooms/street.json') as sample_room:
            room_properties = json.load(sample_room)
            new_room = Room(room_properties)
            rooms.append(new_room)
        # pprint(rooms)

        return rooms



    # TODO: DEPRECATED: Can probably just delete this build_rooms_from_code method now
    def build_rooms_from_code(self):
        '''
        DEPRECATED

        Method for use in testing game engine and demonstrates how the features and rooms could be parsed
        from a file; would be useful if we were hard-coding the values. Could also convert to the real
        file loader by replacing static strings with information from various file-read operations
        :return:
        '''


        # TODO: Create loop (or massive switch statement) to determine which item to parse

        # Parse long descriptions from input file
        with open('long_descriptions.json') as long_descriptions:
            rooms = json.load(long_descriptions)
        # DEBUG
        pprint(rooms[0])

        # Parse feature descriptions from input file
        with open('features.json') as features:
            features = json.load(features)
        #DEBUG
        pprint(features[0])


        street_feature_1 = RoomFeature(features[0]["features"][0])
        street_feature_2 = RoomFeature(features[0]["features"][1])


        # TODO: Add connection links to room_properties

        street_connection_1_properties = {
                'label': 'Arcade',
                'cardinal_direction': 'North',
                'description': "an exciting sign for an arcade",
                'destination': 'Arcade'
        }
        street_connection_1 = RoomConnection(street_connection_1_properties)


        # TODO: Create room_properties as pre-built JSON

        street_properties = {
            'room_features' : [street_feature_1, street_feature_2],
            'long_description' : rooms[0]["description"],
            'short_description' : "Short description here... You're standing on the street",
            'visited' : False,
            'room_connections' : [street_connection_1]
        }

        street = Room(street_properties)
        rooms =  [ street ]
        return rooms

