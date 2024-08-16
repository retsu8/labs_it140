import sys
import re
import logging
from unittest import mock
from unittest import TestCase
import argparse


class Map:
    """Mapping class for building the player map"""

    def __init__(self):
        self.location = {
            "start_room": {
                "name": "Start Room",
                "description": "Summoning room for Cthulahu",
                "item": "",
                "room_image": "",
                "connected_rooms": {"west": "lab"},
            },
            "lab": {
                "name": "Lab",
                "description": "Room for resaearch",
                "item": "green_slime",
                "room_image": "",
                "connected_rooms": {
                    "west": "meeting_room",
                    "east": "start_room",
                    "south": "kitchen",
                },
            },
            "meeting_room": {
                "name": "Meeting Room",
                "description": "Room with lots of couches and a few armchairs.",
                "item": "research_notes",
                "room_image": "",
                "connected_rooms": {
                    "east": "lab",
                    "north": "kiras_room",
                    "west": "bruces_room",
                    "south": "koals_room",
                },
            },
            "kiras_room": {
                "name": "Kira's Room",
                "description": "Kira's the lab assistants room. Nice and neat jsut like she was.",
                "item": "secret_notes",
                "room_image": "",
                "connected_rooms": {"south": "meeting_room"},
            },
            "bruces_room": {
                "name": "Bruce's Room",
                "description": "Bruce the lab technician. A very empty room, with almost nothing in it.",
                "item": "lab_id",
                "room_image": "",
                "connected_rooms": {"east": "meeting_room"},
            },
            "koals_room": {
                "name": "Koal's Room",
                "description": "Koal's the lab lead.  Always piled with clutter.",
                "item": "acid",
                "room_image": "",
                "connected_rooms": {"north": "meeting_room"},
            },
            "staff_quarters": {
                "name": "Staff Quarters",
                "description": "Hy! Its the old staff quarters, always feels like home",
                "item": "sandwich",
                "room_image": "",
                "connected_rooms": {
                    "north": "kitchen",
                    "west": "armory",
                    "east": "garage",
                },
            },
            "lounge": {
                "name": "Lounge",
                "description": "I am the being Cthulahu; summoned to this realm.",
                "villian": True,
            },
            "armory": {
                "name": "Armory",
                "description": "Lots of old crates and boxes in here, laboled with everything the research team needed.",
                "item": "handgun",
                "room_image": "",
                "connected_rooms": {"east": "staff_quarters"},
                "locked": "lab_id",
            },
            "kitchen": {
                "name": "Kitchen",
                "description": "Always loved to work in the kitchen, its the closest to the food.",
                "item": "vehicle_keys",
                "room_image": "",
                "connected_rooms": {
                    "north": "lab",
                    "east": "lounge",
                    "south": "staff_quarters",
                },
            },
            "garage": {
                "name": "Garage",
                "description": "There an old jeap in here, wounder if it actually runs.",
                "item": "crystals",
                "room_image": "",
                "connected_rooms": {"east": "staff_quarters"},
                "locked": "acid",
            },
        }

    def get_connected_rooms(self, location):
        """Get the connected rooms for this locaiton"""
        return self.location[location]["connected_rooms"]

    def get_description(self, location):
        """Get the room discription"""
        return self.location[location]["description"]

    def get_name(self, location):
        """Get the pretty room name"""
        return self.location[location]["name"]

    def get_villian_location(self):
        """Get the villans room"""
        for room in self.location:
            if "villian" in self.location[room]:
                return room


