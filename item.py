from colorama import Fore, Style

class Item():
    def __init__(self):
        self.name = None
        self.description = None
    
    def get_name(self):
        return self.name
    
    def set_name(self, item_name):
        self.name = item_name
    
    def get_description(self):
        return self.description
    
    def set_description(self, item_description):
        self.description = item_description
    
    def print_map():
        map_layout = """
                +-----------------+
                |     Bedroom     |       
                +-----------------+
                        |
                +-----------------+--------------+
                |    Hallway 3    | Locked Room  |
                +-----------------+--------------+
                        |
+--------------+------------------+--------------+
|  Dining Room  |   Hallway 2     |   Ballroom   |
+--------------+------------------+--------------+
                        |
+--------------+------------------+--------------+
|    Kitchen   |    Hallway 1     |    Garage    |
+--------------+------------------+--------------+
                        |
               +------------------+
               |      Foyer       |
               +------------------+
    """
        print(Fore.WHITE + Style.BRIGHT + map_layout + Style.RESET_ALL)
    