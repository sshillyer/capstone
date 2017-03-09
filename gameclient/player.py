# DELPHINUS - ADVENTURE APP
# CS 467 - Winter 2017
# Team Members: Sara Hashem, Shawn Hillyer, Niza Volair

# player.py
# Description: Player and Inventory / related class(es)
# Principal Author of this file per Project plan: Shawn Hillyer

# CITATIONS
# CITE: https://docs.python.org/3.3/library/copy.html
#       Used to figure out how to make a shallow/deep copy of an object rather than just assigning a reference to an object

from constants.strings import *
from constants.language_words import RAM, ACMERAM, GRAPHICS_CARD, FLOPPY_DISK, NEW_LAPTOP
from gameclient.wprint import *
import copy

class Player:
    '''
    Player stats and methods
    '''
    def __init__(self):
        self.cash = 0
        self.coolness = 0
        self.speed = 0
        self.inventory = Inventory()
        self.owned = []
        self.has_hack_skill = False
        self.has_skate_skill = False
        self.has_spraypaint_skill = False

    def add_object_to_inventory(self, object):
        if object:
            copy_of_object = copy.copy(object)
            self.inventory.add_object(copy_of_object)
            self.owned.append(object.get_name())

    def remove_object_from_inventory(self, object):
        self.inventory.remove_object(object)

    def get_inventory_objects(self):
        return self.inventory.objects

    def get_owned_objects(self):
        return self.owned

    def get_cash(self):
        return self.cash

    def update_cash(self, cash_change):
        self.cash += int(cash_change)
        if cash_change > 0:
            change_direction = "increased"
        else:
            change_direction = "decreased"
            cash_change = int(-1 * cash_change)
        wprint("Your [Cash] " + change_direction + " by " + str(cash_change) +".")

    def update_speed(self, speed_change):
        self.speed += int(speed_change)
        if speed_change > 0:
            change_direction = "increased"
        else:
            change_direction = "decreased"
            speed_change = int(-1 * speed_change)
        wprint("Your [Speed] " + change_direction + " by " + str(speed_change) +".")

    def update_coolness(self, coolness_change):
        self.coolness += int(coolness_change)
        if coolness_change > 0:
            change_direction = "increased"
        else:
            change_direction = "decreased"
            coolness_change = int(-1 * coolness_change)
        wprint("Your [Coolness] " + change_direction + " by " + str(coolness_change) +".")

    def get_coolness(self):
        return self.coolness

    def get_speed(self):
        return self.speed

    def set_has_hack_skill(self, has_skill=True):
        self.has_hack_skill = has_skill

    def set_has_spraypaint_skill(self, has_skill=True):
        self.has_spraypaint_skill = has_skill

    def set_has_skate_skill(self, has_skill=True):
        self.has_skate_skill = has_skill

    def can_hack(self):
        return self.has_hack_skill

    def can_skateboard(self):
        return self.has_skate_skill

    def can_spraypaint(self):
        return self.has_spraypaint_skill

    def has_object_by_name(self, object_name):
        '''
        Used in a few different
        :param object_name:
        :return:
        '''
        player_inventory_objects = self.inventory.objects
        for inventory_object in player_inventory_objects:
            if inventory_object.get_name().lower() == object_name.lower():
                return True
        return False

    def has_computer_parts(self):

        if self.has_object_by_name(NEW_LAPTOP) is True:
            return True
        elif    self.has_ram() is True and \
                self.has_object_by_name(GRAPHICS_CARD) is True and \
                self.has_object_by_name(FLOPPY_DISK) is True:
            return True
        else:
            return False

    def has_ram(self):
        has_ram = self.has_object_by_name(RAM) or self.has_object_by_name(ACMERAM)
        return has_ram



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
        for inventory_object in self.objects:
            if inventory_object.name.lower() == object_name.lower():
                return inventory_object
        return None

    def add_object(self, object):
        self.objects.append(object)

    def remove_object(self, object):
        self.objects.remove(object)

    def get_inventory_string(self, longest_obj_name):
        '''
        Get a comma-delineated list of the objects in the inventory
        :return:
        '''

        if self.objects:
            inventory_size = len(self.objects)
            count = 0
            inventory_string = ""
            for object in self.objects:
                obj_name_len = len(object.get_name())
                padding = longest_obj_name - obj_name_len
                count += 1
                inventory_string += "[" + object.get_name() + ']...' + ("." * padding) + object.get_short_description()
                if count is not inventory_size:
                    inventory_string += "\n"
            return inventory_string
        return INVENTORY_EMPTY
