from ascii_magic import AsciiArt
from map import Map
from player import Player


class Item:
    def __init__(self):
        self.items = {
            "research_notes": {
                "name": "Research Notes",
                "description": "Notes of the summon from the lab, all neat and documented.",
                "item_image": AsciiArt.from_image("images/resaearch_notes.jpg"),
                "location": "meeting_room"
            },
            "green_slime": {
                "name": "Green Slime",
                "description": "A strang glowing green slime that was used in the summon circle?",
                "item_image": AsciiArt.from_image("images/slime.png"),
                "location": "lab"
            },
            "secret_notes": {
                "name": "Secret Notes",
                "description": "Notes of the issues with the signal that looks like something went wrong.",
                "item_image": AsciiArt.from_image("images/secret_notes.png"),
                "location": "kira_room"
            },
        }





map = Map()
print(map.location["lab"])
