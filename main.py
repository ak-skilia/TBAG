from room import Room
from character import Character
from character import Enemy
from item import Item
from character import Friend
from colorama import init, Fore, Back, Style

kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")
foyer = Room("Foyer")
bedroom = Room("Bedroom")
garage = Room("Garage")
locked_room = Room("Locked Room")
hallway1 = Room("Hallway 1")
hallway2 = Room("Hallway 2")
hallway3 = Room("Hallway 3")

mordred = Enemy("Mordred", "a zombie knight on zoomies")
mordred.set_conversation("Brrlgrh... rgrhl... brains...")
mordred.set_weakness("jade")
dining_hall.set_character(mordred)

gaius = Character("Gaius","a friendly goblin")
gaius.set_conversation("Hello there! I'm Gaius, the mischevious goblin.")
kitchen.set_character(gaius)

elena = Friend("Elena", "a kind-hearted fairy")
elena.set_conversation("Hi! I'm Elena. I hope you're to keep my company")
ballroom.set_character(elena)

key = Item()
key.set_name("key")
key.set_description("a small rusty thing")
bedroom.set_item(key)

food = Item()
food.set_name("food")
food.set_description("A plate of delicious food.")
kitchen.set_item(food)

music_player = Item()
music_player.set_name("music player")
music_player.set_description("A portable music player.")
ballroom.set_item(music_player)

knife = Item()
knife.set_name("knife")
knife.set_description("A sharp kitchen knife.")
dining_hall.set_item(knife)

map = Item()
map.set_name("map")
map.set_description("A map of the place.")
foyer.set_item(map)

jade = Item()
jade.set_name("jade")
jade.set_description("A glowing rock.")
garage.set_item(jade)

player_inventory = []

kitchen.set_description("A dank and dirty room buzzing with flies")
ballroom.set_description("A vast room with a shiny wooden floor")
dining_hall.set_description("A large room with ornate decorations")
foyer.set_description("A small entryway with a coat rack and a dusty mirror.")
bedroom.set_description("A cozy bedroom with a large bed and a wardrobe.")
garage.set_description("A cluttered garage with tools scattered everywhere.")
locked_room.set_description("A mysterious locked room. You need a key to enter.")
hallway1.set_description("A narrow hallway with creaky floorboards.")
hallway2.set_description("A dimly lit hallway with old paintings on the walls.")
hallway3.set_description("A long hallway with several doors leading to other rooms.")

foyer.link_room(hallway1, "north")
hallway1.link_room(foyer, "south")
hallway1.link_room(garage, "west")
garage.link_room(hallway1, "east")
hallway1.link_room(kitchen, "east")
kitchen.link_room(hallway1, "west")
hallway1.link_room(hallway2, "north")
hallway2.link_room(hallway1, "south")
hallway2.link_room(dining_hall, "east")
dining_hall.link_room(hallway2, "west")
hallway2.link_room(ballroom, "west")
ballroom.link_room(hallway2, "east")
hallway2.link_room(hallway3, "north")
hallway3.link_room(hallway2, "south")
hallway3.link_room(bedroom, "north")
bedroom.link_room(hallway3, "south")
hallway3.link_room(locked_room, "east")
locked_room.link_room(hallway3, "west")

current_room = foyer
previous_room = None
locked_room_unlocked = False

print(Style.BRIGHT + Fore.GREEN + "You find yourself in the foyer of a grand, mysterious mansion.\nThe air is musty, and the sound of distant footsteps echoes through the halls.\nWith no memory of how you arrived, you feel an urge to explore and uncover the secrets hidden within these walls.\n\nYour objective is to navigate the house, interact with its inhabitants, and collect items to aid your journey.\nStay alert, as things may not be what they seem.\n\nUse commands like north, south, east, and west to navigate through the rooms\nInteract with characters using commands like " + Style.RESET_ALL)

init(autoreset=True)

