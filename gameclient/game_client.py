class GameClient:
    '''
    Main controller for the game's flow and logic
    '''
    def __init__(self):
        self.gamestate = GameState()
        self.gamestate.load_rooms_from_files()
        self.ui = UserInterface()

        # Initiate game loop
        self.main_loop()

    def main_loop(self):
        user_input = ""
        while user_input != 'quit':
            print(self.ui.print_main_menu())
            user_input = self.ui.user_prompt()






class GameState:
    '''
    Holds all of the variables that maintain the game's state
    '''
    def __init__(self):
        self.rooms = []
        self.player = Player()

    def load_rooms_from_files(self):
        print("Loading rooms from files (This is a stub)")





class UserInterface:
    '''
    Primarily used to print information to the user's screen
    '''
    def __init__(self):
        self.prompt_text = ">> "


    def print_main_menu(self):
        print("Welcome to Hacker: The Movie: The Adventure Game: The Sequel")
        print("This game is awesome! If you wanna start h4ck1nG the n3t, say 'begin hack'! Or be a sissy and 'quit'!" )

    def user_prompt(self):
        return input(self.prompt_text)



class Player:
    '''
    Player stats and methods
    '''
    def __init__(self):
        self.cash = 0
        self.coolness = 0
        self.speed = 0
        self.inventory = Inventory()

class Inventory:
    '''
    Objects and methods related to adding and removing them from inventory
    '''
    def __init__(self):
        self.objects = []



class Object:

    def __init__(self, name, description):
        self.name = name
        self.description = description
