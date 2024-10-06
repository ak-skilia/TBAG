class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        return f"{self.name} is here!\n{self.description}"
        
    def set_conversation(self, conversation):
        self.conversation = conversation


    def talk(self):
        if self.conversation is not None:
            return f"[{self.name}] says: {self.conversation}"
        else:
            return f"{self.name} doesn't want to talk to you"
        
    def feed(self):
        return f"You feed {self.name} with the food."

class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.status = "healthy"
    
    def set_weakness(self, item_weakness):
        self.weakness = item_weakness
    
    def get_weakness(self):
        return self.weakness
    
    def fight(self, weapon):
        if weapon == "jade":
            self.status = "defeated"
            return True  # Enemy is defeated
        elif weapon == "knife":
            self.status = "injured"
            print("The enemy is injured but still alive.")
            return False  # Enemy is injured but not defeated
        elif weapon == "bare hands":
            self.status = "healthy"
            return False  # Player is defeated
        else:
            return False
        
    def fight_sequence(self, player_inventory, current_room, hallway2):
        from colorama import Fore, Style
        if not any(item.get_name() == "jade" for item in player_inventory):
            print(Fore.RED + "You don't have the ultimate weapon to fight the enemy. Do you want to run away, try to injure the enemy, or keep fighting?")
            sub_command = input(Fore.YELLOW + "Type 'run' to run away, 'injure' to injure with the knife, or 'fight' to keep fighting: ").lower()
            if sub_command == "run":
                print(Fore.GREEN + "You run away safely.")
                return hallway2
            elif sub_command == "injure" and any(item.get_name() == "knife" for item in player_inventory):
                print(Fore.GREEN + "You injure the enemy with the knife and run away.")
                self.fight("knife")
                return hallway2
            elif sub_command == "fight":
                print(Fore.RED + "You decide to keep fighting without any weapons.")
                if self.fight("bare hands"):
                    print(Fore.GREEN + "You have defeated the enemy!")
                    current_room.set_character(None)
                else:
                    print(Fore.RED + "You have been defeated!")
                    return None
            else:
                print(Fore.RED + "You don't have the knife to injure the enemy. You run away safely.")
                return hallway2
        else:
            print(Fore.RED + "What will you fight with?")
            fight_with = input(Fore.YELLOW + "Type 'jade' to use the jade, 'knife' to use the knife, or 'bare hands' to fight without weapons: ").lower()
            if fight_with == "jade":
                if self.fight("jade"):
                    print(Fore.GREEN + "You have defeated the enemy with the jade!")
                    current_room.set_character(None)
                else:
                    print(Fore.RED + "You have been defeated!")
                    return None
            elif fight_with == "knife":
                print(Fore.RED + "You injure the enemy with the knife, but they remain.")
                self.fight("knife")
            elif fight_with == "bare hands":
                if self.fight("bare hands"):
                    print(Fore.GREEN + "You have defeated the enemy!")
                    current_room.set_character(None)
                else:
                    print(Fore.RED + "You have been defeated!")
                    return None
            else:
                print(Fore.RED + "Invalid choice. You run away safely.")
                return hallway2
        return current_room

    def describe(self):
        description = f"{self.name} is here. {self.description}"
        if self.status == "injured":
            description += " The enemy looks injured."
        elif self.status == "defeated":
            description += " The enemy has been defeated."
        return description
    


class Friend(Character):
    def hug(self):
        return f"{self.name} gives you a warm hug!"
        
    def dance(self):
        return f"You dance with {self.name} using the music player."