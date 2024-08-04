import sys
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
            room = room.replace("_", " ").title()
            print(f"{(room)}")
        return input().lower().replace(" ", "_")

    def check_locked_room(self, room):
        if "lock" in room:
            return room["lock"]
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
                    if key_item in self.player.inventory:
                        self.player.location = player_input
                    else:
                        self.player.location = player_input
                    room_item = self.items.get_item(self.player.location)
                    if room_item not in self.player.inventory:
                        self.player.pickup_item(room_item)
            else:
                print(self.dialogue.get_invalid_input())
                print(self.dialogue.get_rooms_promt(self.player.location))


if __name__ == "__main__":
    game = Game()
    game.main()
