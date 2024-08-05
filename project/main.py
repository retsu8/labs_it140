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
        if len(self.maps.get_connected_rooms(self.player.location)) > 1:
            print(self.dialogue.get_rooms_promt(self.player.location))
        else:
            print(self.dialogue.get_room_promt(self.player.location))
        for room in self.maps.get_connected_rooms(self.player.location):
            room = self.maps.get_name(room)
            print(room)
        selection = input()
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
        room_item = self.items.get_item(self.player.location)
        if room_item not in self.player.inventory:
            pickup = input(self.dialogue.pickup_item(room_item["name"]))
            if "y" == pickup:
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
        while not self.player.dead:
            description = self.maps.get_description(self.player.location)
            print(self.dialogue.get_room_description(description))
            print(self.dialogue.get_player_inventory(self.player.get_inventory()))
            player_input = self.player_input_selection()
            if player_input == "0":
                print(self.dialogue.get_player_died())
                sys.exit()
            elif player_input == "help":
                print(self.dialogue.get_additional_input())
            elif player_input in self.maps.get_connected_rooms(self.player.location):
                if player_input in villian:
                    if self.player.get_inventory_count() == self.items.get_count():
                        print("You Win")
                    else:
                        print(self.dialogue.get_player_meets_villan_unarmed())
                        self.handle_player_died()
                else:
                    key_item = self.check_locked_room(self.maps.location[player_input])
                    if key_item in self.player.inventory or not key_item:
                        self.player.location = player_input
                        self.handle_item_pickup(self.player.location)
                    elif key_item:
                        print(self.dialogue.get_room_locked(player_input))
            else:
                print(self.dialogue.get_invalid_input())
                print(self.dialogue.get_rooms_promt(self.player.location))


if __name__ == "__main__":
    game = Game()
    game.main()