class Dialogue:
    def __init__(self):
        """Dialogue functionaity of rooms game; this class makes the dialoge for the game,
        Allowing each function to take care of the specifics for the dialoge assoication.
        Thus only dialoge modiciation should be done here. Incoming var manipulation
        should kept to a minimum."""
        self.vowels = ("a", "e", "i", "o", "u")
        self.help = """To interact with the maps, put go 'direction'.\nTo pickup items, use the command, get item/ or leave item\nTo see this menu again, type in help."""
        self.path = "Choose one of the following paths here {}"
        self.introduction = """Wellcome to Greyhalk, and the tomb of horrors, you're responsible for making it out of this tomb before running into the horrors of Cthulhu. Deep in the crypt, there lies the ancient sigils of summoning.  Having tested these sigals and succeeded; you're now the sole survivor left, after the rest were killed. You need to now collect the various items from the rooms in order to make a new banishing sigal and hopefully it will work.\n"""

    def get_introduciton(self):
        return self.introduction

    def get_player_help(self):
        return self.help

    def get_winning_person(self):
        return "You have managed to collect all the items and banish Cthulhu back to the netherrealm!"

    def get_room_promt(self, location):
        return "Looks like theres only one direction to go here."

    def get_invalid_input(self):
        return "That input is invalid, try again."

    def get_rooms_promt(self, location):
        return """Looks like theres multiple ways to go, where to next?\n_______________________________________________________"""

    def get_additional_input(self):
        return "You can also use 0 to quite the game\n--------------------------------------\n"

    def get_player_died(self):
        return "The game has now ended, you have died."

    def get_item_description(self, item):
        return f"Item Description: {item}"

    def pickup_item(self, item):
        if item[0] in self.vowels:
            return f"You've found an {item}; would you like to pick it up?\n"
        elif item[-1].lower() == "s":
            return f"Youve found the {item}; would you like to pick them up?\n"
        return f"Youve found a {item}; would you like to pick it up?\n"

    def get_room_locked(self, location):
        if "garage" in location:
            return "The room is chained shut, theres no way in."
        elif "armory" in location:
            return "The is locked with a keycard? Maybe there is one around?"

    def leave_item(self):
        return "You decided to leave the item here, this choice may not be wise."

    def pickedup_item(self, item):
        if item[0] in self.vowels:
            return f"You picked up an {item}"
        else:
            return f"You picked up the {item}"

    def get_item_already_found(self, location):
        if location == "garage":
            return "Looks like the truck is empty."
        return "Looks like the room is empty."

    def get_item_pickup(self, item):
        return f"You picked up the item {item}"

    def get_player_inventory(self, inventory_list):
        return f"Inventory: {'; '.join(inventory_list)}"

    def get_room_description(self, description):
        return f"""Description: {description}"""

    def get_player_meets_villan_unarmed(self):
        return "Your not prepared yet, still cant banish back Cthulhu!!!"

    def room_intro(self, location):
        return f"""Location: {location}"""


class Player:
    """Class building the basic player setup"""

    def __init__(self):
        """__init__ function of player class to build player"""
        self.inventory = []
        self.location = "start_room"
        self.visited = []
        self.dead = False

    def update_location(self, location):
        """set the location of the player in the map"""
        self.location = location
        self.visited += [location]

    def get_visited_map(self):
        """Print everwhere the player went"""
        return self.visited

    def update_items(self, item):
        """Add items to inventory"""
        self.items += [item]

    def get_location(self):
        """Get the players location"""
        return self.location

    def pickup_item(self, item):
        """Get item add to inventory items"""
        self.inventory += [item]
        return self.inventory

    def get_inventory(self):
        """Get the pretty inventory names"""
        inventory = set()
        for item in self.inventory:
            inventory.update([item["name"]])
        return sorted(list(inventory))

    def get_inventory_slug(self):
        """Get the slugs for the inventory"""
        inventory = set()
        for item in self.inventory:
            inventory.update([item["slug"]])
        return sorted(list(inventory))

    def get_inventory_count(self):
        """Count the inventory size"""
        return len(self.inventory)

    def reset(self):
        """Reset the player top defaults to start new game"""
        self.inventory = []
        self.location = "start_room"
        self.visited = []
        self.dead = False


