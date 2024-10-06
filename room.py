from colorama import Fore, Style

class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None

    def get_description(self):
        return self.description

    def set_description(self, room_description):
        self.description = room_description

    def describe(self):
        print(self.description)

    def set_name(self, room_name):
        self.name = room_name

    def get_name(self):
        return self.name
    
    def set_character(self, new_character):
        self.character = new_character
    
    def get_character(self):
        return self.character

    def set_item(self, item):
        self.item = item

    def get_item(self):
        return self.item
    
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        details = f"You are in the {self.name} - "
        details += f"{self.description}\n"
        details += "------------------------------------\n"
        
        if self.item is not None:
            details += Fore.GREEN + f"The {self.item.get_name()} is here - {self.item.get_description()}\n------------------------------------\n" + Style.RESET_ALL
        for direction, room in self.linked_rooms.items():
            if room is not None:
                details += Fore.MAGENTA + Style.BRIGHT +"You can move to:" + Style.RESET_ALL
                details += Fore.MAGENTA + Style.BRIGHT + f"The {room.get_name()} is {direction}\n" + Style.RESET_ALL
        return details
    
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self