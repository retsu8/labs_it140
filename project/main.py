import sys
import re
from logic.map import Map
from logic.player import Player
from logic.item import Item
from logic.dialogue import Dialogue


class Game:
    """Main game class for construcing the text based game."""

    maps = Map()
    player = Player()
    dialogue = Dialogue()
    items = Item()

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
        else:
            return False
        re.sub("[^A-Za-z0-9 ]+", "", selection)
        selection = selection.lower().replace(" ", "_")
        return selection

    def check_locked_room(self, room):
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

    def handle_item_pickup(self, locaiton):
        """Handle room item pickup"""
        room_item = self.items.get_item(self.player.get_location())
        print(self.player.get_inventory())
        print(room_item)
        if room_item["name"] not in self.player.get_inventory():
            pickup = input(self.dialogue.pickup_item(room_item["name"]))
            pickup = pickup.split(" ", maxsplit=1)
            if "get" in pickup:
                pickup.remove("get")
                pickup = pickup[0].lower()
                if room_item["name"].lower() in pickup:
                    self.player.pickup_item(room_item)
                    print(self.dialogue.pickedup_item(room_item["name"]))
                    print(self.dialogue.get_item_description(room_item["description"]))
            else:
                print(self.dialogue.leave_item())

    def main(self):
        """Main player handling function"""
        print(self.dialogue.get_introduciton())
        print(self.dialogue.get_player_help())
        print(self.dialogue.get_additional_input())
        villian = self.maps.get_villian_location()
        description = self.maps.get_description(self.player.get_location())
        print(self.dialogue.get_room_description(description))
        while not self.player.dead:
            print(self.dialogue.get_player_inventory(self.player.get_inventory()))
            player_input = self.player_input_selection()
            connected_rooms = self.maps.get_connected_rooms(self.player.get_location())
            if player_input == "0":
                print(self.dialogue.get_player_died())
                sys.exit()
            elif player_input == "help":
                print(self.dialogue.get_additional_input())
            elif player_input in connected_rooms.keys():
                if player_input in villian:
                    if self.player.get_inventory_count() == self.items.get_count():
                        print("You Win")
                    else:
                        print(self.dialogue.get_player_meets_villan_unarmed())
                        self.handle_player_died()
                else:
                    key_location = connected_rooms[player_input]
                    key_item = self.check_locked_room(self.maps.location[key_location])
                    if key_item in self.player.get_inventory() or not key_item:
                        self.player.update_location(key_location)
                        description = self.maps.get_description(self.player.get_location())
                        print(self.dialogue.room_into(key_location))
                        print(self.dialogue.get_room_description(description))
                        self.handle_item_pickup(self.player.get_location())
                    elif key_item:
                        print(self.dialogue.get_room_locked(key_location))
            else:
                print(self.dialogue.get_invalid_input())
                print(self.dialogue.get_rooms_promt(self.player.get_location()))


if __name__ == "__main__":
    game = Game()
    game.main()
