# DELPHINUS - ADVENTURE APP
# CS 467 - Winter 2017
# Team Members: Sara Hashem, Shawn Hillyer, Niza Volair

# object.py
# Description: Object and related classes
# Principal Author of this file per Project plan: Shawn Hillyer

# CITATIONS
# CITE:

class Object:
    '''
    An object. Can be in a Room or players inventory.
     Can be picked up from a room, dropped in a room, used, 'look at'ed, and possibly other actions
    '''
    def __init__(self, properties):
        if properties['name']:
            self.name = properties['name']
        if properties['description']:
            self.description = properties['description']
        if properties['default_location']:
            self.default_location = properties['default_location']

    def get_description(self):
        return self.description

    def get_name(self):
        return self.name

    def get_default_location_name(self):
        return self.default_location

    def get_environmental_description(self):
        # TODO: Refine the output of this function somewhat? Could give objects unique environmental descriptions but
        # TODO: 1depending on the room they are in it wouldn't make sense once dropped somewhere else(SSH)
        description = "You see a " + self.name + " in the area."
        return description

class ObjectBuilder:
    '''
    Generates objects and returns them to caller
    '''
    def __init__(self):
        pass

    def get_game_objects(self):
        all_objects = []

        skateboard = Object({
            'name' : 'Skateboard',
            'description' : 'A trendy skateboard with the text \'Z3R0 C007\' inked on its surface',
            'default_location' : 'Street'
        })


        all_objects.append(skateboard)

        return all_objects
