# DELPHINUS - ADVENTURE APP
# CS 467 - Winter 2017
# Team Members: Sara Hashem, Shawn Hillyer, Niza Volair

# save_game.py
# Description: SaveGame class. Encapsulates all of the data needed from the GameState class or a file to save/load data
# Principal Author of this file per Project plan: Shawn Hillyer

# CITATIONS
# CITE: http://stackoverflow.com/questions/4810537/how-to-clear-the-screen-in-python
# CITE: http://stackoverflow.com/questions/110362/how-can-i-find-the-current-os-in-python
# CITE: http://stackoverflow.com/questions/7935972/writing-to-a-new-directory-in-python-without-changing-directory
# CITE: http://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file-using-python
# CITE: http://stackoverflow.com/questions/30876497/open-a-file-from-user-input-in-python-2-7

from constants.gameplay_settings import STARTING_TIME
import json
import glob
import os

class SaveGame:
    def __init__(self, gamestate):
        '''
        Instantiate a SaveGame from the gamestate data passed in
        If None is passed in, this constructor does nothing. Instead, call load_from_file() to load up the SaveGame
        with data which can then be accessed by calling various methods
        :param gamestate:
        '''

        # These must be defined - the only reason I give them values here is so that I can test the loadgame/savegame
        # methods without having them actually read/write from/to real files
        if gamestate is not None:
            # Room information and objects in each room
            self.current_room_name = gamestate.get_current_room().get_name()
            try:
                self.prior_room = gamestate.get_prior_room().get_name()
            except:
                self.prior_room = ""

            self.visited_rooms = []
            self.object_room_mapping = {}
            self.features_hacked_mapping = {}
            for room in gamestate.rooms:
                if room.is_visited():
                    self.visited_rooms.append(room.get_name())

                # Grab all the objects for *this specific room* and add to a list, then append that to dictionary
                room_objects = []
                for room_object in room.objects:
                    room_objects.append(room_object.get_name())
                self.object_room_mapping[room.get_name()] = room_objects

                # Remember which room features have been hacked
                hacked_features = []
                for room_feature in room.room_features:
                    if room_feature.is_hackable() is True:
                        self.features_hacked_mapping[room.get_name()] = { room_feature.get_name() : room_feature.is_hacked() }


            # Special booleans
            self.is_trash_can_looted = gamestate.is_trash_can_looted

            # Objects in inventory
            self.player_inventory = []
            for inventory_object in gamestate.player.get_inventory_objects():
                self.player_inventory.append(inventory_object.get_name())

            # Player variables
            self.player_cash = gamestate.player.get_cash()
            self.player_coolness = gamestate.player.get_coolness()
            self.player_speed = gamestate.player.get_speed()
            self.player_has_hack_skill = gamestate.player.can_hack()
            self.player_has_skate_skill = gamestate.player.can_skateboard()
            self.player_has_spraypaint_skill = gamestate.player.can_spraypaint()

            # Other variables stored in GameState
            self.time_left = gamestate.get_time_left()


    def write_to_file(self, filename):
        '''
        SAVING A SAVEGAME FROM GAMESTATE
            A SaveGame would be instantiated when a player chooses to 'save' their game. Pass in the gamestate object
            from the GameClient and then parse through the object looking for the relevant data to save to file.

            Once a SaveGame object is instantiated, you can call write_to_file() method to save the data.
        '''
        saved_dir = './gamedata/savedgames/'
        filename = filename

        json_savegame = {
            'current_room' : self.current_room_name,
            'prior_room': self.prior_room,
            'visited_rooms': self.visited_rooms,
            'hacked_features' : self.features_hacked_mapping,

            # Special booleans
            'is_trash_can_looted': self.is_trash_can_looted,

            # Objects in rooms and inventory
            'objects_in_rooms': self.object_room_mapping,
            'player_inventory': self.player_inventory,

            # Player variables
            'player_cash': self.player_cash,
            'player_coolness': self.player_coolness,
            'player_speed': self.player_speed,
            'player_has_hack_skill': self.player_has_hack_skill,
            'player_has_skate_skill': self.player_has_skate_skill,
            'player_has_spraypaint_skill': self.player_has_spraypaint_skill,

            # Other variables stored in GameState
            'time_left': self.time_left
        }

        with open(os.path.join(saved_dir, filename), 'w') as saved_game_file:
            json.dump(json_savegame, saved_game_file)

        write_successful = True

        return write_successful


    def load_from_file(self, filename):
        '''
        LOADING A SAVEGAME FROM FILE
            Instead, call the load_from_file() method. This will populate the SaveGame object with the necessary
            data. The GameState class will simply create a SaveGame object, call load_from_file(), then use the SaveGame
            to parse it for the data it wants and handle the logic of "repopulating" the GameState so that it matches
            the original savegame in a similar fashion as write_to_file
        '''
        filename = './gamedata/savedgames/' + filename
        self.save_data = {}
        with open(filename, 'r') as savedgame:
            self.save_data = json.load(savedgame)

        # Room information
        self.current_room_name = self.save_data['current_room']
        self.visited_rooms = self.save_data['visited_rooms']
        self.prior_room = self.save_data['prior_room']

        # Hacked features
        self.features_hacked_mapping = self.save_data['hacked_features']

        # Special booleans
        self.is_trash_can_looted = self.save_data['is_trash_can_looted']

        # Objects in rooms and inventory
        self.object_room_mapping = self.save_data['objects_in_rooms']
        self.player_inventory = self.save_data['player_inventory']

        # Player variables
        self.player_cash = self.save_data['player_cash']
        self.player_coolness = self.save_data['player_coolness']
        self.player_speed = self.save_data['player_speed']
        self.player_has_hack_skill = self.save_data['player_has_hack_skill']
        self.player_has_skate_skill = self.save_data['player_has_skate_skill']
        self.player_has_spraypaint_skill = self.save_data['player_has_spraypaint_skill']

        # Other variables stored in GameState
        self.time_left = self.save_data['time_left']

    def get_current_room(self):
        try:
            return self.current_room_name
        except:
            return "Street"

    def get_hacked_feature_mapping(self):
        try:
            return self.features_hacked_mapping
        except:
            return False

    def get_is_trash_can_looted(self):
        try:
            return self.is_trash_can_looted
        except:
            return False

    def get_player_cash(self):
        try:
            return self.player_cash
        except:
            return 0

    def get_player_coolness(self):
        try:
            return self.player_coolness
        except:
            return 0

    def get_player_has_hack_skill(self):
        try:
            return self.player_has_hack_skill
        except:
            return False

    def get_player_has_skate_skill(self):
        try:
            return self.player_has_skate_skill
        except:
            return False

    def get_player_has_spraypaint_skill(self):
        try:
            return self.player_has_spraypaint_skill
        except:
            return False

    def get_player_speed(self):
        try:
            return self.player_speed
        except:
            return None

    def get_objects_room_mapping(self):
        try:
            return self.object_room_mapping
        except:
            return None

    def get_player_inventory(self):
        try:
            return self.player_inventory
        except:
            return None

    def get_prior_room(self):
        try:
            if self.prior_room == "":
                return None
            else:
                return self.prior_room
        except:
            return None

    def get_time_left(self):
        try:
            return self.time_left
        except:
            return None

    def get_visited_rooms_list(self):
        try:
            return self.visited_rooms
        except:
            return None

    def is_valid_saved_game(self, file_name):
        '''
        Pass in a string and validate if the filename is valid
        Invalid might be because string is an invalid filename in the op system or some other reason(s)
        :param file_name:
        :return: True if filename is valid, False if not valid
        '''
        savedgames = self.get_savegame_filenames()

        for savedgame in savedgames:
            if str(savedgame) == str(file_name):
                return True

        return False

    def is_existing_saved_game(self, file_name):
        '''
        Pass in a string and validate if the filename is valid
        Invalid might be because string is an invalid filename in the op system or some other reason(s)
        :param file_name:
        :return: True if filename is does not already exist, False if exists
        '''
        savedgames = self.get_savegame_filenames()

        for savedgame in savedgames:
            if str(savedgame) == str(file_name):
                return False

        return True

    @staticmethod
    def get_savegame_filenames():
        '''
        Returns a list of the filenames in the savegame folder
        :return: All files in the savedgame folder
        '''
        # TODO: Implement this
        savedgames = []
        savedgames_dir = './gamedata/savedgames/*.json'
        savedgames_files_path =  glob.glob(savedgames_dir)

        # Trim preceding path from filename strings
        savedgames_files = []
        for file in savedgames_files_path:
            file = file[22:]
            savedgames_files.append(file)

        # Load saved game content from directory
        for savedgame in savedgames_files_path:
            with open(savedgame) as savedgame:
                savedgames.append(savedgame)

        return savedgames_files


