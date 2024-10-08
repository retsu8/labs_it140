import sys
import re
import logging
from unittest import mock
from unittest import TestCase
import argparse
from logic.map import Map
from logic.player import Player
from logic.item import Item
from logic.dialogue import Dialogue


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
                print(key_item)
                print(self.player.get_inventory_slug())
                if key_item in self.player.get_inventory_slug() or not key_item:
                    self.player.update_location(key_location)
                    description = self.maps.get_description(self.player.get_location())
                    print(self.dialogue.room_intro(key_location))
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