class Item:
    def __init__(self):
        self.items = {
            "research_notes": {
                "name": "Research Notes",
                "description": "Notes of the summon from the lab, all neat and documented.",
                "location": "meeting_room",
                "slug": "research_notes",
            },
            "green_slime": {
                "name": "Green Slime",
                "description": "A strang glowing green slime that was used in the summon circle?",
                "location": "lab",
                "slug": "green_slime",
            },
            "secret_notes": {
                "name": "Secret Notes",
                "description": "Notes of the issues with the signal that looks like something went wrong.",
                "location": "kiras_room",
                "slug": "secret_notes",
            },
            "lab_id": {
                "name": "Lab ID",
                "description": "The lab id badge for the lab and grounds",
                "location": "bruces_room",
                "slug": "lab_id",
            },
            "acid": {
                "name": "Acid Vail",
                "description": "Vail of acid placed haphazurdusly on the desk",
                "location": "koals_room",
                "slug": "acid",
            },
            "sandwich": {
                "name": "Rye with Tuna",
                "description": "A great lunch to have before setting up the sigals to banish the final boss.",
                "location": "staff_quarters",
                "slug": "sandwich",
            },
            "handgun": {
                "name": "Handgun",
                "description": "Possibly rather useless here but it still helps personal moral.",
                "location": "armory",
                "slug": "handgun",
            },
            "keys": {
                "name": "Vehicle Keys",
                "description": "Keys for the jeep in the garage.",
                "location": "kitchen",
                "slug": "keys",
            },
            "crystals": {
                "name": "Purple Pulsating Crystal",
                "description": "This crystal is very agitating to be near, best to put it away.",
                "location": "garage",
                "slug": "crystals",
            },
        }

    def get_item(self, location):
        """Get the item from the room location"""
        for key, item in self.items.items():
            if location in item["location"]:
                return self.items[key]
        return ""

    def get_count(self):
        """Get the count of items possible"""
        return len(self.items.keys())

    def get_description(self, item):
        """Get the items discription"""
        return self.items[item]["description"]


class Game:
    """Main game class for construcing the text based game."""

    def __init__(self):
        self.maps = Map()
        self.player = Player()
        self.dialogue = Dialogue()
        self.items = Item()
        self.villian = self.maps.get_villian_location()

    def player_input_selection(self):
        """Handle Player input for room navigation"""
        if len(self.maps.get_connected_rooms(self.player.get_location())) > 1:
            print(self.dialogue.get_rooms_promt(self.player.get_location()))
        else:
            print(self.dialogue.get_room_promt(self.player.get_location()))
        for key, room in self.maps.get_connected_rooms(
            self.player.get_location()
        ).items():
            room = self.maps.get_name(room)
            print(f"{key}: {room}")
        selection = input().split(" ", maxsplit=1)
        if "go" in selection:
            selection = selection[1]
        elif "0" in selection or "help" in selection:
            return selection[0]
        else:
            return False
        re.sub("[^A-Za-z0-9 ]+", "", selection)
        selection = selection.lower().replace(" ", "_")
        return selection

    def check_locked_room(self, room):
        """Check if the room is locked"""
        if "locked" in room.keys():
            return room["locked"]
        else:
            return False

    def handle_play_again(self):
        """Handle player interaction with play again"""
        print("Fun map of where you wondered.")
        print(self.player.get_visited_map())
        while True:
            ans = input("Play again? Y/N")
            if "y" == ans.lower():
                self.player.reset()
                return
            elif "n" == ans.lower():
                print("Goodbye")
                return
            else:
                print("Invalid response")

    def handle_player_died(self):
        """Handles player that died"""
        self.player.dead = True
        print(self.dialogue.get_player_died())
        return self.handle_play_again()

    def handle_item_pickup(self, room_item):
        """Player item pickup"""
        pickup = input(self.dialogue.pickup_item(room_item["name"]))
        pickup = pickup.split(" ", maxsplit=1)
        if self.handle_player_defaults(pickup):
            return
        elif "get" in pickup:
            pickup.remove("get")
            pickup = pickup[0].lower()
            if room_item["name"].lower() in pickup:
                self.player.pickup_item(room_item)
                print(self.dialogue.pickedup_item(room_item["name"]))
                print(self.dialogue.get_item_description(room_item["description"]))
                return True
            else:
                print(self.dialogue.get_invalid_input())
        elif "leave" in pickup:
            pickup.remove("leave")
            print(self.dialogue.leave_item())
            return True
        else:
            print(self.dialogue.get_invalid_input())
        return False

    def handle_player_defaults(self, player_input):
        if player_input == "0":
            self.handle_player_died()
            return True
        elif player_input == "help":
            print(self.dialogue.get_player_help())
            return True
        return False
    
    def play_introduction(self):
        """Introduce the story and help menu"""
        print(self.dialogue.get_introduciton())
        print(self.dialogue.get_player_help())
        print(self.dialogue.get_additional_input())

    def get_room_description(self, location):
        """Return the room description"""
        description = self.maps.get_description(location)
        print(self.dialogue.get_room_description(description))

    def handle_player_walk(self):
        """Main player walk functionality."""
        player_input = self.player_input_selection()
        connected_rooms = self.maps.get_connected_rooms(self.player.get_location())
        if self.handle_player_defaults(player_input):
            return
        elif player_input in connected_rooms.keys():
            # HOW TO: handle player fights villain
            if player_input in self.villian:
                if self.player.get_inventory_count() == self.items.get_count():
                    print(self.dialogue.get_winning_person())
                else:
                    print(self.dialogue.get_player_meets_villan_unarmed())
                    self.handle_player_died()
            else:
                key_location = connected_rooms[player_input]
                key_item = self.check_locked_room(self.maps.location[key_location])
                if key_item in self.player.get_inventory_slug() or not key_item:
                    self.player.update_location(key_location)
                    description = self.maps.get_description(self.player.get_location())
                    key_room_name = self.maps.get_name(key_location)
                    print(self.dialogue.room_intro(key_room_name))
                    print(self.dialogue.get_room_description(description))
                    room_item = self.items.get_item(self.player.get_location())
                    if room_item["slug"] not in self.player.get_inventory_slug():
                        choice = False
                        while not choice:
                            choice = self.handle_item_pickup(room_item)
                elif key_item:
                    print(self.dialogue.get_room_locked(key_location))
        else:
            print(self.dialogue.get_invalid_input())
            print(self.dialogue.get_rooms_promt(self.player.get_location()))

    def main(self):
        """Main player handling function"""
        self.play_introduction()
        self.get_room_description(self.player.get_location())
        while not self.player.dead:
            print(self.dialogue.get_player_inventory(self.player.get_inventory()))
            self.handle_player_walk()


