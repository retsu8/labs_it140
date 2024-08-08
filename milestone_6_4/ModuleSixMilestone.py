##########################
# William Paddock
# Module 6 Milestone: Moving Between Rooms
#########################

import sys


class Player:
    """Basic player class to define play actions"""

    def __init__(self):
        """Initialize the player"""
        self.location = "Start Room"

    def update_location(self, loc):
        """Updat the player location"""
        self.location = loc

    def get_location(self):
        """Return player location"""
        return self.location


class Game:
    """Basic Game class"""

    def __init__(self):
        """Setup gameplay basics, build player, set rooms
        Create basic rooms"""
        self.rooms = {
            "Great Hall": {"South": "Bedroom"},
            "Bedroom": {"North": "Great Hall", "East": "Cellar"},
            "Cellar": {"West": "Bedroom"},
        }

        # Make sure to welcome player
        print("Welcome to dungean")
        print(
            "There are five commands here to use; exit, or go [North, South, East, and West]\n\n"
        )

    def validate_input(self, move):
        """Validate input for the go move command"""
        move = move.split(" ")

        # Check to make sure we have a go command to move with
        if "go" in move:
            move.remove("go")
            # Then find the direction intended
            for word in move:
                word = word.capitalize()
                if word in ["North", "South", "East", "West"]:
                    # Return that direction
                    return word
        
        elif "exit" in move:
            # Check for exit
            return "exit"

        # If go command not found and/or direction not used, fail input.
        return False

    def run_end_game(self):
        """Quite the game function"""
        while True:
            """Loop for an answer"""
            x = input("Would you like to quite the game? Y/N")    
            if "y" in x.lower():
                print("Thank you for playing!")
                return True
            elif "n" in x.lower():
                print("Onward!")
                return False
            else:
                print("Invalid input?")

    def main(self, player):
        """Working main class for game"""
        player.update_location("Great Hall")
        while player.get_location() != "exit":
            # Create input loop for game commands
            print(f"You are in {player.location}; where would you like to go?\n")
            movement = self.validate_input(input())
            # Validate the input loop
            if movement in self.rooms[player.location]:
                print(movement)
                # Update the player location on valid input
                player.update_location(self.rooms[player.location][movement])
            elif movement == "exit":
                # End game on exit
                loc = player.get_location()
                player.update_location("exit")
                if self.run_end_game():
                    continue
                player.update_location(loc)
            else:
                # Junk input recieved dump and try again.
                print("You cant go that way.\n")


if __name__ == "__main__":
    # Build the game
    game = Game()

    # Put the player in the game
    player = Player()
    game.main(player)
