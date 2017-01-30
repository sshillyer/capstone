# DELPHINUS - ADVENTURE APP
# CS 467 - Winter 2017
# Team Members: Sara Hashem, Shawn Hillyer, Niza Volair

# player.py
# Description: Player and Inventory / related class(es)
# Principal Author of this file per Project plan: Shawn Hillyer

# CITATIONS
# CITE:

from constants.strings import *

class Player:
    '''
    Player stats and methods
    '''
    def __init__(self):
        self.cash = 0
        self.coolness = 0
        self.speed = 0
        self.inventory = Inventory()

    def add_object_to_inventory(self, object):
        self.inventory.add_object(object)

    def remove_object_from_inventory(self, object):
        self.inventory.remove_object(object)

    def get_inventory_string(self):
        return self.inventory.get_inventory_string()

    def get_inventory_objects(self):
        return self.inventory.objects




class Inventory:
    '''
    Objects and methods related to adding and removing them from inventory
    '''
    def __init__(self):
        self.objects = []

    def get_object_by_name(self, object_name):
        '''
        Finds an object in the inventory by name and returns a reference to it
        :param object_name:
        :return:
        '''
        # TODO: Test function
        for inventory_object in self.objects:
            if inventory_object.name.lower() == object_name.lower():
                return inventory_object
        return None


    def add_object(self, object):
        self.objects.append(object)


    def remove_object(self, object):
        self.objects.remove(object)

    def get_inventory_string(self):
        '''
        Get a comma-delineated list of the objects in the inventory
        :return:
        '''
        if self.objects:
            inventory_size = len(self.objects)
            count = 0
            inventory_string = ""
            for object in self.objects:
                count += 1
                inventory_string += object.get_name()
                if count is not inventory_size:
                    inventory_string += "\n"
            return inventory_string
        return INVENTORY_EMPTY
