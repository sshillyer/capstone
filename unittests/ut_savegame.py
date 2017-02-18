# Unit test to test out the save_game class

from gameclient.game_client import *
from fileio.save_game import *
import pprint

# For debugging
from debug.debug import *

logger = logging.getLogger(__name__)


def ut_savegame():
    GC = GameClient()
    GC.gamestate.rooms = GC.gamestate.rb.load_room_data_from_file()
    GC.gamestate.initialize_gamestate()

    sg = SaveGame(GC.gamestate)
    pp = pprint.PrettyPrinter()
    print("Current Room:")
    pp.pprint(sg.get_current_room())
    print("Objects in Rooms:")
    pp.pprint(sg.get_objects_room_mapping())
    print("Player inventory:")
    pp.pprint(sg.get_player_inventory())
    print("List of visited rooms:")
    pp.pprint(sg.get_visited_rooms_list())


ut_savegame()