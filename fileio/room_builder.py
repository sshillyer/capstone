# DELPHINUS - ADVENTURE APP
# CS 467 - Winter 2017
# Team Members: Sara Hashem, Shawn Hillyer, Niza Volair

# room_builder.py
# Description: RoomBuilder class generates list of room objects from individual files
# Principal Author of this file per Project plan: Sara Hashem

# CITATIONS
# CITE: http://askubuntu.com/questions/352198/reading-all-files-from-a-directory

from gameclient.room import *

from debug.debug import *
logger = logging.getLogger(__name__)

import json
import glob


class RoomBuilder:
    '''
    This class is designed to build a room or multiple rooms from files

    Todo: Read all files from gamedata/rooms and append them to rooms before returning it
    Game-engine presently assumes first room in the list is the starting room, this is probably
    "bad" solution -- if order of file read changes, let Shawn know. Plan is to set current room to
    "Street" room so I can just update the initialization to look up that room first. -- SSH
    '''
    def __init__(self):
        # logger.debug("RoomBuilder instantiated")
        pass

    def load_room_data_from_file(self):
        '''
        Called by GameClient to instantiate all of the rooms. This is called whether the game is new
        or loaded. Returns ALL rooms as a list.
        '''
        rooms = []
        rooms_dir = './gamedata/rooms/*.json'
        rooms_files =  glob.glob(rooms_dir)

        # Load room content from directory
        # TODO: Determine logical order; for now, based on Project Plan (hashems)
        for room in rooms_files:
            with open(room) as room:
                room_properties = json.load(room)
                new_room = Room(room_properties)
                rooms.append(new_room)

        # DEBUG
        # for i in rooms:
        #     print(i.name)

        return rooms
