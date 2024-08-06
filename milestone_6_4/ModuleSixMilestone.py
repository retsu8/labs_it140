##########################
# William Paddock
# Module 6 Milestone: Moving Between Rooms
#########################

# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.

import sys

class Player:
    """Basic player class to define play actions"""

    def __init__(self):
        """Initialize the player"""
        self.location = "Great Hall"

    def update_location(self, loc):
        """Updat the player location"""
        self.location = loc

    def get_location(self):
        """Return player location"""
        return self.location


class Game:
    """Basic Game class"""
    def __init__(self):
        """Setup gameplay basics, build player, set rooms"""
        self.player = Player()
        self.rooms = {
            "Great Hall": {"South": "Bedroom"},
            "Bedroom": {"North": "Great Hall", "East": "Cellar"},
            "Cellar": {"West": "Bedroom"},
        }

        # Make sure to welcome player
        print("Welcome to dungean")
        print("There are five commands here to use; exit, North, South, East, and West")

    def main(self):
        """Working main class for game"""
        while self.player.get_location() != "exit":
            print(f"You are in {self.player.location}; where would you like to go?")
            movement = input().capitalize()
            if movement in self.rooms[self.player.location]:
                self.player.update_location(self.rooms[self.player.location][movement])
            elif movement == "exit":
                self.player.update_location("exit")
                sys.exit()
            else:
                print("Theres no door there?")

if __name__ == "__main__":
    game = Game()
    game.main()
