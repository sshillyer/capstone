# DELPHINUS - ADVENTURE APP
# CS 467 - Winter 2017
# Team Members: Sara Hashem, Shawn Hillyer, Niza Volair

# room.py
# Description: Room class and related / composite classes
# Principal Author of this file per Project plan: Shawn Hillyer

# CITATIONS
# CITE:

from stringresources.strings import *

from debug.debug import *
logger = logging.getLogger(__name__)


class Room:
    '''
    Specifications: A room has at least 2 features, a long and short description, and has either been visited or not

    Each room can have 0 or more room connections, each of which must be able to be accessed by typing
    the .name for that connection, the cardinal direction, and various combination of either. 'go' in front optional

    The room features are encapsulated as they can be examined by typing in their name and this gives a
    description.

    Rooms can also have objects in them that can be picked up or dropped by the player.

    '''
    def __init__(self, properties):
        # Ensure the properites exist then read them into instance of Room object
        if properties:
            self.name = properties['name']
            self.long_description = properties['long_description']
            self.short_description = properties['short_description']
            self.visited = properties['visited']

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
        Get the "long description" version of the room's description
        :return: string representing full length description
        '''
        full_description = self.long_description + self.get_supplemental_description()
        return full_description

    def get_short_description(self):
        '''
        Get the "short description" version of the room's description
        :return: string representing shortened description used after a room has been visited (visited is True)
        '''
        full_description = self.short_description + self.get_supplemental_description()
        return full_description

    def get_supplemental_description(self):
        '''
        Get a string of all the connections and objects in the Room
        :return: string
        '''
        description = "\nEXITS:\n" + self.get_connection_string() + "\nOBJECTS: \n" + self.get_object_list_string()
        return description

    def get_connection_string(self):
        '''
        Return a string of all the connections in the room
        :return: string
        '''
        connection_string = ""
        if self.room_connections:
            for connection in self.room_connections:
                connection_string = connection_string + connection.get_connection_description() + "\n"
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
                objects_string = objects_string + object.get_environmental_description()
        else:
            objects_string = NO_INTERESTING_OBJECTS_MESSAGE
        return objects_string


    def set_visited(self, visited = True):
        '''
        Sets whether the room has been visited or not
        :return:
        '''
        self.visited = visited

    def get_feature(self, feature):
        '''
        If the feature is in the room, returns that Feature. Called by gameclient for 'look at' verb
        :param feature: string. The name of the feature being searched for
        :return: The feature itself or null
        '''
        for room_feature in self.room_features:
            logger.debug("Checking if " + room_feature.get_name().lower() + " is " + feature.lower() +"...")
            if room_feature.get_name().lower() == feature.lower():
                logger.debug("Match found!")
                return room_feature
            else:
                logger.debug("Not a match!")

        # If the room does not have a feature with that name, return None
        return None

    def get_object_by_name(self, object_name):
        '''
        Return reference to an object looked up by name if it exists in the room
        :param object_name:
        :return:
        '''
        for room_object in self.objects:
            if room_object.get_name().lower() == object_name.lower():
                return room_object
        return None

    def add_object_to_room(self, object):
        self.objects.append(object)


    def remove_object_from_room(self, object):
        self.objects.remove(object)


    def remove_object_from_room_by_name(self, object_name):
        object_to_remove = self.get_object_by_name(object_name)
        if object_to_remove is not None:
            self.remove_object_from_room(object_to_remove)
            return True
        return False

    def set_objects(self, object_list):
        # Used by initialize_new_game() method in GameState class
        self.objects = object_list

    def is_visited(self):
        return self.visited


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

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description


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
        description = "To the [" + self.cardinal_direction + "] you see " + self.description + ". [" + self.label + "]."
        return description