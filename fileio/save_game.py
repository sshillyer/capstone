# DELPHINUS - ADVENTURE APP
# CS 467 - Winter 2017
# Team Members: Sara Hashem, Shawn Hillyer, Niza Volair

# save_game.py
# Description: SaveGame class. Encapsulates all of the data needed from the GameState class or a file to save/load data
# Principal Author of this file per Project plan: Shawn Hillyer

# CITATIONS
# CITE: http://stackoverflow.com/questions/4810537/how-to-clear-the-screen-in-python
# CITE: http://stackoverflow.com/questions/110362/how-can-i-find-the-current-os-in-python

class SaveGame:
    def __init__(self, gamestate):
        '''
        Instantiate a SaveGame from the gamestate data passed in
        If None is passed in, this constructor does nothing. Instead, call load_from_file() to load up the SaveGame
        with data which can then be accessed by calling various methods
        :param gamestate:
        '''

        # TODO: Write UNIT TESTS for this code, entirely untested
        if gamestate:
            # As of 1/29, the useful gamestate data includes:
            # * The current room
            self.current_room = gamestate.get_current_room().get_name()
            # * What rooms have been visited
            self.visited_rooms = []
            # * What objects are in each Room's .object's properties
            self.objects_in_rooms = {}
            # * What objects are in the player's inventory
            self.player_inventory = []
            # * The player's various stats (speed, coolness, etc.)

            for room in gamestate.rooms:
                if room.is_visited():
                    self.visited_rooms.append(room.get_name())

                # Grab all the objects for *this specific room* and add to a list, then append that to dictionary
                room_objects = []
                for room_object in room.objects:
                    room_objects.append(room_object)
                self.objects_in_rooms[room.get_name()] = room_objects

            # Read the player's inventory
            for inventory_object in gamestate.player.get_inventory_objects():
                self.player_inventory.append(inventory_object)



    def write_to_file(self, filename):
        '''
        SAVING A SAVEGAME FROM GAMESTATE
            A SaveGame would be instantiated when a player chooses to 'save' their game. Pass in the gamestate object
            from the GameClient and then parse through the object looking for the relevant data to save to file.

            Once a SaveGame object is instantiated, you can call write_to_file() method to save the data.
        '''
        pass

    def load_from_file(self, filename):
        '''
        LOADING A SAVEGAME FROM FILE
            Instead, call the load_from_file() method. This will populate the SaveGame object with the necessary
            data. The GameState class will simply create a SaveGame object, call load_from_file(), then use the SaveGame
            to parse it for the data it wants and handle the logic of "repopulating" the GameState so that it matches
            the original savegame in a similar fashion as write_to_file
        '''
        pass

    def get_visited_rooms_list(self):
        return self.visited_rooms

    def get_objects_in_rooms(self):
        return self.objects_in_rooms

    def get_player_inventory(self):
        return self.player_inventory

    def get_current_room(self):
        return self.current_room