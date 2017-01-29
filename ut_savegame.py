# Unit test to test out the save_game class

from gameclient.game_client import *
from fileio.save_game import *
import pprint

# For debugging
from debug.debug import *


logger = logging.getLogger(__name__)


def main():
    GC = GameClient()
    GC.gamestate.rooms = GC.gamestate.rb.load_room_data_from_file()
    GC.gamestate.initialize_new_game()


    sg = SaveGame(GC.gamestate)
    pp = pprint.PrettyPrinter()
    print("Current Room:")
    pp.pprint(sg.get_current_room())
    print("Objects in Rooms:")
    pp.pprint(sg.get_objects_in_rooms())
    print("Player inventory:")
    pp.pprint(sg.get_player_inventory())
    print("List of visited rooms:")
    pp.pprint(sg.get_visited_rooms_list())

main()