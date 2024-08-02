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

	def main(self):
		print(self.dialogue.get_introduciton())
		print(self.dialogue.get_player_help())
		while not self.player.dead:
			print(self.maps.get_description(self.player.location))
			if len(self.maps.get_connected_rooms(self.player.location)) > 1:
				print(self.dialogue.get_rooms_promt(self.player.location))
			else:
				print(self.dialogue.get_room_promt(self.player.location))
			for room in self.maps.get_connected_rooms(self.player.location):
				room = room.replace("_", " ").title()
				print(f"{(room)}")
			print(self.dialogue.get_additional_input())
			player_input = input()
			if player_input == "0":
				print(self.dialogue.get_player_died())
				sys.exit()
			else if player_input == "garage":
				if 'acid' in self.player.inventory and 'crystal' in self.inventory:
					self.player.location = self.maps[player_input]
					print(self.dialogue.get_item_already_found(self.player.location))
					print(dialogue.pickup_item(self.player.location))





if __name__ == "__main__":
	game = Game()
	game.main()