while True:
    print("\n")
    print(Fore.WHITE + f"{current_room.get_details()}")
    
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        print(Fore.MAGENTA + f"{inhabitant.describe()}")
        print(Fore.YELLOW + "Your inventory:", ', '.join(item.get_name() for item in player_inventory))

    available_commands = ["north", "south", "east", "west", "inventory"]
    if inhabitant is not None:
        available_commands.append("talk")
        if isinstance(inhabitant, Enemy):
            available_commands.append("fight")
        if isinstance(inhabitant, Friend):
            available_commands.append("hug")
        if any(item.get_name() == "music player" for item in player_inventory):
            available_commands.append("dance")
        if any(item.get_name() == "food" for item in player_inventory):
            available_commands.append("feed")
    if current_room.get_item() is not None:
        available_commands.append(f"take {current_room.get_item().get_name()}")
    if current_room == hallway3 and any(item.get_name() == "key" for item in player_inventory):
        available_commands.append("use key")
    if current_room == bedroom:
        available_commands.append("nap")
    if any(item.get_name() == "map" for item in player_inventory):
        available_commands.append("use map")
    command = input(Fore.BLUE + Style.BRIGHT + f"What do you want to do? ({', '.join(available_commands)}) \n>>> ").lower()
    
    if command == "use map":
        Item.print_map()
    elif command in ["north", "south", "east", "west"]:
        if command == "east" and current_room == hallway3 and not locked_room_unlocked:
            print(Fore.RED + "The door to the east is locked. You need a key to enter.")
        else:
            previous_room = current_room 
            current_room = current_room.move(command)
            if previous_room == kitchen and food_taken:
                kitchen.set_item(food)
                food_taken = False
            if current_room == locked_room:
                print(Fore.RED + "\nYou are now in the Locked Room")
                print(current_room.get_description())
                print(Fore.RED + "------------------------------------------------------------------------")
                print(Fore.RED + "Ancient artifacts being the trapped and vengeful High Priestesses")
                print(Fore.RED + "---\nThey strike you down with a bolt of lightning\n---\nYou have sadly perished..\n---")
                print(Fore.RED + "Oh well! \n---\nTry not to be so gullible next time. \n---\nThanks for breaking their curse on our behalf!")
                break
    elif command == "talk" and inhabitant is not None:
        print(Fore.GREEN + f"{inhabitant.talk()}")
    elif command == "fight" and inhabitant is not None:
        new_room = inhabitant.fight_sequence(player_inventory, current_room, hallway2)
        if new_room is None:
            break
        else:
            current_room = new_room
    elif command.startswith("take ") and current_room.get_item() is not None:
        item_name = command.split("take ")[1]
        if current_room.get_item().get_name() == item_name:
            print(Fore.GREEN + f"You have taken the {item_name}.")
            player_inventory.append(current_room.get_item())
            if item_name == "food":
                food_taken = True
            current_room.set_item(None)
    elif command == "use key" and current_room == hallway3 and any(item.get_name() == "key" for item in player_inventory):
        if not locked_room_unlocked:
            print(Fore.GREEN + "You use the key to unlock the locked room.")
            locked_room_unlocked = True
            locked_room.set_description(Fore.RED +"A mysterious room that has now been unlocked. It contains various ancient artifacts.")
            print(Fore.GREEN + "The locked room is now accessible.")
        else:
            print(Fore.RED + "The locked room is already unlocked.")
    elif command == "inventory":
        print(Fore.GREEN + "Your inventory:", ', '.join(item.get_name() for item in player_inventory))       
    elif command == "hug" and isinstance(inhabitant, Friend):
        print(Fore.MAGENTA + f"{inhabitant.hug()}")
    elif command == "dance" and any(item.get_name() == "music player" for item in player_inventory):
        if isinstance(inhabitant, Friend):
            print(Fore.MAGENTA + f"{inhabitant.dance()}")
    elif command == "feed" and any(item.get_name() == "food" for item in player_inventory):
        if isinstance(inhabitant, Character):
            print(Fore.MAGENTA + f"{inhabitant.feed()}")
            player_inventory = [item for item in player_inventory if item.get_name() != "food"]
        else:
            print(Fore.RED + "There's no food to feed with")
        player_inventory = [item for item in player_inventory if item.get_name() != "food"]
    elif command == "nap" and current_room == bedroom:
        print(Fore.YELLOW + "You take a nap \nzzzzzzzzzzzzzzzzzzzzzzzzzz")
        print(Fore.YELLOW + "\nwakey wakey \nyou now feel refreshed")
    else:
        print(Fore.RED + f"Invalid command. Try one of the following: {', '.join(available_commands)}.")
