# Unit tests for language parser
# Created by Shawn

import unittest
from constants.verbs import *
from languageparser.language_parser import *
from fileio.room import *
from fileio.object import *
from debug.debug import *

logger = logging.getLogger(__name__)


class TestLanguageParser(unittest.TestCase):
    def setUp(self):
        self.LP = LanguageParser()
        # So we can access all of the actual rooms, features, objects in the game files...
        self.ObjectBuilder = ObjectBuilder()
        self.objects = self.ObjectBuilder.load_object_data_from_file("../gamedata/objects/*.json")

        # Get all of the object names in game
        self.object_names = []
        for obj in self.objects:
            self.object_names.append(obj.get_name())

        self.RoomBuilder = RoomBuilder()
        self.rooms = self.RoomBuilder.load_room_data_from_file("../gamedata/rooms/*.json")

        # Get all of the features by name and rooms by name
        self.room_names = []
        self.room_feature_names = []
        for room in self.rooms:
            self.room_names.append(room.get_name())
            for feature in room.room_features:
                self.room_feature_names.append(feature.get_name())

        self.cardinal_directions = ['north', 'south', 'east', 'west']

    def test_lp_newgame_valid_strings(self):
        for test_string in NEW_GAME_ALIASES:
            result = self.LP.parse_command(test_string)
            expected_noun = {'name': None, 'type': None}

            self.assertEquals(NEW_GAME, result.get_verb(), NEW_GAME + " does not match " + str(result.get_verb()))
            self.assertEquals(expected_noun, result.get_noun())
            self.assertIsNone(result.get_extras())
            self.assertIsNone(result.get_preposition())
            self.assertIsNone(result.get_error_message())

            logger.debug("Checking if string returns verb NEW_GAME: '" + test_string + "'")
            logger.debug("Passed.")

    def test_lp_loadgame_valid_strings(self):
        for test_string in LOAD_GAME_ALIASES:
            result = self.LP.parse_command(test_string)
            expected_noun = {'name': None, 'type': None}

            self.assertEquals(LOAD_GAME, result.get_verb(), LOAD_GAME + " does not match " + str(result.get_verb()))
            self.assertEquals(expected_noun, result.get_noun())
            self.assertIsNone(result.get_extras())
            self.assertIsNone(result.get_preposition())
            self.assertIsNone(result.get_error_message())

            logger.debug("Checking if string returns verb LOAD_GAME: '" + test_string + "'")
            logger.debug("Passed.")

    def test_lp_help_valid_strings(self):
        for test_string in HELP_ALIASES:
            result = self.LP.parse_command(test_string)
            expected_noun = {'name': None, 'type': None}

            self.assertEquals(HELP, result.get_verb(), HELP + " does not match " + str(result.get_verb()))
            self.assertEquals(expected_noun, result.get_noun())
            self.assertIsNone(result.get_extras())
            self.assertIsNone(result.get_preposition())
            self.assertIsNone(result.get_error_message())

            logger.debug("Checking if string returns verb HELP: '" + test_string + "'")
            logger.debug("Passed.")

    def test_lp_quit_valid_strings(self):
        for test_string in QUIT_ALIASES:
            result = self.LP.parse_command(test_string)
            expected_noun = {'name': None, 'type': None}

            self.assertEquals(QUIT, result.get_verb(), QUIT + " does not match " + str(result.get_verb()))
            self.assertEquals(expected_noun, result.get_noun())
            self.assertIsNone(result.get_extras())
            self.assertIsNone(result.get_preposition())
            self.assertIsNone(result.get_error_message())

            logger.debug("Checking if string returns verb QUIT: '" + test_string + "'")
            logger.debug("Passed.")

    def test_lp_buy_valid_object_names(self):
        for obj_name in self.object_names:
            for buy_word in BUY_ALIASES:
                test_string = buy_word + " " + str(obj_name)
                obj_name = obj_name.lower()
                expected_noun = {'name': obj_name, 'type': "object"}
                result = self.LP.parse_command(test_string)

                self.assertEquals(BUY, result.get_verb(), "Command '" + test_string + "' incorrectly returns verb: " + str(result.get_verb()))
                self.assertEquals(expected_noun, result.get_noun())
                self.assertIsNone(result.get_extras())
                self.assertIsNone(result.get_preposition())
                self.assertIsNone(result.get_error_message())

                logger.debug("Checking if string returns verb BUY: '" + test_string + "' and NOUN: '" + obj_name + "'")
                logger.debug("Passed.")

    def test_lp_buy_invalid_object_names(self):
        invalid_object_names = [
            '', ' ', '\n', '\t', 'hi', '  hi', 'flippers', 'two words'
        ]

        for obj_name in invalid_object_names:
            for buy_word in BUY_ALIASES:
                test_string = buy_word + " " + str(obj_name)
                obj_name = obj_name.lower()
                # TODO: Revise this unit test with revised language parser logic
                # I think the language parser actually sets expected_noun to None instead of dictionary of None values?
                expected_noun = {'name': '', 'type': None}
                result = self.LP.parse_command(test_string)

                self.assertEquals(BUY, result.get_verb(), "Command '" + test_string + "' incorrectly returns verb: " + str(result.get_verb()))
                self.assertEquals(expected_noun, result.get_noun())
                self.assertEquals(None, result.get_extras())
                self.assertEquals(None, result.get_preposition())
                self.assertIsNone(result.get_extras())

                logger.debug("Checking if string returns verb BUY: '" + test_string + "' and NOUN: '" + obj_name + "'")
                logger.debug("Passed.")

    def test_lp_look(self):
        for look_word in LOOK_ALIASES:
            look_word = look_word.lower()
            expected_noun = {'name': None, 'type': None}
            result = self.LP.parse_command(look_word)
            self.assertEquals(LOOK, result.get_verb())
            self.assertEquals(expected_noun, result.get_noun())
            self.assertIsNone(result.get_extras())
            self.assertIsNone(result.get_preposition())
            self.assertIsNone(result.get_extras())

            logger.debug("Checking if string returns verb LOOK: '" + look_word + "'")
            logger.debug("Passed.")

    def test_lp_inventory(self):
        for inventory_word in INVENTORY_ALIASES:
            inventory_word = inventory_word.lower()
            expected_noun = {'name': None, 'type': None}
            result = self.LP.parse_command(inventory_word)

            self.assertEquals(INVENTORY, result.get_verb(), "Command '" + inventory_word + "' incorrectly returns verb: " + str(result.get_verb()))
            self.assertEquals(expected_noun, result.get_noun())
            self.assertIsNone(result.get_extras())
            self.assertIsNone(result.get_preposition())
            self.assertIsNone(result.get_extras())

            logger.debug("Checking if string returns verb INVENTORY: '" + inventory_word + "'")
            logger.debug("Passed.")


    def test_lp__take_objects(self):
        for obj_name in self.object_names:
            for take_word in TAKE_ALIASES:
                test_string = take_word + " " + str(obj_name)
                obj_name = obj_name.lower()
                expected_noun = {'name': obj_name, 'type': "object"}
                result = self.LP.parse_command(test_string)

                self.assertEquals(TAKE, result.get_verb(), "Command '" + test_string + "' incorrectly returns verb: " + str(result.get_verb()))
                self.assertEquals(expected_noun, result.get_noun())
                self.assertIsNone(result.get_extras())
                self.assertIsNone(result.get_preposition())
                self.assertIsNone(result.get_error_message())

                logger.debug("Checking if string returns verb TAKE: '" + test_string + "' and NOUN: '" + obj_name + "'")
                logger.debug("Passed.")

    def test_lp__drop_objects(self):
        for obj_name in self.object_names:
            for drop_word in DROP_ALIASES:
                test_string = drop_word + " " + str(obj_name)
                obj_name = obj_name.lower()
                expected_noun = {'name': obj_name, 'type': "object"}
                result = self.LP.parse_command(test_string)

                self.assertEquals(DROP, result.get_verb(), "Command '" + test_string + "' incorrectly returns verb: " + str(result.get_verb()))
                self.assertEquals(expected_noun, result.get_noun())
                self.assertIsNone(result.get_extras())
                self.assertIsNone(result.get_preposition())
                self.assertIsNone(result.get_error_message())

                logger.debug("Checking if string returns verb TAKE: '" + test_string + "' and NOUN: '" + obj_name + "'")
                logger.debug("Passed.")

    def test_lp_go(self):
        destinations = self.cardinal_directions
        for rm in self.room_names:
            destinations.append(rm)

        for go_word in GO_ALIASES:
            for destination in destinations:
                go_word = go_word.lower()
                destination = destination.lower()
                command = go_word + " " + destination
                expected_noun = {'name': destination, 'type': 'destination'}
                result = self.LP.parse_command(command)

                self.assertEquals(GO, result.get_verb(), "Command '" + command + "' incorrectly returns verb: " + str(result.get_verb()))
                self.assertEquals(expected_noun, result.get_noun(), "Command '" + command + "' incorrectly returns noun: " + str(result.get_noun()))
                self.assertIsNone(result.get_extras())
                self.assertIsNone(result.get_preposition())
                self.assertIsNone(result.get_extras())

                logger.debug("Checking if string returns verb INVENTORY: '" + go_word + "'")
                logger.debug("Passed.")


if __name__ == '__main__':
    unittest.main()