class TestPlayerInputSelection(TestCase):

    @mock.patch("__main__.Game.handle_item_pickup")
    def test_player_input_selection(self, handle_item_pickup_mock):
        """Test the selection input for good responses"""
        handle_item_pickup_mock.return_value=True

        game = Game()
        with mock.patch("builtins.input", return_value="go west"):
            self.assertEqual(game.player_input_selection(), "west")

        with mock.patch("builtins.input", return_value="go right"):
            self.assertEqual(game.player_input_selection(), "right")

        with mock.patch("builtins.input", return_value="goright"):
            self.assertEqual(game.player_input_selection(), False)

        with mock.patch("builtins.input", return_value="try again"):
            self.assertEqual(game.player_input_selection(), False)

    def test_check_locked_room(self):
        game = Game()
        keys = {"locked": "acid"}
        self.assertIs(game.check_locked_room(keys), "acid")

    def test_handle_play_again(self):
        game = Game()
        game.player.update_location("staff_quarters")
        with mock.patch("builtins.input", return_value="y"):
            game.handle_play_again()
            self.assertEqual(game.player.location, "start_room")

    def test_update_inventory(self):
        game = Game()
        item = Item()
        game.player.pickup_item(item.items["green_slime"])
        self.assertEqual(game.player.get_inventory(), ["Green Slime"])
        game.player.pickup_item(item.items["research_notes"])
        self.assertEqual(game.player.get_inventory(), ["Green Slime", "Research Notes"])

    def test_handle_item_pickup(self):
        game = Game()
        game.player.update_location("lab")
        with mock.patch("builtins.input", return_value="get green slime"):
            room_item = game.items.get_item(game.player.get_location())
            game.handle_item_pickup(room_item)
            self.assertEqual(game.player.get_inventory(), ["Green Slime"])

    def not_a_test(self):
        return "test"


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-h":
        """Handle simple testing for a few needed resources"""
        print("Printing out tests")
        test = TestPlayerInputSelection()
        test.test_player_input_selection()
        test.test_check_locked_room()
        test.test_handle_play_again()
        test.test_update_inventory()
        test.test_handle_item_pickup()
    else:
        """Start the game"""
        game = Game()
        game.main()